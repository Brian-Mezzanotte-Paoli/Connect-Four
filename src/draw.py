from setting import Opt
import pygame

class Grill:
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font(Opt.Font.NAME)
        self.screen = pygame.display.set_mode(Opt.SIZE)
        self.screen.fill(Opt.Colors.BACKGROUND)
        pygame.display.flip()

    def get_position(self):
        key = None
        while not key in list(range(7)):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.key - 49
                elif event.type == pygame.QUIT:
                    return -1
        return key

class Tokens:
    pass

class Token:
    pass
