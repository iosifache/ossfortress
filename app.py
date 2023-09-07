from flask import Flask, send_from_directory, request, redirect, session, make_response
import pam
import os
import subprocess
import string

app = Flask(__name__)

app.secret_key = b"192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"

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
            session["user"] = username

            uid = get_uid(username)
            session["uid"] = uid

            response = make_response(redirect('/dashboard'))
            response.set_cookie('uid', str(uid))

            return response

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
def command():
    if ("user" not in session):
        return "Authenticated route", 401

    command = request.args.get("command", None)
    if not validate_command(command):
        return "Invalid command", 400

    return execute_string_command(command)

@app.route("/username")
def username():
    uid = request.args.get("uid", None)
    uid = int(uid)
    if (uid == None):
        return "Invalid UID", 400

    output = execute_string_command(f"id -nu {uid}")
    if "no such user" in output:
        return "N/A"

    return output

@app.route("/logout")
def logout():
    session.pop("user")

    return redirect("/")