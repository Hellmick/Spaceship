import sys
import pygame
from settings import Settings
from spaceship import Spaceship
import func as f

def run_game():
    pygame.init()

    r_settings = Settings()
    screen = pygame.display.set_mode((r_settings.screen_width, r_settings.screen_height))

    pygame.display.set_caption("WIELKA KURWA RAKIETA")
    spaceship = Spaceship(screen)

    while True:
        f.check_events(spaceship)
        spaceship.update(r_settings.speed_factor)
        f.update_screen(r_settings.background, screen, spaceship)

run_game()