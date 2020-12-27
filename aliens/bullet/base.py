"""
This module contains base bullet class and configuration
"""
import pygame
from pygame.sprite import Sprite


class BaseBullet(Sprite):
    """
    Base class for ship bullets
    """

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Bullet settings
        self.speed_factor = ai_settings.bullet_speed_factor
        self.width = ai_settings.bullet_width
        self.height = ai_settings.bullet_height
        self.color = ai_settings.bullet_color

        # Bullet rectangle and placement
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        """
        Bullet movement
        """
        # Update of bullet position
        self.y -= self.speed_factor

        # Update of bullet rect
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Display bullet on screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
