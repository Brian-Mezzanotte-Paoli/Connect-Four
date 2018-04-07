PLAYER, COMPUTER = 1,2

class Game:
    def __init__(self):
        self.win = False

    def change_turn(self):
        self.turn = 3-self.turn

    def play(self, starter):
        self.turn = starter
        while not self.win:
            if self.turn = PLAYER:
                pass
            elif self.turn == COMPUTER:
                pass

            self.change_turn()
