import pygame
from pygame.sprite import Sprite

class MazeElement(Sprite):
    """A Class to manage the maze"""

    def __init__(self, gg_game, shape):
        """Create the maze"""
        super().__init__()

        self.screen = gg_game.screen

        self.image = pygame.image.load('graphics/maze_image.png')
        self.image = pygame.transform.scale(self.image, (shape[2], shape[3]))
        self.rect = self.image.get_rect()

        self.rect.x = shape[0]
        self.rect.y = shape[1]


    def draw_maze(self):
        """Draw the maze to the screen"""

        # border walls
        pygame.draw.lines(self.screen, self.color, False, [(0,0), (self.settings.screen_width-2, 0), (self.settings.screen_width-2, self.settings.screen_height), (0, self.settings.screen_height), (0, 0)], 5)
