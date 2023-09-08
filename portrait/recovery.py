from ctypes import CDLL, POINTER, c_char, c_char_p, c_int


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
