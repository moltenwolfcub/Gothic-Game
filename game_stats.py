class GameStats:
    """Track statiscitcs of the game"""

    def __init__(self, gg_game) -> None:
        """Initialize Statistics"""

        self.settings = gg_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Initialize variable statistics"""
        self.score = 0
