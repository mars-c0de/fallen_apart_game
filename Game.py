import pygame
import NPC

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * .75)
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 60


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fallen Apart")


#Player
player = NPC.NPC(screen, 200,200, 45, 60)
# player_start_x = 200
# player_start_y = 200
# base_sprite = pygame.image.load("img/fixed_base_sprite_facing_screen.png")
# #Downscale Image 
# player_sprite = pygame.transform.scale(base_sprite, (PLAYER_WIDTH, PLAYER_HEIGHT))
# #Creates a hitbox
# player_hitbox = player_sprite.get_rect()
# #Spawn location
# player_hitbox.center = (player_start_x, player_start_y)


run = True
while run:
    screen.fill("blue")
    
    player.draw()

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()