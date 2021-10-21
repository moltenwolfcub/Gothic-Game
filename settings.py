class Settings:
    """A class to store the game's settings."""

    def __init__(self):
        """Initialize the game's static settings."""

        #screen settings
        self.screen_width = 1920
        self.screen_height = 1080

        #player settings
        self.player_speed = 5.0
        self.player_size = 75

        #item settings
        self.item_size = 80

        #enemy settings
        self.enemy_size = 100

        #button settings
        self.button_alternate_text_color =  (0, 125, 0)
        self.button_text_color = (255, 255, 255)

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout"""

        self.enemy_speed = 5.0
        self.item_points = 10
    
    def increase_speed(self):
        """Increase dynamic settings"""
        self.enemy_speed *= self.speedup_scale

        self.item_points = int(self.item_points * self.score_scale)
