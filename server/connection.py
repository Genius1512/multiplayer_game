from pickle import loads, dumps
import socket
from threading import Thread
from typing import Any


class Connection(Thread):
    def __init__(self, server: socket.socket):
        super().__init__(
            target=self.handle_client,
            daemon=True
        )

        self.server = server
        self.socket = None

        self.start()

    def handle_client(self):
        self.socket, _ = self.server.accept()

        while True:
            pass

    def send(self, data: Any):
        self.socket.send(dumps(data))

    def receive(self) -> Any:
        return loads(self.socket.recv(1024))
