class GameStats:
    """Track statiscitcs of the game"""

    def __init__(self, gg_game) -> None:
        """Initialize Statistics"""

        self.settings = gg_game.settings
        self.reset_stats()

        self.game_active = False
        self.in_lobby = True
        self.in_stats = False
        self.in_stat_reset_check = False

        self.high_score = 0

        self.total_items_collected = 0

    def reset_total_stats(self):
        """Reset the statistics stored cross game"""
        self.total_items_collected = 0

    def reset_stats(self):
        """Initialize variable statistics"""
        self.score = 0
