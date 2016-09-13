class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (20, 0, 105)

        # Ship settings
        self.ship_speed_factor = 10

        # Bullet settings
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
