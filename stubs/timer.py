# timer

from typing import Callable

TimerCallbackType = Callable[int]


class Timer:
    PERIODIC: int
    ONE_SHOT: int
    PWM: int
    A: int
    B: int
    POSITIVE: int
    NEGATIVE: int
    TIMEOUT: int
    MATCH: int

    def __init__(self, id: int = 0):
        ...

    def init(
        self,
        *,
        mode: int = Timer.PERIODIC,
        period: int = -1,
        callback: TimerCallbackType = None
    ):
        ...

    def deinit(self):
        ...
