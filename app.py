from flask import Flask, send_from_directory, request, redirect, session, make_response
import pam
import os
import subprocess
import string
import logging

app = Flask(__name__)

app.secret_key = b"192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"

LOG_LOCATION = "/var/log/portrait.log"

def check_log_file():
    if not os.path.isfile(LOG_LOCATION):
        open(LOG_LOCATION, "w").close()
        os.chmod(LOG_LOCATION, 0o666)


check_log_file()
logging.basicConfig(filename=LOG_LOCATION,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def execute_string_command(command: str) -> str:
    command = command.split(" ")

    return subprocess.check_output(command).decode("utf-8")

def get_uid(username: str) -> int:
    output = execute_string_command(f"id -u {username}")
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
    return is_an_allowed_command(command) and contains_allowed_characters(command)


@app.route("/", methods = ["POST", "GET"])
def home():
    if(request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
 
        if pam.authenticate(username, password):
            uid = get_uid(username)

            session["user"] = username
            session["uid"] = uid

            response = make_response(redirect('/dashboard'))
            response.set_cookie('uid', str(uid))

            logging.info(f"Authenticating user with credentials: {username}:{password}")

            return response

        logging.warn(f"Failing authentication with credentials: {username}:{password}")

        return redirect("/?error=login")

    return send_from_directory("pages", "index.html")


@app.route("/recovery")
def recovery():
    return send_from_directory("pages", "recovery.html")


@app.route("/dashboard")
def dashboard():
    if ("user" not in session):
        return redirect("/")

    return send_from_directory("pages", "dashboard.html")

@app.route("/command")
def execute_command():
    if ("user" not in session):
        return "Authenticated route", 401

    command = request.args.get("command", None)
    if not validate_command(command):
        logging.warn(f"Dropping invalid command: {command}")

        return "Invalid command", 400
    else:
        logging.info(f"Executing valid command: {command}")

    return execute_string_command(command)

@app.route("/username")
def translate_username_to_uid():
    uid = request.args.get("uid", None)
    if (uid == None):
        return "Invalid UID", 400

    logging.info(f"Translating for username to UID: {username}")

    output = execute_string_command(f"id -nu {uid}")
    if "no such user" in output:
        return "N/A"

    return output

@app.route("/logout")
def logout():
    if ("user" not in session):
        return "Authenticated route", 401

    logging.info(f"Logging out user: {session['user']}")

    session.pop("user")

    return redirect("/")