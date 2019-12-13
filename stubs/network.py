# network

from typing import List, Optional, Tuple

IFConfigType = Tuple[str, str, str, str]

AP_IF: int
STA_IF: int


class AbstractNIC:
    def __init__(self, id: None):
        ...

    def active(self, is_active: Optional[bool]) -> Optional[bool]:
        ...

    # def connect(self, service_id, key=None, *_):
    #     ...

    def disconnect(self):
        ...

    def isconnected(self) -> bool:
        ...

    # def scan(self) -> List[Tuple]:
    #     ...

    def status(self, param: str) -> str:
        ...

    def ifconfig(self, config: Optional[IFConfigType] = None) -> IFConfigType:
        return ("", "", "", "")

    def config(self, key: Optional[str]) -> Optional[str]:
        ...


MODE_11B: int
MODE_11G: int
MODE_11N: int


PhyMode = int  # MODE_11B | MODE_11G | MODE_11N


def phy_mode(mode: Optional[PhyMode]) -> Optional[PhyMode]:
    ...


class WLAN(AbstractNIC):
    def __init__(self, _):
        ...

    def connect(
        self,
        ssid: Optional[str] = None,
        password: Optional[str] = None,
        *,
        bssid: Optional[str] = None
    ):
        ...

    # -> (ssid, bssid, channel, RSSI, authmode, hidden)
    def scan(self) -> Tuple[str, str, str, str, int, int]:
        return ("", "", "", "", 0, 0)
