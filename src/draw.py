from setting import Opt
import pygame

class Grill:
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font(Opt.Font.NAME)
        self.screen = pygame.display.set_mode(Opt.SIZE)
        self.screen.fill(Opt.Colors.BACKGROUND)
        pygame.display.flip()

class Tokens:
    pass

class Token:
    pass
