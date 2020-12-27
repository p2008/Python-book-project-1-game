"""
This module contains settings for the application.
"""


class Settings:
    """
    This class stores game settings
    """

    def __init__(self):
        """
        Game settings initialization
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_image = "images/ship.bmp"
        self.ship_speed_factor = 1.5
