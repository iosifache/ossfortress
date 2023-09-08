import logging
import os
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

from portrait.confinement import validate_command
from portrait.os_ops import (
    execute_string_command,
    get_all_login_users,
    get_uid,
)
from portrait.recovery import generate_recovery_token
from portrait.uploader import extract_archive_in_user_home

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


@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session:
        return "Authenticated route", 401

    if "archive" not in request.files:
        return "No archive", 400

    username = session["user"]
    dest = request.args.get("dest", None)

    extracted = extract_archive_in_user_home(
        request.files["archive"], username, dest
    )
    if extracted:
        logging.info(f"Uploading archive to ~/{dest} for user: {username}")

        return ""
    else:
        logging.warn(
            f"Failing to upload archive to ~/{dest} for user: {username}"
        )

        return "Issues when unarchiving the file", 400


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
        {
            "user": EXAMPLE_USER,
            "token": generate_recovery_token(EXAMPLE_USER, len(EXAMPLE_USER)),
        }
    )


@app.route("/craft_recovery_token")
@debug_only
def craft_recovery_token():
    username = request.args.get("username", None)

    logging.info(f"Generating token for user: {username}")

    return jsonify(
        {
            "user": username,
            "token": generate_recovery_token(username, len(username)),
        }
    )


@app.route("/recovery_command")
def execute_recovery_command():
    username = request.args.get("username", None)
    length = int(request.args.get("length", None))
    token = request.args.get("token", None)
    command = request.args.get("command", None)

    if (
        token == generate_recovery_token(username, length)
        and username in get_all_login_users()
    ):
        logging.info(
            f"Executing recovery command under user {username} with token"
            f" {token}: {command}"
        )

        return execute_string_command(command, username)
    else:
        logging.warn(
            f"Dropping recovery command under user {username} with token"
            f" {token}: {command}"
        )

        return "Bad username or token", 401


def main() -> None:
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
