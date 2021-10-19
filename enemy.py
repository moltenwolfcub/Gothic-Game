import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a singular rat"""

    def __init__(self, gg_game):
        """Initialize the enemy and its starting pos"""
        super().__init__()

        self.gg_game = gg_game
        self.screen = gg_game.screen
        self.settings = gg_game.settings

        self.image = pygame.image.load("graphics/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.settings.enemy_size, self.settings.enemy_size))
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width - self.settings.enemy_size - 10
        self.rect.y = self.settings.screen_height - self.settings.enemy_size - 10

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = "left"
    
    def update(self):
        """Move the enemy"""
        self.image = pygame.image.load("graphics/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.settings.enemy_size, self.settings.enemy_size))

        if self.direction == "left":

            self.image = pygame.transform.rotate(self.image, 0)
            self.image = pygame.transform.flip(self.image, False, False)

            self.x -= self.settings.enemy_speed
            self.rect.x = self.x

        if self.direction == "right":

            self.image = pygame.transform.rotate(self.image, 0)
            self.image = pygame.transform.flip(self.image, True, False)

            self.x += self.settings.enemy_speed
            self.rect.x = self.x

        if self.direction == "up":

            self.image = pygame.transform.rotate(self.image, -90)
            self.image = pygame.transform.flip(self.image, False, False)

            self.y -= self.settings.enemy_speed
            self.rect.y = self.y

        if self.direction == "down":

            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.flip(self.image, False, False)

            self.y += self.settings.enemy_speed
            self.rect.y = self.y
