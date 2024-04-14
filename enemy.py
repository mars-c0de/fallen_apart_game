import pygame
import random

enemy_spawn_x = random.randint(0,320)
enemy_spawn_y = random.randint(0,180)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.spawn_x = 400
        self.spawn_y = 500
        pygame.sprite.Sprite.__init__(self)
        enemy_sprite2 = pygame.image.load("animation/Walk-Cycle_0000_L01.png")
        self.enemy_sprite2 = pygame.transform.scale(enemy_sprite2, (self.width, self.height))
        #base_sprite now represents the loaded image
        self.hitbox = self.enemy_sprite2.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)

    def update(self):
        self.screen.blit(self.enemy_sprite, self.hitbox)
