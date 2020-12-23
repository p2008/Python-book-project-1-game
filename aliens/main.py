import sys

import pygame
from aliens.settings import Settings


def run_game():
    # Game initialization and screen object creation.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # Main loop
    while True:

        # Wait for key or mouse button being pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        # Display last screen seen
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
