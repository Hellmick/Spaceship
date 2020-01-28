import pygame

class Spaceship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery * 1.8
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_x = 0
        self.moving_y = 0

    def update(self, speed):
        if (self.rect.right < self.screen_rect.right or self.moving_x < 0) and (self.moving_x > 0 or self.rect.left > self.screen_rect.left):
            self.centerx += self.moving_x * speed
        if (self.rect.bottom < self.screen_rect.bottom or self.moving_y < 0) and (self.moving_y > 0 or self.rect.top > self.screen_rect.top):
            self.centery += self.moving_y * speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        

