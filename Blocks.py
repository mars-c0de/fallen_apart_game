#File with different block types and behaviors
import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, img, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.TILE_SIZE = int(size)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + self.TILE_SIZE // 2, y + (self.TILE_SIZE - self.image.get_height()))
    
class Tile(Block):
    pass

class Water(Block):
    pass

class Decoration(Block):
    pass