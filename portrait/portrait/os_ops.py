import os
import pwd
import subprocess
import typing


def get_all_login_users() -> typing.Generator[str, None, None]:
    for user in pwd.getpwall():
        if user[6] not in ["/usr/sbin/nologin", "/bin/false"]:
            yield user[0]


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


def get_home_dir(username: str) -> str:
    return pwd.getpwnam(username).pw_dir


def delegate(uid: int, gid: int) -> None:
    def set_ids():
        os.setgid(uid)
        os.setuid(gid)

    return set_ids


def execute_string_command(command: str, username: str = "root") -> str:
    command = command.split(" ")

    if username != "root":
        uid = get_uid(username)
        gid = get_gid(username)

        output = subprocess.check_output(
            command, preexec_fn=delegate(uid, gid)
        )

    else:
        output = subprocess.check_output(command)

    return output.decode("utf-8")
