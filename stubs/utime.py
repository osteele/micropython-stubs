# time

from typing import Optional, Tuple

TimeTupleType = Tuple[int, int, int, int, int, int, int, int]


def localtime(ms: Optional[int] = 0) -> TimeTupleType:
    pass


def mktime() -> TimeTupleType:
    return (0, 0, 0, 0, 0, 0, 0, 0)


def sleep(seconds: int):
    pass


def sleep_ms(ms: int) -> int:
    return 0


def sleep_us(us: int):
    pass


def ticks_ms() -> int:
    return 0


def ticks_us() -> int:
    return 0


def ticks_cpu() -> int:
    return 0


def ticks_add(ticks: int, delta: int) -> int:
    return 0


def ticks_diff(ticks1: int, ticks2: int) -> int:
    return 0


def time() -> int:
    return 0
