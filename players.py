import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, spawn_x, spawn_y, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

        pygame.sprite.Sprite.__init__(self)

        #initialize its HP at 100 
        self.hp = 200

        #load an image for the sprite
        #player_sprite now represents the loaded image

        self.player_ani = player_ani()

        #HITBOX 
        self.hitbox = self.player_ani.frame.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)

        #make a rangebox for the player just as we did with the enemy
        #we don't need a sensorbox since the player doesn't sense the enemy & move towards it 
        self.rangebox = self.hitbox.copy()
        self.rangebox.width *= 2
        self.rangebox.height *= 2
        self.rangebox.centerx = self.hitbox.centerx
        self.rangebox.centery = self.hitbox.centery

        #variables to control movement
        self.movex=0 
        self.movey=0 
        self.speed=4
        self.time = 0
        self.jump = False
        self.gravity = 0.3
        self.velocity = 0
        self.collisionxl = False
        self.collisionyu = False
        self.collisionxr = False
        self.collisionyd = False

        #ETC

    def take_damage(self):
        self.hp = 0

    def update(self, dt):
        # if self.collisionyd == True:
        #     self.jump = Falsex``
        #     self.velocity = -10
        #     self.time = 0

        # print(self.jump)
        # print(self.collisionyd)
        # print(self.velocity)

        #if the hp is dead, then it just stops updating it
        if self.hp <= 0:
            self.hp = 0
            #set self.hp = 0 so the number in the top left won't be negative 
            pass

        if self.hp > 0:
            if self.jump == True or self.collisionyd == False:
                self.time += dt/1000
                self.movey = self.gravity*self.time+self.velocity
                self.velocity += self.gravity
            if self.hitbox.y > self.spawn_y:
                self.jump = False
                self.movey = 0
                self.velocity = 0
                self.time = 0
                self.hitbox.centery = self.spawn_y
                self.spawn_y = self.hitbox.centery
                self.collisionyd = True

            self.hitbox.move_ip(self.movex,self.movey)
            self.rangebox.move_ip(self.movex,self.movey)
            #move the rangebox in the same way 
            
            if(self.movex != 0):
                self.screen.blit(self.player_ani.next_frame(dt), self.hitbox)
            else:
                self.screen.blit(self.player_ani.frame, self.hitbox)
            

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

