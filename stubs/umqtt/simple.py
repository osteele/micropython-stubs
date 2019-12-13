# umqtt.simple


class MQTTException(Exception):
    ...

 
class MQTTClient:
    server = None
    port: int

    def __init__(
        self,
        client_id,
        server,
        port: int = 0,
        user=None,
        password=None,
        keepalive=0,
        ssl=False,
        ssl_params={},
    ):
        ...

    def set_callback(self, cb):
        ...

    def set_last_will(self, topic: str, msg: str, retain: bool = False, qos=0):
        ...

    def connect(self, clean_session: bool = False):
        ...

    def disconnect(self):
        ...

    def publish(self, topic: str, msg: str, retain: bool = False, qos: int = 0):
        ...

    def subscribe(self, topic: str, qos: int = 0):
        ...

    def wait_msg(self):
        ...
