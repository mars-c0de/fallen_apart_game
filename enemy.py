import pygame
import random
import players

enemy_spawn_x = random.randint(0,320)
enemy_spawn_y = random.randint(0,180)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.spawn_x = 400
        self.spawn_y = 500
        pygame.sprite.Sprite.__init__(self)
        enemy_sprite2 = pygame.image.load("img/Enemy.png")
        self.enemy_sprite2 = pygame.transform.scale(enemy_sprite2, (self.width, self.height))
        #transform it to the width & height

        #base_sprite now represents the loaded image
        self.hitbox = self.enemy_sprite2.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)

        #copy the hitbox twice to make rangebox & sensorbox
        self.rangebox = self.hitbox.copy()
        self.sensorbox = self.hitbox.copy()

        #set the center coords of both the rangebox & sensorbox to line up with hitbox, then make the width & height
        #sensorbox width is bigger than rangebox because the enemy needs to sense you over a wider distance 
        self.rangebox.width *= 2
        self.rangebox.height *= 2
        self.rangebox.centerx = self.hitbox.centerx 
        self.rangebox.centery = self.hitbox.centery

        self.sensorbox.width *= 9
        self.sensorbox.height *= 7
        self.sensorbox.centerx = self.hitbox.centerx
        self.sensorbox.centery = self.hitbox.centery

        #player hp
        self.hp = 100

        self.movex = 0
        self.movey = 0
        self.speed = 2

    def take_damage(self):
        self.hp -= 10
        #take_damage() for enemy is called when you hit j on keyboard in TestGen.py

    def attack(self):
        pass
                
    def update(self):
        if self.hp > 0:
            self.screen.blit(self.enemy_sprite2, self.hitbox)
        elif self.hp <= 0:
            pass
        #blit takes inputs of which image & coordinates to use

    