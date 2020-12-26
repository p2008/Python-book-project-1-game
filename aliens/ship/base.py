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
        self.center = float(self.rect.centerx)

        # Attributes corresponding to ship movement
        self.moving_right = False
        self.moving_left = False
        self.ship_speed_factor = 1.5

    def update(self):
        """
        Update ship placement base on moving attributes
        """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor

        self.rect.centerx = self.center

    def blit_me(self):
        """
        Display ship in his actual position
        """

        self.screen.blit(self.image, self.rect)
