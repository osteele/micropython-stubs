# machine

from __future__ import annotations

from typing import Callable, Optional, overload


class Pin:
    # Modes
    IN: int
    OUT: int
    OPEN_DRAIN: int
    ALT: int
    ALT_OPEN_DRAIN: int

    # Pull
    PULL_UP: int
    PULL_DOWN: int

    # Drive
    LOW_POWER: int
    MED_POWER: int
    HIGH_POWER: int

    # IRQ
    IRQ_FALLING: int
    IRQ_RISING: int
    IRQ_LOW_LEVEL: int
    IRQ_HIGH_LEVEL: int

    # IRQ Wake
    IDLE: int
    SLEEP: int
    DEEPSLEEP: int

    def __init__(
        self,
        id: int,
        mode: int = -1,
        pull: int = -1,
        *,
        value: int = 0,
        drive: int = 0,
        alt: int = 0
    ):
        ...

    def init(
        self,
        mode: int = -1,
        pull: int = -1,
        *,
        value: int = 0,
        drive: int = 0,
        alt: int = 0
    ):
        ...

    @overload
    def value(self, value: int):
        ...

    @overload
    def value(self) -> int:
        ...

    def value(self, value: Optional[int] = None):
        pass

    def on(self):
        ...

    def off(self):
        ...

    @overload
    def mode(self, value: int):
        ...

    @overload
    def mode(self) -> int:
        ...

    def mode(self, value: Optional[int] = None):
        pass

    @overload
    def pull(self, pull: int):
        ...

    @overload
    def pull(self) -> int:
        ...

    def pull(self, pull: Optional[int] = None):
        pass

    @overload
    def drive(self, drive: int):
        ...

    @overload
    def drive(self) -> int:
        ...

    def drive(self, drive: Optional[int] = None):
        pass

    def irq(
        self,
        handler: Callable[[Pin], None],
        trigger: int,
        *,
        priority: int = 1,
        wake: Optional[int] = None,
        hard: bool = False
    ):
        ...
