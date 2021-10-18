import pygame

class Player:
    """A class to manage the player."""

    def __init__(self, gg_game) -> None:
        """Initialize the player and set their starting pos"""

        self.gg_game = gg_game

        self.screen = gg_game.screen
        self.settings = gg_game.settings
        
        self.screen_rect = gg_game.screen.get_rect()

        self.image = pygame.image.load ("graphics/player.png")
        self.image = pygame.transform.scale(self.image, (self.settings.player_size, self.settings.player_size))
        self.rect = self.image.get_rect()

        self.rect.topleft = self.screen_rect.topleft
        self.rect.x += 10
        self.rect.y += 10

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.last_moved_direction = "up"

    def update(self):
        """Update the ship's position based on the movement flags"""

        if self.moving_right and self.rect.right < self.screen_rect.right:

            self.last_moved_direction = "right"

            if not pygame.sprite.spritecollideany(self, self.gg_game.maze_elements):
                self.x += self.settings.player_speed
            else:
                self.x -= self.settings.player_speed

        if self.moving_left and self.rect.left > 0:

            self.last_moved_direction = "left"

            if not pygame.sprite.spritecollideany(self, self.gg_game.maze_elements):
                self.x -= self.settings.player_speed
            else:
                self.x += self.settings.player_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:

            self.last_moved_direction = "down"

            if not pygame.sprite.spritecollideany(self, self.gg_game.maze_elements):
                self.y += self.settings.player_speed
            else:
                self.y -= self.settings.player_speed

        if self.moving_up and self.rect.top > 0:

            self.last_moved_direction = "up"

            if not pygame.sprite.spritecollideany(self, self.gg_game.maze_elements):
                self.y -= self.settings.player_speed
            else:
                self.y += self.settings.player_speed
        
        if pygame.sprite.spritecollideany(self, self.gg_game.maze_elements):
            if self.last_moved_direction == "up":
                self.y += self.settings.player_speed
            elif self.last_moved_direction == "down":
                self.y -= self.settings.player_speed
            elif self.last_moved_direction == "left":
                self.x += self.settings.player_speed
            elif self.last_moved_direction == "right":
                self.x -= self.settings.player_speed
        
        if self.x < 0:
            self.x = 0
        if self.y > self.settings.screen_height - 75:
            self.y = self.settings.screen_height - 75

        
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def resize_window(self, event, old_screen_size): # dosen't work so unused
        """Moves image to compensate resizing the window"""
        center_pos = (self.rect.x, self.rect.y)
        self.rect.width += 10
        self.rect.height += 10

        self.image = pygame.transform.scale(self.image, self.rect.size)
        print("Resizing", self.rect.size, (old_screen_size[0]/self.screen.get_rect().width, old_screen_size[1]/self.screen.get_rect().height))
