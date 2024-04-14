import pygame
import Blocks
import pygame.freetype
import players, enemy
screen = pygame.display.set_mode((800,600))
TILE_TYPES = 3
img_list = []
TILE_SIZE = 50
for x in range(TILE_TYPES):
    img = pygame.image.load(f"img/{x}.jpg")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

#GAME_FONT = pygame.freetype.Font(None,size=48)

class World():
    def __init__(self):
        self.obstacle_list = []
        self.damage_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()

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
                        self.damage_group.add(water)
                    elif tile == 2:
                        decoration = Blocks.Decoration(img, TILE_SIZE, img_rect.x, img_rect.y)
                        self.decoration_group.add(decoration)

    def draw(self):
        for tile in self.obstacle_list:
            screen.blit(tile[0],tile[1])
        self.damage_group.update()
        self.decoration_group.update()
        self.damage_group.draw(screen)
        self.decoration_group.draw(screen)
