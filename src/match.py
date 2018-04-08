from setting import Refr
from draw import Grill

class Game:
    def __init__(self):
        self.win = False
        self.grill = Grill()

    def change_turn(self):
        self.turn = 3-self.turn

    def play(self, starter):
        self.turn = starter
        while not self.win:
            if self.turn == Refr.PLAYER:
                pass
            elif self.turn == Refr.COMPUTER:
                pass

            self.change_turn()
