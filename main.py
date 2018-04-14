
from src.match import Game
from logger import Logger

def main(argv):
    logger = Logger()
    g = Game(logger)
    g.play(1)

if __name__ == "__main__":
    import sys
    main(sys.argv)
