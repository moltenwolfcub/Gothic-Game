import pygame

class Text:

    def __init__(self, gg_game, text, pos, centered = False) -> None:
        """Initialize button attributes"""

        self.gg_game = gg_game
        self.screen = self.gg_game.screen

        self.text = text
        self.pos = pos
        self.centered = centered
        
        self.text_color = self.gg_game.settings.stats_text_color
        self.font = pygame.font.SysFont(None, 48)

        self.prep_text()
    
    def prep_text(self):
        """Prepare the text"""
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        if self.centered:
            self.text_image_rect.center = self.pos
        else:
            self.text_image_rect.x, self.text_image_rect.y = self.pos[0], self.pos[1]
    
    def draw_text(self):
        """Draw the Text to the screen"""
        self.screen.blit(self.text_image, self.text_image_rect)
