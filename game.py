import pygame
import sprites

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * .75)
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fallen Apart")

#Player
player = sprites.Player(screen, 500,500, 45, 60)
# player_start_x = 200
# player_start_y = 200

#player.test()

clock = pygame.time.Clock()


run = True
while run:
    dt = clock.tick(60)
    screen.fill("blue")
    player.update(dt)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.player_ani.direction(0)
                player.movex = -1 * player.speed
            if event.key == pygame.K_d:
                player.player_ani.direction(1)
                player.movex = 1 * player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.movex = 0
            if event.key == pygame.K_d:
                player.movex = 0


    pygame.display.update()