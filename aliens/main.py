"""
This is the main module of the application.
"""
import pygame
from pygame.sprite import Group

import aliens.game_functions as gf
from aliens.settings import Settings
from aliens.ship.base import BaseShip


def run_game():
    # Game initialization and screen object creation.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Initiate spaceship
    ship = BaseShip(ai_settings=ai_settings, screen=screen)

    # Initiate spaceships bullets
    bullets = Group()

    # Main loop
    while True:
        # Wait for key or mouse button being pressed
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)


if __name__ == "__main__":
    run_game()
