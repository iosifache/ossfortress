import logging
import os
import pwd
import string
import subprocess
import typing
from ctypes import CDLL, POINTER, c_char, c_char_p, c_int
from functools import wraps

import pam
from flask import (
    Flask,
    abort,
    current_app,
    jsonify,
    make_response,
    redirect,
    request,
    send_from_directory,
    session,
)

app = Flask(__name__)

app.secret_key = (
    b"192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"
)

LOG_LOCATION = "/var/log/portrait.log"
EXAMPLE_USER = "r"


def check_log_file():
    if not os.path.isfile(LOG_LOCATION):
        open(LOG_LOCATION, "w").close()
        os.chmod(LOG_LOCATION, 0o666)


check_log_file()
logging.basicConfig(
    filename=LOG_LOCATION,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


def execute_string_command(command: str, username: str = "root") -> str:
    command = command.split(" ")

    uid = get_uid(username)
    gid = get_gid(username)

    return subprocess.check_output(
        command, preexec_fn=delegate(uid, gid)
    ).decode("utf-8")


def delegate(uid: int, gid: int) -> None:
    def set_ids():
        os.setgid(uid)
        os.setuid(gid)

    return set_ids


def get_uid(username: str) -> int:
    output = execute_string_command(f"id -u {username}")
    if "no such user" in output:
        return None

    return int(output)


def get_gid(username: str) -> int:
    output = execute_string_command(f"id -g {username}")
    if "no such user" in output:
        return None

    return int(output)


def contains_allowed_characters(command: str) -> bool:
    allowed_characters = string.ascii_letters + string.digits + "\"'- ./+%{}"

    for char in command:
        if char not in allowed_characters:
            print(char)
            return False

    return True


def is_an_allowed_command(command: str) -> bool:
    ok = False
    allowed_commands = ["find", "ls", "cat", "xxd", "pwd"]
    for current in allowed_commands:
        if command.startswith(current):
            ok = True
            break

    return ok


def validate_command(command: str) -> bool:
    return is_an_allowed_command(command) and contains_allowed_characters(
        command
    )


def generate_recovery_token(user: str) -> str:
    charptr = POINTER(c_char)

    so = CDLL("./c_modules/generate_recovery_token.so")
    so.generate_recovery_token.argtypes = [charptr, c_int]
    so.generate_recovery_token.restype = c_char_p

    user_bytes = user.encode("utf-8")
    buf = so.generate_recovery_token(user_bytes, len(user))

    if buf:
        buf = buf.decode("utf-8")

    return buf


def get_all_login_users() -> typing.Generator[str, None, None]:
    for user in pwd.getpwall():
        if user[6] not in ["/usr/sbin/nologin", "/bin/false"]:
            yield user[0]


def debug_only(f):
    @wraps(f)
    def wrapped(**kwargs):
        if not current_app.debug:
            abort(404)

        return f(**kwargs)

    return wrapped


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if pam.authenticate(username, password):
            uid = get_uid(username)

            session["user"] = username
            session["uid"] = uid

            response = make_response(redirect("/dashboard"))
            response.set_cookie("uid", str(uid))

            logging.info(
                f"Authenticating user with credentials: {username}:{password}"
            )

            return response

        logging.warn(
            f"Failing authentication with credentials: {username}:{password}"
        )

        return redirect("/?error=login")

    return send_from_directory("pages", "index.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    return send_from_directory("pages", "dashboard.html")


@app.route("/command")
def execute_command():
    if "user" not in session:
        return "Authenticated route", 401

    command = request.args.get("command", None)
    if not validate_command(command):
        logging.warn(f"Dropping invalid command: {command}")

        return "Invalid command", 400
    else:
        logging.info(f"Executing valid command: {command}")

    return execute_string_command(command, session["user"])


@app.route("/username")
def translate_username_to_uid():
    uid = request.args.get("uid", None)
    if uid is None:
        return "Invalid UID", 400

    logging.info(f"Translating for username to UID: {uid}")

    output = execute_string_command(f"id -nu {uid}")
    if "no such user" in output:
        return "N/A"

    return output


@app.route("/logout")
def logout():
    if "user" not in session:
        return "Authenticated route", 401

    logging.info(f"Logging out user: {session['user']}")

    session.pop("user")

    return redirect("/")


@app.route("/recovery")
def recovery():
    return send_from_directory("pages", "recovery.html")


@app.route("/example_recovery_token")
def generate_example_recovery_token():
    logging.info("Requesting example recovery token")

    return jsonify(
        {"user": EXAMPLE_USER, "token": generate_recovery_token(EXAMPLE_USER)}
    )


@app.route("/craft_recovery_token")
@debug_only
def craft_recovery_token():
    username = request.args.get("username", None)

    logging.warn(f"Generating token for user: {username}")

    return jsonify(
        {"user": username, "token": generate_recovery_token(username)}
    )


@app.route("/recovery_command")
def execute_recovery_command():
    username = request.args.get("username", None)
    token = request.args.get("token", None)
    command = request.args.get("command", None)

    if username in get_all_login_users() and token == generate_recovery_token(
        username
    ):
        logging.warn(
            f"Executing recovery command under user {username} with token"
            f" {token}: {command}"
        )

        return execute_string_command(command, username)
    else:
        logging.warn(
            f"Dropping recovery command under user {username} with token"
            f" {token}: {command}"
        )

        return "Authenticated route", 401


def main() -> None:
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
