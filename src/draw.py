from setting import Opt, Refr
import pygame


def draw_rect(surface, rect, color, thickness=0):
    pygame.draw.rect(surface, color, rect, thickness)
def draw_circle(surface, pos, radius, color, thickness=0):
    pygame.draw.circle(surface, color, pos, radius, thickness)
def draw_token(surface, pos, color):
    draw_circle(surface,pos,Opt.Token.RADIUS,color)

class Grill:
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font(Opt.Font.NAME)
        self.screen = pygame.display.set_mode(Opt.Window.SIZE)
        self.screen.fill(Opt.Colors.BACKGROUND)
        self.mount_under()
        self.mount_upper()
        self.screen.blit(self.under_screen, (0,0))
        self.screen.blit(self.upper_screen, (0,0))
        self.tokens = pygame.sprite.Group()
        pygame.display.flip()

    def mount_under(self):
        self.under_screen = pygame.Surface(Opt.Window.SIZE)
        self.under_screen.set_colorkey(Opt.Colors.KEY)
        draw_rect(self.under_screen,Opt.Window.RECT, Opt.Colors.EMPTY)

    def mount_upper(self):
        self.upper_screen = pygame.Surface(Opt.Window.SIZE)
        self.upper_screen.set_colorkey(Opt.Colors.KEY)
        draw_rect(self.upper_screen,Opt.Window.RECT, Opt.Colors.GRILL)
        for y in range(Opt.Window.NY):
            for x in range(Opt.Window.NX):
                center = (x*Opt.Token.SIZE + Opt.Window.MARGIN + Opt.Token.SIZE/2,
                        y*Opt.Token.SIZE + Opt.Window.MARGIN + Opt.Token.SIZE/2)
                draw_token(self.upper_screen,center,Opt.Colors.KEY)

    def get_position(self):
        key = None
        while not key in list(range(7)):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.key - 49
                elif event.type == pygame.QUIT:
                    return Refr.QUIT
        return key

    def token(self, turn, x, y):
        token = Token(turn,x,y)
        self.tokens.add(token)
        while token.rect.y < token.desty:
            now = pygame.time.get_ticks()
            if now - token.last_move > token.speed:
                token.rect.y += 10
                self.screen.fill(Opt.Colors.BACKGROUND)
                self.screen.blit(self.under_screen,(0,0))
                self.tokens.draw(self.screen)
                self.screen.blit(self.upper_screen,(0,0))
                self.last_move = now
                pygame.display.flip()


class Token(pygame.sprite.Sprite):
    def __init__(self,turn,x,y):
        pygame.sprite.Sprite.__init__(self)
        if turn == Refr.PLAYER: self.color = Opt.Colors.PLAYER
        elif turn == Refr.COMPUTER: self.color = Opt.Colors.COMPUTER
        self.desty = y * Opt.Token.SIZE + Opt.Window.MARGIN
        self.image = pygame.Surface((Opt.Token.SIZE,Opt.Token.SIZE))
        draw_token(self.image,(Opt.Token.SIZE/2,Opt.Token.SIZE/2),self.color)
        self.image.set_colorkey(Opt.Colors.KEY)
        self.rect = self.image.get_rect()
        self.rect.x = x * Opt.Token.SIZE + Opt.Window.MARGIN
        self.rect.y = -Opt.Token.SIZE
        self.speed = Opt.Token.SPEED
        self.last_move = 0
