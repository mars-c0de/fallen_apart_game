import pygame
import Blocks

screen = pygame.display.set_mode((640,360))
#Number of tiles
TILE_TYPES = 3
img_list = []
TILE_SIZE = int(screen.get_width()/16)
for x in range(TILE_TYPES):
    img = pygame.image.load(f"img/{x}.jpg")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)



def draw_bg():
	screen.fill("blue")
	pygame.draw.line(screen, "red", (0, 300), (800, 300))

class World():
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile == 0:
                        self.obstacle_list.append(tile_data)
                    elif tile == 1:
                        water = Blocks.Water(img, TILE_SIZE, img_rect.x, img_rect.y)
                        damage_group.add(water)
                    elif tile == 2:
                        decoration = Blocks.Decoration(img, TILE_SIZE, img_rect.x, img_rect.y)
                        decoration_group.add(decoration)

    def draw(self):
        for tile in self.obstacle_list:
            screen.blit(tile[0],tile[1])


damage_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()


world_data = [
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
    [1,0,1,0,0],
    [2,2,2,0,0,2,1,0]
]
world = World()
world.process_data(world_data)

run = True

while run:
    draw_bg()
    damage_group.update()
    decoration_group.update()

    damage_group.draw(screen)
    decoration_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()