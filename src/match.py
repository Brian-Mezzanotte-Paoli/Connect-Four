from setting import Refr
from draw import Grill
from matrix import Matrix
from strategy import IA
class Game:
    def __init__(self,logger):
        self.logger = logger
        self.win = False
        self.running = True
        self.grill = Grill(logger)
        self.matrix = Matrix(logger)
        self.strategy = IA()
        self.logger.start()

    def change_turn(self):
        self.turn = 3-self.turn

    def play(self, starter):
        self.turn = starter
        while not self.win and self.running:
            self.logger.debug("new round: turn player " + str(self.turn))
            if self.turn == Refr.PLAYER:
                choice = self.grill.get_position()
            elif self.turn == Refr.COMPUTER:
                choice = self.strategy.get_choice()
            print(choice,self.turn)
            y = self.matrix.add(self.turn,choice-1)
            self.grill.token(self.turn,choice,y)
            self.change_turn()
            if choice == Refr.QUIT:
                self.running = False
            if self.matrix.control_victory():
                self.win = True
        self.logger.quit()
