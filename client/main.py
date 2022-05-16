import peapy2

from other_player import OtherPlayer
from player import Player


def main():
    game = peapy2.PeaPy("PeaPy", 800, 600, peapy2.Color(255, 255, 255))

    player = game.add_object(Player(
        "Player"
    ))

    other_player = game.add_object(OtherPlayer(
        "OtherPlayer",
        200,
        200
    ))

    while game.update():
        pass
        

if __name__ == "__main__":
    main()
