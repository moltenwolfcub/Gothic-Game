import pygame

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, gg_game) -> None:
        """Initialize scorekeeping attributes"""

        self.screen = gg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gg_game.settings
        self.stats = gg_game.stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.top = 20

    def check_high_score(self):
        """Check if ther's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit (self.score_image, self.score_rect)
        self.screen.blit (self.high_score_image, self.high_score_rect)
