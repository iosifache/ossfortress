import string


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
