class User():
    def __init__(self, sock, ip, port, name=None):
        self._sock = sock
        self._ip = ip
        self._port = port
        if name is None:
            self.name = ip
        else:
            self.name = name

    @property
    def sock(self):
        return self._sock

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

