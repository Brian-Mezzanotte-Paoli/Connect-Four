from src.setting import Refr
from src.draw import Grill
from src.matrix import Matrix
from src.strategy import IA
from src.machine import Machine

from time import sleep

class Game:
    def __init__(self, emule, mode):
        self.win = False
        self.running = True
        self.emule = emule
        self.c = True
        self.grill = Grill()
        self.matrix = Matrix()
        if not self.emule:
            self.machine = Machine()
        self.strategy = IA(self.matrix)

    def change_turn(self):
        self.turn = 3-self.turn

    def get_choice(self):
        if self.turn == Refr.PLAYER:
            if self.emule:
                self.choice = self.grill.get_position()
            else:
                self.choice = self.machine.wait_player()
        elif self.turn == Refr.COMPUTER:
            self.choice = self.strategy.get_choice()

    def state(self):
        if self.choice == Refr.QUIT:
            self.running = False
        #if self.matrix.control_victory():
        #    self.win = True

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
            if self.c:
                self.go_turn()
            else:
                sleep(0.1)
        return self.turn
