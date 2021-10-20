import pygame
import random

class Item:
    """A class to represent a single star."""

    def __init__(self, gg_game):

        self.gg_game = gg_game
        self.screen = gg_game.screen
        self.settings = gg_game.settings

        self.image = pygame.image.load("graphics/item.png")
        self.image = pygame.transform.scale(self.image, (self.settings.item_size, self.settings.item_size))
        self.rect = self.image.get_rect()

        self.move()

    def blitme(self):
        """Show the item."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Check if touching player"""
        if self.rect.colliderect(self.gg_game.player.rect):
            self.gg_game.increase_score()
            self.move()
    
    def move(self):
        self.rect.x = random.randint(10, self.settings.screen_width-self.rect.width - 10)
        self.rect.y = random.randint(10, self.settings.screen_height-self.rect.height - 10)
