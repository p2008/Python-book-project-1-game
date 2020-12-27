import pygame


class BaseShip:
    """
    Base class for ships
    """

    def __init__(self, ai_settings, screen, image=None):
        """
        Initialization of spaceship and its start placement.
        :param ai_settings: An instance of the Settings class.
        :param screen: App screen object.
        :param image: A path to ship image (bmp).

        """
        self.screen = screen

        # Set spaceship image and its rectangle
        self.image = pygame.image.load(image or ai_settings.ship_image)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # New ships will be shown on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Attributes corresponding to ship movement
        self.moving_right = False
        self.moving_left = False
        self.speed_factor = ai_settings.ship_speed_factor

    def update(self):
        """
        Update ship placement base on moving attributes
        """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed_factor

        self.rect.centerx = self.center

    def blit_me(self):
        """
        Display ship in his actual position
        """

        self.screen.blit(self.image, self.rect)
