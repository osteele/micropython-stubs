from typing import List, Tuple, Union

from .pin import Pin


class I2C:
    def __init__(
        self, id: int = -1, *, scl: Pin, sda: Pin, freq: int = 400000, timeout: int = 0
    ):
        ...

    # General Methods
    def init(
        self, id: int = -1, *, scl: Pin, sda: Pin, freq: int = 400000, timeout: int = 0
    ):
        ...

    def deinit(self):
        ...

    def scan(self) -> List[int]:
        return []

    # Primitive I2C Operations
    def start(self):
        ...

    def stop(self):
        ...

    def readinto(self, buf: bytes, nack: bool = True):
        ...

    def write(self, buf: bytes) -> int:
        ...

    # Standard bus operations
    def readfrom(self, addr: int, nbytes: int, stop: bool = True) -> bytes:
        ...

    def readfrom_into(self, addr: int, buf: bytes, stop: bool = True):
        ...

    def writeto(self, addr: int, buf: bytes, stop: bool = True) -> int:
        ...

    def writevto(self, addr: int, vector: Union[Tuple, List], stop: bool = True) -> int:
        ...

    # Memory operations
    def readfrom_mem(
        self, addr: int, memaddr: int, nbytes: int, *, addrsize: int = 8
    ) -> bytes:
        ...

    def readfrom_mem_into(
        self, addr: int, memaddr: int, buf: bytes, *, addrsize: int = 8
    ):
        ...

    def writeto_mem(self, addr: int, memaddr: int, buf: bytes, *, addrsize: int = 8):
        ...
