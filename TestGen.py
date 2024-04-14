import pygame
import Blocks
import sprites
import World
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((800,600))
#Number of tiles
# TILE_TYPES = 3
# img_list = []
# TILE_SIZE = int(screen.get_width()/16)
# for x in range(TILE_TYPES):
#     img = pygame.image.load(f"img/{x}.jpg")
#     img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
#     img_list.append(img)

GAME_FONT = pygame.freetype.Font(None,size=48)

# def draw_bg():
# 	screen.fill("blue")
# 	pygame.draw.line(screen, "red", (0, 300), (800, 300))

# class World():
#     def __init__(self):
#         self.obstacle_list = []

#     def process_data(self, data):
#         for y, row in enumerate(data):
#             for x, tile in enumerate(row):
#                 if tile >= 0:
#                     img = img_list[tile]
#                     img_rect = img.get_rect()
#                     img_rect.x = x * TILE_SIZE
#                     img_rect.y = y * TILE_SIZE
#                     tile_data = (img, img_rect)
#                     if tile == 0:
#                         self.obstacle_list.append(tile_data)
#                     elif tile == 1:
#                         water = Blocks.Water(img, TILE_SIZE, img_rect.x, img_rect.y)
#                         damage_group.add(water)
#                     elif tile == 2:
#                         decoration = Blocks.Decoration(img, TILE_SIZE, img_rect.x, img_rect.y)
#                         decoration_group.add(decoration)

#     def draw(self):
#         for tile in self.obstacle_list:
#             screen.blit(tile[0],tile[1])


# damage_group = pygame.sprite.Group()
# decoration_group = pygame.sprite.Group()


# world_data = [
#     [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
#     [1,0,1,0,0],
#     [2,2,2,0,0,2,1,0],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#     #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# ]
# world = World()
# world.process_data(world_data)

player = sprites.Player(screen, 500,500, 45, 60)
clock = pygame.time.Clock()



run = True


while run:
    dt = clock.tick(60)
    
    screen.fill("blue")
    
    
    player.update(dt)
    World.draw_bg()
    World.world.draw()
    World.damage_group.update()
    World.decoration_group.update()
    player.update(dt)
    World.damage_group.draw(screen)
    World.decoration_group.draw(screen)
    
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
        
        #Check Collisions
        for tile in World.world.obstacle_list:
            #check collision in x direction
            if tile[1].colliderect(player.hitbox.x + player.movex * player.speed, player.hitbox.y, player.width, player.height):
                #print("collison")
                player.movex = 0
            #collision in y direction
            #if tile[1].colliderect(player.hitbox.x , player.hitbox.y + player.movey, player.width, player.height):
                #Check if under or above by checking y velocity??
                #If below ground
                #player.movey = tile[1].bottom - player.hitbox.top
                #If above ground
                #player.movey = tile[1].top - player.rect.bottom
                #player.inair = False 
    pygame.display.update()

pygame.quit()