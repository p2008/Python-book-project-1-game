"""
This module contains the application logic.
"""
import sys

import pygame


def check_events(ship):
    """
    Events triggered by keyboard and mouse.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event=event, ship=ship)

        elif event.type == pygame.KEYUP:
            _check_keyup_events(event=event, ship=ship)


def _check_keydown_events(event, ship):
    """
    Events triggered by pressing a key.

    :param event: pygame event object
    :param ship: instance of Ship class
    """
    if event.key == pygame.K_RIGHT:
        # Move ship right side
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move ship left side
        ship.moving_left = True


def _check_keyup_events(event, ship):
    """
    Events triggered by releasing a key.

    :param event: pygame event object
    :param ship: instance of Ship class
    """
    if event.key == pygame.K_RIGHT:
        # Cancel ship right side movement
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        # Cancel ship left side movement
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """
    Update the images on the screen and go to new one.

    :param ai_settings: An instance of the Settings class.
    :param screen: App screen object.
    :param ship: An instance of the BaseShip class.
    """
    # Screen refresh
    screen.fill(ai_settings.bg_color)
    ship.blit_me()

    # Display last screen shown
    pygame.display.flip()
