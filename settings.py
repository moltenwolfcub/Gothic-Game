class Settings:
    """A class to store the game's settings."""

    def __init__(self):
        """Initialize the games settings."""

        #screen settings
        self.screen_width = 0
        self.screen_height = 0

        #player settings
        self.player_speed = 5.0
        self.player_size = 75
        self.max_health = 100

        #item settings
        self.item_size = 80

        #enemy settings
        self.enemy_size = 100
        self.enemy_speed = 5.0

        #button settings
        self.button_color = (255, 0, 0)
        self.button_text_color = (255, 255, 255)
