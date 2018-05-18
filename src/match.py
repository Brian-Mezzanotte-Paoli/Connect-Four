from src.setting import Refr
from src.draw import Grill
from src.matrix import Matrix
from src.strategy import IA
class Game:
    def __init__(self,):
        self.win = False
        self.running = True
        self.grill = Grill()
        self.matrix = Matrix()
        self.strategy = IA()

    def change_turn(self):
        self.turn = 3-self.turn

    def play(self, starter):
        self.turn = starter
        while not self.win and self.running:
            if self.turn == Refr.PLAYER:
                choice = self.grill.get_position()
            elif self.turn == Refr.COMPUTER:
                choice = self.strategy.get_choice()
            y = self.matrix.add(self.turn,choice)
            self.grill.token(self.turn,choice,y)
            self.change_turn()
            if choice == Refr.QUIT:
                self.running = False
            if self.matrix.control_victory():
                self.win = True
