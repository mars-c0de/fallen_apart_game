import pygame
import Blocks
from players import Player
from enemy import Enemy
import World
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((800,600))

GAME_FONT = pygame.freetype.Font(None,size=48)
#creates an instance of Font from pygame.freetype module


#0 = minecraft grass, 1 = water, 2 = blades of grass

world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world = World.World()
world.process_data(world_data)
#world: 
play = Player(screen, 500,500, 45, 60)
#play: instance of player class. 500 & 500 is spawnx and spawny, 45x60 is widthxheight
clock = pygame.time.Clock()
#clock: a clock

en = Enemy(screen, 45, 60)
#en: enemy with height 45, 60

run = True


while run:
    dt = clock.tick(60)
    #stores the time since the last time clock.tick() was called
    
    screen.fill("blue")
    #each time we run, we empty the screen with "fill",  then run the draw() method of class instance World()
    world.draw(play.movex, dt)
    #the draw method runs the update() method (empty) and .draw() method of 2 sprite groups: damage_group and decoration_group
    #see world for more info
    
    GAME_FONT.render_to(screen, (0, 0), str(play.health), (255, 0, 0))
    #runs the render_to() method on an instance of Font defined earlier.
    #takes inputs: surface to draw on, destination coordinates, the player's health in string form, and text color

    #this moves the player
    #within updates, player_ani() is run, which is why .update() takes dt as an argument


    #this just blits the enemy onscreen at its hitbox coords

    #Event Handler
    for tile in world.obstacle_list:
            #check collision in x direction
            if tile[1].collidepoint(play.hitbox.midtop[0],play.hitbox.midtop[1]):
                play.hitbox.y = tile[1].midbottom[1]
                play.collisionyu = True
                play.velocity = 0
                play.movey = 0
                break
            elif tile[1].collidepoint(play.hitbox.midleft[0],play.hitbox.midleft[1]):
                play.hitbox.x = tile[1].midright[0]
                play.collisionxl = True
                play.movex = 2
                break
            elif tile[1].collidepoint(play.hitbox.midright[0],play.hitbox.midright[1]):
                play.hitbox.x = tile[1].midleft[0] - play.hitbox.width
                play.collisionxr = True
                play.movex = 2
                break
            elif tile[1].collidepoint(play.hitbox.midbottom[0],play.hitbox.midbottom[1]):
                play.hitbox.y = tile[1].midtop[1] - play.hitbox.height
                play.jump = False
                play.collisionyd = True
                play.time = 0
                play.velocity = 0
                play.movey = 0
                break
            else:
                if not tile[1].collidepoint(play.hitbox.midbottom[0],play.hitbox.midbottom[1]+0.25):
                    play.collisionyd = False
                else:
                    play.collisionyd = True
                play.collisionxr = False
                play.collisionxl = False
                play.collisionyu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                play.player_ani.direction(0)
                if not play.collisionxl:
                    play.movex = 1
            if event.key == pygame.K_d:
                play.player_ani.direction(1)
                if not play.collisionxr:
                    play.movex = -1
            if event.key == pygame.K_SPACE:
                if play.collisionyd == True:
                    play.velocity = -10
                    play.jump = True
                if play.health == 10:
                    play.health = 'Dead'
                elif type(play.health) == int:
                    play.health -=10
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                play.movex = 2
            if event.key == pygame.K_d:
                play.movex = 2
    play.update(dt)
    en.update()
    pygame.display.update()

pygame.quit()