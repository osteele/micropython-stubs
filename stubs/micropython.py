# micropython

from typing import Optional, TypeVar, overload

T = TypeVar("T")


def const(expr: T) -> T:
    return expr


@overload
def opt_level(level: int):
    ...


@overload
def opt_level() -> int:
    ...


def opt_level(level: Optional[int] = None):
    pass


def alloc_emergency_exception_buf(size: int):
    ...


def heap_lock():
    ...


def heap_unlock():
    ...


def kbd_intr(chr: int):
    ...


def mem_info(verbose: Optional[bool]):
    ...


def qstr_info(verbose: Optional[bool]):
    ...


def schedule(func, arg):
    ...


def stack_use():
    pass
