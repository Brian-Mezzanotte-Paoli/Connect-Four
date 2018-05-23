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

    def do_reset(self, arg):
        mac = self.game.machine
        mac.reset()

    def do_run(self, arg):
        mac = self.game.machine
        mac.run(arg)

    def do_show(self, arg):
        self.game.matrix.show()

    def do_wait_player(self, arg):
        mac = self.game.machine
        mac.wait_player()

    def do_stop(self, arg):
        mac = self.game.machine
        mac.c = False

    def do_clear(self, arg):
        mac = self.game.machine
        mac.open_ports_lists(self.game.matrix.m)
