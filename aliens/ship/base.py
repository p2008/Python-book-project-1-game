import pygame


class BaseShip:
    """
    Base class for ships
    """

    def __init__(self, screen, image="images/ship.bmp"):
        """
        Initialization of spaceship and its start placement.
        """
        self.screen = screen

        # Set spaceship image and its rectangle
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # New ships will be shown on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_me(self):
        """
        Display ship in his actual position
        """

        self.screen.blit(self.image, self.rect)
