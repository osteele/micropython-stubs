# esp

import enum
from typing import Optional

LOG_DEBUG = 4
LOG_ERROR = 1
LOG_INFO = 3
LOG_NONE = 0
LOG_VERBOSE = 5
LOG_WARNING = 2

SLEEP_NONE = 1
SLEEP_MODEM = 2
SLEEP_LIGHT = 3


class SleepType(enum.IntEnum):
    SLEEP_NONE = 1
    SLEEP_MODEM = 2
    SLEEP_LIGHT = 3


def sleep_type(sleep_type: SleepType = None) -> SleepType:
    ...


def deepsleep(time: int):
    ...


def flash_id() -> bytes:
    ...


def flash_size() -> int:
    ...


def flash_user_start() -> int:
    ...


def flash_read(byte_offset: int, length_or_buffer: int) -> bytes:
    ...


def flash_write(byte_offset: int, bytes: bytes):
    ...


def flash_erase(sector_no: int):
    ...


def set_native_code_location(start: int, length: int):
    ...


def osdebug(param: Optional[int]):
    pass
