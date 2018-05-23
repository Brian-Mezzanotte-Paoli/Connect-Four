from src.setting import Refr
from src.draw import Grill
from src.matrix import Matrix
from src.strategy import IA
from src.machine import Machine

class Game:
    def __init__(self):
        self.win = False
        self.running = True
        self.grill = Grill()
        self.matrix = Matrix()
        self.machine = Machine()
        self.strategy = IA(self.matrix)

    def change_turn(self):
        self.turn = 3-self.turn

    def get_choice(self):
        if self.turn == Refr.PLAYER:
            self.choice = self.grill.get_position()
        elif self.turn == Refr.COMPUTER:
            self.choice = self.strategy.get_choice()

    def state(self):
        if self.choice == Refr.QUIT:
            self.running = False
        if self.matrix.control_victory():
            self.win = True

    def go_turn(self):
        self.matrix.show()
        self.get_choice()
        y = self.matrix.add(self.turn,self.choice)
        self.grill.token(self.turn,self.choice,y)
        self.change_turn()
        self.state()

    def run(self, starter):
        self.turn = starter
        while not self.win and self.running:
            self.go_turn()
        return self.turn
