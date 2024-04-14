import pygame
import Blocks
import pygame.freetype
import players, enemy
screen = pygame.display.set_mode((800,600))
TILE_TYPES = 7
img_list = []
TILE_SIZE = 50
for x in range(TILE_TYPES):
    img = pygame.image.load(f"img/Tiles_000{x+1}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
    #each tile is named 0, 1, or 2
    #here, we load image 1, then size it down, then add it. 2 is added next, then 3. 
    #resulting list: [image 1, image 2, image 3]

#GAME_FONT = pygame.freetype.Font(None,size=48)

class World():
    def __init__(self):
        self.obstacle_list = []
        self.damage_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()

    #data is world_data as passed in TestGen-- basically a list of nested lists 
    def process_data(self, data):
        for y, row in enumerate(data):
            #y is just the number row it's on (1st, 2nd, 3rd...)
            #row represents the entire nested list AKA row 
            for x, tile in enumerate(row):
                #x represents which position in the row it is, tile represents the actual value of that item
                if tile >= 0 and tile != 3:
                    img = img_list[tile]
                    #acceess the image corresponding to index tile, as defined above
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    #img_rect.x retrieves the x coord of the top left corner, we then multiply by tilesize to place in correct spot
                    #we place these tiles in the right spot with the conditionals below
                    tile_data = [img, img_rect, -100]
                    #for each item in the row, make a tuple with the image & its coordinates

                    if tile >= 0:
                        self.obstacle_list.append(tile_data)
                        #if the value is 0, add that tuple to obstacle_list
                    elif tile == 1:
                        water = Blocks.Water(img, TILE_SIZE, img_rect.x, img_rect.y)
                        self.damage_group.add(water)
                        #if the value is 1, create a Water() at the given position & add to sprite group
                    elif tile == 2:
                        decoration = Blocks.Decoration(img, TILE_SIZE, img_rect.x, img_rect.y)
                        self.decoration_group.add(decoration)
                        #if the value is 2, create a Decoration() at the given position & add to sprite group


    def draw(self, move, dt):
        #print(self.obstacle_list[0][1].x)
        if move == 1 and self.obstacle_list[0][1].x < 450:
            dx = 5
            for sprite in self.damage_group:
                if sprite.rect.x < 0 and sprite.rect.x + dx > 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for sprite in self.decoration_group:
                if sprite.rect.x < 0 and sprite.rect.x + dx > 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for tile in self.obstacle_list:
                if tile[1].x < 0 and tile[1].x + dx > 0:
                    tile[1].x = 0
                tile[1].x += dx
        if move == -1:
            dx = -5
            for sprite in self.damage_group:
                if sprite.rect.x > 0 and sprite.rect.x + dx < 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for sprite in self.decoration_group:
                if sprite.rect.x > 0 and sprite.rect.x + dx < 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for tile in self.obstacle_list:
                if tile[1].x > 0 and tile[1].x + dx < 0:
                    tile[1].x = 0
                tile[1].x += dx
        for tile in self.obstacle_list:
            screen.blit(tile[0],tile[1])
        self.damage_group.update()
        self.decoration_group.update()
        self.damage_group.draw(screen)
        self.decoration_group.draw(screen)
