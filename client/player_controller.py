import peapy2

import keyboard


class PlayerController(peapy2.Component):
    NAME = "PlayerController"

    def __init__(self, velocity: int = 1):
        super().__init__()

        self.velocity = velocity

    # Called when the component is created
    def init(self):
        pass

    # Called when the game gets updated
    def update(self):
        if keyboard.is_pressed("w"):
            self.game_object.transform.y -= self.velocity
        if keyboard.is_pressed("s"):
            self.game_object.transform.y += self.velocity
        if keyboard.is_pressed("a"):
            self.game_object.transform.x -= self.velocity
        if keyboard.is_pressed("d"):
            self.game_object.transform.x += self.velocity

    # Called when the component is destroyed
    def destroy(self):
        pass
