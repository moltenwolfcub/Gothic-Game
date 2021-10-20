import pygame, random, sys
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a singular rat"""

    def __init__(self, gg_game, start_pos = ""):
        """Initialize the enemy and its starting pos"""
        super().__init__()

        self.gg_game = gg_game
        self.screen = gg_game.screen
        self.settings = gg_game.settings

        self.image = pygame.image.load("graphics/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.settings.enemy_size, self.settings.enemy_size))
        self.rect = self.image.get_rect()

        self.collision_rect = self.image.get_rect()

        if not start_pos:
            self.rect.x = self.settings.screen_width - self.settings.enemy_size - 10
            self.rect.y = self.settings.screen_height - self.settings.enemy_size - 10
        
        elif start_pos:
            self.rect.x = start_pos[0]
            self.rect.y = start_pos[1]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = "left"
    
    def update(self):
        """Move the enemy"""
        if not self.check_edges():
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
        
        else:
            self.change_direction()
        

        if random.randint(1, 10000) == 1:

            enemy = Enemy(self.gg_game, (self.rect.x, self.rect.y))
            self.gg_game.enemies.add(enemy)

    def change_direction(self):
        """1/3 chance of turning left ,right or turning back"""
        if self.direction == "right":
            value = random.choice([0, 2])
            if value == 0:
                self.direction = "up"
            elif value == 1:
                self.direction = "down"
            elif value == 2:
                self.direction = "left"
            else:
                print("Programmer error \n exiting...")
                sys.exit()

        elif self.direction == "left":
            value = random.choice([0, 2])
            if value == 0:
                self.direction = "down"
            elif value == 1:
                self.direction = "up"
            elif value == 2:
                self.direction = "right"
            else:
                print("Programmer error \n exiting...")
                sys.exit()

        elif self.direction == "up":
            value = random.choice([0, 2])
            if value == 0:
                self.direction = "left"
            elif value == 1:
                self.direction = "right"
            elif value == 2:
                self.direction = "down"
            else:
                print("Programmer error \n exiting...")
                sys.exit()
                
        elif self.direction == "down":
            value = random.choice([0, 2])
            if value == 0:
                self.direction = "right"
            elif value == 1:
                self.direction = "left"
            elif value == 2:
                self.direction = "up"
            else:
                print("Programmer error \n exiting...")
                sys.exit()
                

    def check_edges(self) -> bool:
        """Return True if enemy is at the edge of the screen or hitting a wall"""
        screen_rect = self.screen.get_rect()

        self.collision_rect.center = self.rect.center 

        if self.direction == "right":
            self.collision_rect.x += self.settings.enemy_speed

            if self.collision_rect.right > screen_rect.right:
                return True

            for line_rect in self.gg_game.maze_elements:
                if line_rect.rect.colliderect(self.collision_rect):
                    return True
        
        elif self.direction == "left":
            self.collision_rect.x -= self.settings.enemy_speed

            if self.collision_rect.left < 0:
                return True

            for line_rect in self.gg_game.maze_elements:
                if line_rect.rect.colliderect(self.collision_rect):
                    return True
        
        elif self.direction == "up":
            self.collision_rect.y -= self.settings.enemy_speed

            if self.collision_rect.top < 0:
                return True

            for line_rect in self.gg_game.maze_elements:
                if line_rect.rect.colliderect(self.collision_rect):
                    return True
        
        elif self.direction == "down":
            self.collision_rect.y += self.settings.enemy_speed

            if self.collision_rect.top > screen_rect.top:
                return True

            for line_rect in self.gg_game.maze_elements:
                if line_rect.rect.colliderect(self.collision_rect):
                    return True
