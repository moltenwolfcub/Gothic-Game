class GameStats:
    """Track statiscitcs of the game"""

    def __init__(self, gg_game) -> None:
        """Initialize Statistics"""

        self.settings = gg_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Initialize variable statistics"""
        self.health = self.settings.max_health
        self.score = 0
