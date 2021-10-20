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

        #enemy size
        self.enemy_size = 100
        self.enemy_speed = 5.0
