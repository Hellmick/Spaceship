from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, r_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, r_settings)