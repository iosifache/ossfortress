import os
from ctypes import CDLL, POINTER, c_char, c_char_p, c_int


def get_so_path() -> str:
    return os.path.join(
        os.path.abspath(os.path.join(__file__, os.pardir)),
        "c_modules/generate_recovery_token.so",
    )


def generate_recovery_token(user: str, length: int) -> str:
    charptr = POINTER(c_char)

    so = CDLL(get_so_path())
    so.generate_recovery_token.argtypes = [charptr, c_int]
    so.generate_recovery_token.restype = c_char_p

    user_bytes = user.encode("utf-8")
    buf = so.generate_recovery_token(user_bytes, length)

    if buf:
        buf = buf.decode("utf-8")

    return buf
