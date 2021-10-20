import pygame, sys, random

from settings import Settings
from player import Player
from maze import MazeElement
from item import Item
from enemy import Enemy

class GothicGame:
    """Overall class to manage game assets and behaviour"""

    def __init__(self) -> None:
        """Initialize the game and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),pygame.FULLSCREEN)#,pygame.RESIZABLE)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.bacground_filename = "graphics/background.png"
        self.bg_image = pygame.image.load(self.bacground_filename)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Rat's Revenge")

        self.player = Player(self)
        self.item = Item(self)
        self.maze_elements = pygame.sprite.Group()

        self.maze_line_shapes = [
            (110, 110, 500, 10),
            (110, 110, 10, 400),
            (110, 620, 10, 240),
            (0, 620, 110, 10),
            (110, 960, 500, 10),
            (720, 960, 10, 120),
            (600, 330, 10, 630),
            (450, 110, 10, 680),
            (270, 280, 10, 680),
            (600, 330, 500, 10),
            (720, 450, 250, 10),
            (720, 450, 10, 350),
            (1100, 330, 10, 140),
            (720, 0, 10, 210),
            (850, 110, 10, 100),
            (850, 210, 260, 10),
            (970, 0, 10, 110),
            (970, 110, 140, 10),
            (1230, 110, 570, 10),
            (1230, 110, 10, 365),
            (1370, 230, 700, 10)
        ]

        self.create_maze()

        self.enemies = pygame.sprite.Group()

        enemy = Enemy(self)
        self.enemies.add(enemy)


    def create_maze(self):
        """Draw the maze rects"""
        for shape in self.maze_line_shapes:
            element = MazeElement(self, shape)
            self.maze_elements.add(element)

    def _resize_screen(self, event): # doesn't works so unused
        """Update elements when screen is resized resized"""
        #old_screen_size = (self.settings.screen_width, self.settings.screen_height)

        #self.screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)

        ## background image

        #self.screen.blit(pygame.transform.scale(self.bg_image, event.dict['size']), (0, 0))

        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        #self.player.resize_window(event, old_screen_size)
            
    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = True

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.player.moving_down = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.player.moving_up = False

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            #elif event.type == pygame.VIDEORESIZE:
            #    self._resize_screen(event)

    def _update_screen(self):
        """Update the images on the screen and flip to a new screen."""

        self.screen.blit(self.bg_image, (0, 0))
        self.player.blitme()
        self.item.blitme()

        self.maze_elements.draw(self.screen)
        self.enemies.draw(self.screen)
        
        pygame.display.flip()

    def update_enemies(self):
        """Update the positions of the enemies and possibly duplicate"""
        self.enemies.update()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.update_enemies()
            self.player.update()
            self.item.update()

            self._update_screen()


if __name__=='__main__':
    #make a game instance, and run the game.
    gg = GothicGame()
    gg.run_game()
