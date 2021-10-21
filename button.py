import pygame

class Button:

    def __init__(self, gg_game, msg, pos = "", size =(200, 75), font_size = 48) -> None:
        """Initialize button attributes"""

        self.msg = msg

        self.settings = gg_game.settings
        self.screen = gg_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = size[0],size[1]
        
        self.other_text_color = self.settings.button_alternate_text_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(None, font_size)

        self.image = pygame.image.load("graphics/ui/button.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        if pos:
            self.rect.center = pos
        else:
            self.rect.center = self.screen_rect.center

        self.prep_msg(self.msg, self.text_color)

    def prep_msg(self, msg, text_color):
        """Turn message into rendered image"""
        self.msg_image = self.font.render(msg, True, text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.y += 5
    
    def draw_button(self):
        self.screen.blit(self.image, self.rect)

        if self.alternate_color:
            self.prep_msg(self.msg, self.other_text_color)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        else:
            self.prep_msg(self.msg, self.text_color)
            self.screen.blit(self.msg_image, self.msg_image_rect)
