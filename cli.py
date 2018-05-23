from cmd import Cmd

class Cli(Cmd):
    def __init__(self, game):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.game = game
        self.do_quit = lambda _: True
        self.run = self.cmdloop

    def do_elev(self, arg):
        mac = self.game.machine
        if arg == "up":
            mac.play_elev_up(2)


if __name__ == "__main__":
    Cli().run()
