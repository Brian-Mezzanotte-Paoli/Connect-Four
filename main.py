from threading import Thread

from src.match import Game
from cli import Cli


def main(argv):
    g = Game()
    c = Cli(g)

    game = Thread(target=g.run, args=(1,))
    cli = Thread(target=c.run)

    game.start()
    cli.start()

if __name__ == "__main__":
    import sys
    main(sys.argv)
