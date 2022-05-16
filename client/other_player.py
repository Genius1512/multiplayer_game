import peapy2

from other_player_networking import OtherPlayerNetworking


class OtherPlayer(peapy2.GameObject):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name)

        self.transform = None
        self.renderer = None
        self.other_player_networking = None

        self.x = x
        self.y = y

    # Called when the object is created
    def init(self):
        self.transform = self.add_component(peapy2.Transform(
            self.x,
            self.y,
            50,
            50
        ))
        del self.x, self.y

        self.renderer = self.add_component(peapy2.ShapeRenderer(
            "rectangle",
            peapy2.Color(255, 0, 0)
        ))

        self.other_player_networking = self.add_component(OtherPlayerNetworking(
            
        ))

    # Called when the object gets updated
    def update(self):
        pass

    # Called when the object is destroyed
    def destroy(self):
        pass
