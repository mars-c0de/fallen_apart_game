import pygame
import sprites
import pygame.freetype

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = (SCREEN_WIDTH)*0.75
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 40


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fallen Apart")

#Player
player = sprites.Player(screen, 500,500, 45, 60)
enemy = sprites.Enemy(screen,45,60)
enemy2 = sprites.Enemy2(screen,45,60)
# player_start_x = 200
# player_start_y = 200

#player.test() 

clock = pygame.time.Clock()
GAME_FONT = pygame.freetype.Font(None,size=48)

run = True
while run:
    dt = clock.tick(60)
    screen.fill("blue")
    player.update(dt)
    enemy.update()
    enemy2.update()

    GAME_FONT.render_to(screen, (0, 0), str(player.health), (255, 0, 0))

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
            if event.key == pygame.K_SPACE:
                player.jump = True
                if player.health == 10:
                    player.health = 'Dead'
                elif type(player.health) == int:
                    player.health -=10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                player.movex = 0
            if event.key == pygame.K_d:
                player.movex = 0

    pygame.display.update()