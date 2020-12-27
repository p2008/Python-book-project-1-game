"""
This module contains the application logic.
"""
import sys

import pygame

from aliens.bullet.base import BaseBullet


def update_bullets(bullets):
    """
    Update bullets on the screen and removal of off screen bullets.

    :param bullets: instance of pygame Group class containing bullet instances
    """
    bullets.update()

    # Remove bullets that gone off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_events(ai_settings, screen, ship, bullets):
    """
    Events triggered by keyboard and mouse.
    :param ai_settings: An instance of the Settings class.
    :param screen: App screen object.
    :param ship: An instance of the BaseShip class.
    :param bullets: An instance of the BaseBullet class.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event=event, ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)

        elif event.type == pygame.KEYUP:
            _check_keyup_events(event=event, ship=ship)


def _check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    Events triggered by pressing a key.

    :param event: pygame event object
    :param ai_settings: An instance of the Settings class.
    :param screen: App screen object.
    :param ship: An instance of the BaseShip class.
    :param bullets: An instance of the BaseBullet class.
    """
    if event.key == pygame.K_RIGHT:
        # Move ship right side
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move ship left side
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        _fire_bullet(ai_settings=ai_settings, bullets=bullets, screen=screen, ship=ship)


def _fire_bullet(ai_settings, bullets, screen, ship):
    """
    Create new bullet if the bullets limit wasn't reached.

    :param ai_settings: An instance of the Settings class.
    :param bullets: An instance of the BaseBullet class.
    :param screen: App screen object.
    :param ship: An instance of the BaseShip class.
    """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = BaseBullet(ai_settings=ai_settings, screen=screen, ship=ship)
        bullets.add(new_bullet)


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


def update_screen(ai_settings, screen, ship, bullets):
    """
    Update the images on the screen and go to new one.

    :param ai_settings: An instance of the Settings class.
    :param screen: App screen object.
    :param ship: An instance of the BaseShip class.
    :param bullets: An instance of the BaseBullet class.
    """
    screen.fill(ai_settings.bg_color)

    # Bullets refresh under the layers of ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Ship refresh
    ship.blit_me()

    # Display last screen shown
    pygame.display.flip()
