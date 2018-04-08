from setting import Refr

class Game:
    def __init__(self):
        self.win = False

    def change_turn(self):
        self.turn = 3-self.turn

    def play(self, starter):
        self.turn = starter
        while not self.win:
            if self.turn = Refr.PLAYER:
                pass
            elif self.turn == Refr.COMPUTER:
                pass

            self.change_turn()
