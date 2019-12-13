# ustruct

from typing import Tuple


def calcsize(fmt: str) -> int:
    return 0


def pack(fmt: str, *values) -> bytes:
    return b""


def pack_into(fmt: str, buffer, offset: int, *values):
    ...


def unpack(fmt: str, data: bytes) -> Tuple:
    return ()


def unpack_from(fmt: str, data: bytes, offset: int = 0) -> Tuple:
    return ()
