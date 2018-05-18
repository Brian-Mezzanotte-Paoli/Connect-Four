from cmd import Cmd

from src.match import Game

class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.game = Game()
        self.do_quit = lambda _: True
        self.run = self.cmdloop

    def do_choice(self):
        self.game.


if __name__ == "__main__":
    Cli().run()
