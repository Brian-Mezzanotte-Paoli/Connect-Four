from threading import Thread

from src.match import Game
from cli import Cli



def main(argv):

    _, mode, starter, emule = ["main.py", "pc", "1", "1"]

    emule = bool(int(emule))    # '0' -> 0 -> False
                                # '1' -> 1 -> True
    starter = int(starter)
    g = Game(bool(emule), mode)
    c = Cli(g)

    game = Thread(target=g.run, args=(starter,))
    cli = Thread(target=c.run)

    game.start()
    cli.start()

if __name__ == "__main__":
    import sys
    main(sys.argv)
