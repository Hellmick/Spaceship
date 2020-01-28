import pygame
import sys
from spaceship import Spaceship
from settings import Settings

def check_keydown_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_x = -1
    elif event.key == pygame.K_RIGHT:
        ship.moving_x = 1
    if event.key == pygame.K_UP:
        ship.moving_y = -1
    elif event.key == pygame.K_DOWN:
        ship.moving_y = 1

def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        ship.moving_x = 0
    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        ship.moving_y = 0

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(bg, screen, ship):
    screen.fill(bg)
    ship.blitme()
    pygame.display.flip()