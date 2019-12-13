# machine

IDLE: int
SLEEP: int
DEEPSLEEP: int

PWRON_RESET: int
HARD_RESET: int
WDT_RESET: int
DEEPSLEEP_RESET: int
SOFT_RESET: int

WLAN_WAKE: int
PIN_WAKE: int
RTC_WAKE: int


def unique_id() -> bytes:
    ...


def reset():
    ...


def reset_cause():
    ...


def disable_irq():
    ...


def enable_irq(state):
    ...


def freq():
    ...


def idle():
    ...


def sleep():
    ...


def lightsleep(time_ms: int = 0):
    ...


def deepsleep(time_ms: int = 0):
    ...


def wake_reason():
    ...


def time_pulse_us(pin, pulse_level, timeout_us: int = 1000000):
    ...


def rng():
    ...
