import pygame

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
    ship = BaseShip(screen=screen)

    # Main loop
    while True:
        # Wait for key or mouse button being pressed
        gf.check_events()
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship)


if __name__ == "__main__":
    run_game()
