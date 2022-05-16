import peapy2

from player_controller import PlayerController
from player_networking import PlayerNetworking


class Player(peapy2.GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.transform = None
        self.renderer = None
        self.player_controller = None
        self.player_networking = None

    # Called when the object is created
    def init(self):
        self.transform = self.add_component(peapy2.Transform(
            100,
            100,
            50,
            50
        ))

        self.renderer = self.add_component(peapy2.ShapeRenderer(
            "rectangle",
            peapy2.Color(0, 255, 0)
        ))

        self.player_controller = self.add_component(PlayerController(
            3
        ))

        self.player_networking = self.add_component(PlayerNetworking(
            
        ))

    # Called when the object gets updated
    def update(self):
        pass

    # Called when the object is destroyed
    def destroy(self):
        pass
