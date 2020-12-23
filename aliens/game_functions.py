import sys

import pygame


def check_events():
    """
    Events triggered by keyboard and mouse
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """
    Update the images on the screen and go to new one.

    :param ai_settings: An instance of the Settings class
    :param screen: App screen object
    :param ship: An instance of the BaseShip class
    """
    # Screen refresh
    screen.fill(ai_settings.bg_color)
    ship.blit_me()

    # Display last screen shown
    pygame.display.flip()
