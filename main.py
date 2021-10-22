import pygame, sys

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from text import Text

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

        self.import_images()
        self.make_buttons()

        pygame.display.set_caption("Rat's Revenge")

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.player = Player(self)
        self.item = Item(self)

        self.enemies = pygame.sprite.Group()
        enemy = Enemy(self)
        self.enemies.add(enemy)

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


        self.mouse_down = False

    def import_images(self):

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),pygame.FULLSCREEN)#,pygame.RESIZABLE)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.bacground_filename = "graphics/background.png"
        self.bg_image = pygame.image.load(self.bacground_filename)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.lobby_bacground_filename = "graphics/ui/background.jpg"
        self.lobby_bg_image = pygame.image.load(self.lobby_bacground_filename)
        self.lobby_bg_image = pygame.transform.scale(self.lobby_bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.logo_filename = "graphics/ui/logo.png"
        self.logo_image = pygame.image.load(self.logo_filename)
        self.logo_image = pygame.transform.scale(self.logo_image, (500,500))

    def make_buttons(self):

        self.play_button = Button(self, "Play", (self.settings.screen_width//2, self.settings.screen_height//2 - 100))
        self.stats_button = Button(self, "Statistics",(self.settings.screen_width//2, self.settings.screen_height//2 - 25), (300, 75))
        self.credits_button = Button(self, "Credits", (self.settings.screen_width//2, self.settings.screen_height//2 + 50), (250, 75))
        self.exit_button = Button(self, "Exit", (self.settings.screen_width//2, self.settings.screen_height//2 + 125))
        self.troll_button = Button(self, "Click Here", (self.settings.screen_width- 200,self.settings.screen_height-75), (330, 75))

        self.stats_back_button = Button(self, "Back", (self.settings.screen_width//2-170 ,self.settings.screen_height-75), (200, 75))
        self.stats_reset_button = Button(self, "Reset Statistics", (self.settings.screen_width//2 + 170 ,self.settings.screen_height-75), (480, 75))

        self.reset_confirm_button = Button(self, "Yes", (self.settings.screen_width//2 + 100 ,self.settings.screen_height//2 + 50))
        self.reset_deny_button = Button(self, "No", (self.settings.screen_width//2 - 100 ,self.settings.screen_height//2 + 50))

        self.credits_back_button = Button(self, "Back", (self.settings.screen_width//2, self.settings.screen_height-100), (200, 75))

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
            if self.stats.game_active:
                self.player_hit()
            elif self.stats.in_lobby:
                sys.exit()
            elif self.stats.in_stat_reset_check:
                self.stats.in_stat_reset_check = False
                self.stats.in_stats = True
            else:
                self.stats.in_stats = False
                self.stats.in_credits = False

                self.stats.in_lobby = True

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
                self.exit_game()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False

            #elif event.type == pygame.VIDEORESIZE:
            #    self._resize_screen(event)

    def check_mouse(self):
        mouse_pos = pygame.mouse.get_pos()


        if self.play_button.rect.collidepoint(mouse_pos):
            self.play_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_lobby:
                self.settings.initialize_dynamic_settings()
                self.stats.reset_stats()
                self.stats.game_active = True
                self.scoreboard.prep_score()

                self.enemies.empty()
                enemy = Enemy(self)
                self.enemies.add(enemy)

                self.player.reset_pos()


                pygame.mouse.set_visible(False)

        else:
            self.play_button.alternate_color = False


        if self.credits_button.rect.collidepoint(mouse_pos):
            self.credits_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_lobby:
                self.stats.in_lobby = False
                self.stats.in_credits = True

        else:
            self.credits_button.alternate_color = False

    
        if self.stats_button.rect.collidepoint(mouse_pos):
            self.stats_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_lobby:
                self.stats.in_lobby = False
                self.stats.in_stats = True

        else:
            self.stats_button.alternate_color = False


        if self.exit_button.rect.collidepoint(mouse_pos):
            self.exit_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_lobby:
                self.exit_game()

        else:
            self.exit_button.alternate_color = False


        if self.troll_button.rect.collidepoint(mouse_pos):
            self.troll_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_lobby:
                pass

        else:
            self.troll_button.alternate_color = False




        if self.stats_reset_button.rect.collidepoint(mouse_pos):
            self.stats_reset_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_stats:
                self.stats.in_stats = False
                self.stats.in_stat_reset_check = True

        else:
            self.stats_reset_button.alternate_color = False


        if self.stats_back_button.rect.collidepoint(mouse_pos):
            self.stats_back_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_stats:
                self.stats.in_stats = False
                self.stats.in_lobby = True

        else:
            self.stats_back_button.alternate_color = False



        if self.reset_confirm_button.rect.collidepoint(mouse_pos):
            self.reset_confirm_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_stat_reset_check:
                self.stats.reset_total_stats()

                self.stats.in_stat_reset_check = False
                self.stats.in_stats = True

        else:
            self.reset_confirm_button.alternate_color = False


        if self.reset_deny_button.rect.collidepoint(mouse_pos):
            self.reset_deny_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_stat_reset_check:
                self.stats.in_stat_reset_check = False
                self.stats.in_stats = True

        else:
            self.reset_deny_button.alternate_color = False

        

        if self.credits_back_button.rect.collidepoint(mouse_pos):
            self.credits_back_button.alternate_color = True
            if self.mouse_down and not self.stats.game_active and self.stats.in_credits:
                self.stats.in_credits = False
                self.stats.in_lobby = True

        else:
            self.reset_deny_button.alternate_color = False
            pass

    def _update_screen(self):
        """Update the images on the screen and flip to a new screen."""

        if self.stats.game_active:

            self.screen.blit(self.bg_image, (0, 0))
            self.item.blitme()

            self.maze_elements.draw(self.screen)
            self.enemies.draw(self.screen)
            self.player.blitme()

            self.scoreboard.show_score()

        if not self.stats.game_active:
            self.screen.blit(self.lobby_bg_image, (0, 0))
            self.screen.blit(self.logo_image, (self.settings.screen_width//2-250,-20))

            if self.stats.in_lobby:
                self.play_button.draw_button()
                self.stats_button.draw_button()
                self.credits_button.draw_button()
                self.exit_button.draw_button()
                self.troll_button.draw_button()
            
            elif self.stats.in_stats:

                self.high_score_text = Text(self, "High Score:", (self.settings.screen_width//2 - 400, 400))
                self.high_score_value = Text(self, str(self.stats.high_score), (self.settings.screen_width//2 + 360, 400))

                self.total_items_text = Text(self, "Total items Collected:", (self.settings.screen_width//2 - 400, 475))
                self.total_items_value = Text(self, str(self.stats.total_items_collected), (self.settings.screen_width//2 + 360, 475))


                self.total_items_text.draw_text()
                self.total_items_value.draw_text()

                self.high_score_text.draw_text()
                self.high_score_value.draw_text()


                self.stats_back_button.draw_button()
                self.stats_reset_button.draw_button()

            elif self.stats.in_stat_reset_check:

                self.reset_warining_text = Text(self, "Are you sure that you want to reset all of your statistics?", (self.settings.screen_width//2, 450), True)
                self.reset_warining_text.draw_text()

                self.reset_confirm_button.draw_button()
                self.reset_deny_button.draw_button()
            
            elif self.stats.in_credits:

                self.proggrammer_credt_text = Text(self, "Lead Programmer: Oliver", (self.settings.screen_width//2 ,self.settings.screen_height//2 - 100), True)
                self.artist_credt_text = Text(self, "Lead Artist: Livvy", (self.settings.screen_width//2 ,self.settings.screen_height//2 + 0), True)
                self.music_credt_text = Text(self, "Lead Sound Artist: Bernard", (self.settings.screen_width//2 ,self.settings.screen_height//2 + 100), True)

                self.proggrammer_credt_text.draw_text()
                self.artist_credt_text.draw_text()
                self.music_credt_text.draw_text()

                self.credits_back_button.draw_button()

        
        pygame.display.flip()

    def update_enemies(self):
        """Update the positions of the enemies"""
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player_hit()

    def player_hit(self):
        """Respond to player_enemy collisions"""
        
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def increase_score(self):
        """Increase score"""
        self.stats.total_items_collected += 1

        self.stats.score += self.settings.item_points
        self.scoreboard.prep_score()
        self.scoreboard.check_high_score()

    def exit_game(self):
        sys.exit()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.check_mouse()
            if self.stats.game_active:
                self.update_enemies()
                self.player.update()
                self.item.update()

            self._update_screen()


if __name__=='__main__':
    #make a game instance, and run the game.
    gg = GothicGame()
    gg.run_game()
