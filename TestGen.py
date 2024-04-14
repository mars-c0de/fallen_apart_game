import pygame
import Blocks
from players import Player
from enemy import Enemy
import World
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((800,600))

GAME_FONT = pygame.freetype.Font(None,size=48)


world_data = [
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
    [1,0,1,0,0],
    [2,2,2,0,0,2,1,0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0,0,0,0,0],
    [0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world = World.World()
world.process_data(world_data)
play = Player(screen, 500,500, 45, 60)
clock = pygame.time.Clock()

en = Enemy(screen, 45, 60)

run = True


while run:
    dt = clock.tick(60)
    
    screen.fill("blue")
    
    world.draw()
    
    GAME_FONT.render_to(screen, (0, 0), str(play.health), (255, 0, 0))

    #Event Handler
    for tile in world.obstacle_list:
            #check collision in x direction
            if tile[1].collidepoint(play.hitbox.midtop[0],play.hitbox.midtop[1]):
                play.hitbox.y = tile[1].midbottom[1]
                play.collisionyu = True
                play.velocity = 0
                play.movey = 0
            elif tile[1].collidepoint(play.hitbox.midleft[0],play.hitbox.midleft[1]):
                play.hitbox.x = tile[1].midright[0]
                play.collisionxl = True
                play.movex = 0
            elif tile[1].collidepoint(play.hitbox.midright[0],play.hitbox.midright[1]):
                play.hitbox.x = tile[1].midleft[0]
                play.collisionxr = True
                play.movex = 0
            else:
                play.collisionxr = False
                play.collisionxl = False
                play.collisionyu = False
            if tile[1].collidepoint(play.hitbox.midbottom[0],play.hitbox.midbottom[1]):
                play.hitbox.bottom = tile[1].midtop[1]+0.1
                play.jump = False
                play.collisionyd = True
                play.movey = 0
            else:
                play.collisionyd = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                play.player_ani.direction(0)
                if not play.collisionxl:
                    play.movex = -1 * play.speed
            if event.key == pygame.K_d:
                play.player_ani.direction(1)
                if not play.collisionxr:
                    play.movex = 1 * play.speed
            if event.key == pygame.K_SPACE:
                play.jump = True
                if play.health == 10:
                    play.health = 'Dead'
                elif type(play.health) == int:
                    play.health -=10
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                play.movex = 0
            if event.key == pygame.K_d:
                play.movex = 0
    play.update(dt)
    en.update()
    pygame.display.update()

pygame.quit()