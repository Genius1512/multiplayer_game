import socket


class Server:
    def __init__(self):
        self.ip = "0.0.0.0"
        self.port = 5555
        self.max_players = 10

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(self.max_players)


def main():
    server = Server()


if __name__ == "__main__":
    main()
