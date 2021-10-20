from pygame import font
import pygame

class Button:

    def __init__(self, gg_game, msg, pos = "", size =(200, 50), font_size = 48) -> None:
        """Initialize button attributes"""

        self.settings = gg_game.settings
        self.screen = gg_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = size[0],size[1]
        
        self.button_color = self.settings.button_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(None, font_size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if pos:
            self.rect.center = pos
        else:
            self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn message into rendered image"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
