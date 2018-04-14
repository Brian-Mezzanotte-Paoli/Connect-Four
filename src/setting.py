class RGB:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,80,255)
    DARKBLUE = (10,10,200)
    YELLOW = (255,255,0)
    PURPLE = (255,0,255)
    LIGHTBLUE = (0,255,255)
    GREY = (100,100,100)

class Opt:
    class Window:
        WIDTH = 740
        HEIGHT = 640
        SIZE = WIDTH, HEIGHT
        MARGIN = 20
        NX = 7
        NY = 6
        RECT = (MARGIN,MARGIN,WIDTH-MARGIN*2,HEIGHT-MARGIN*2)
    class Token:
        SIZE = 100
        RADIUS = 40
        SPEED = 10
    class Colors:
        PLAYER = RGB.YELLOW
        COMPUTER = RGB.RED
        EMPTY = RGB.WHITE
        DECORATION = RGB.DARKBLUE
        GRILL = RGB.BLUE
        BACKGROUND = RGB.GREY
        KEY = RGB.BLACK
    class Font:
        NAME = "arial"
        COLOR = RGB.BLACK
        SIZE = 18


class Refr:
    PLAYER = 1
    COMPUTER = 2
    QUIT = -1
    ERROR = -2
