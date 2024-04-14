import pygame
import random

enemy_spawn_x = random.randint(0,320)
enemy_spawn_y = random.randint(0,180)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.spawn_x = enemy_spawn_x
        self.spawn_y = enemy_spawn_y
        pygame.sprite.Sprite.__init__(self)

        enemy_sprite = pygame.image.load("animation/Walk-Cycle_0000_L01.png")
        self.enemy_sprite = pygame.transform.scale(enemy_sprite, (self.width, self.height))
        #base_sprite now represents the loaded image
        self.hitbox = self.enemy_sprite.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)

    def update(self):
        self.screen.blit(self.enemy_sprite, self.hitbox)

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


class player_ani():
    def direction(self, dir):
        if dir == 0:
            self.facing = 0
        if dir == 1:
            self.facing = 1
        self.next_frame(250)
    def next_frame(self, time) -> pygame.Surface:
        self.time += time
        if self.time < 150:
            return self.frame
        if self.current_frame < 3:
            self.current_frame += 1
            if self.facing == 0:
                self.frame = self.left_frames[self.current_frame]
            else:
                self.frame = self.right_frames[self.current_frame]
        else:
            self.current_frame = 0
            if self.facing == 0:
                self.frame = self.left_frames[self.current_frame]
            else:
                self.frame = self.right_frames[self.current_frame]
        self.time = 0
        return self.frame
    
    def __init__(self):
        self.left_frames = [pygame.transform.scale(pygame.image.load('animation/Walk-Cycle_0000_L0' + str(x) + '.png'), (45,60)) for x in range(4)]
        self.right_frames = [pygame.transform.scale(pygame.image.load('animation/Walk-Cycle_0000_R0' + str(x) + '.png'), (45, 60)) for x in range(4)]
        self.frame = self.left_frames[0]
        self.time = 0
        self.facing = 0
        self.current_frame = 0
        self.max_frames = 4


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_x, spawn_y, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

        pygame.sprite.Sprite.__init__(self)

        #initialize its HP at 100 
        self.hp = 100

        #load an image for the sprite
        #player_sprite now represents the loaded image

        self.player_ani = player_ani()

        #HITBOX 
        self.hitbox = self.player_ani.frame.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)

        #variables to control movement
        self.movex=0 
        self.movey=0 
        self.speed=4
        self.time = 0
        self.jump = False
        self.gravity = 0.3
        self.velocity = -10
        self.health = 100

        #ETC

    def update(self, dt):
        if self.jump == True:
            self.time += dt/1000
            self.movey = self.gravity*self.time+self.velocity
            self.velocity += self.gravity

        if self.hitbox.centery > self.spawn_y and self.jump == True:
            self.jump = False
            self.movey = 0
            self.velocity = -10
            self.time = 0
            self.hitbox.centery = self.spawn_y

        self.hitbox.move_ip(self.movex,self.movey)
        
        if(self.movex != 0):
            self.screen.blit(self.player_ani.next_frame(dt), self.hitbox)
        else:
            self.screen.blit(self.player_ani.frame, self.hitbox)





'''
self.hitbox represents the get_rect() of the Player. 
The Player's image is represented by the base_sprite 
The Player itself will move if we move the self.hitbox.

'''