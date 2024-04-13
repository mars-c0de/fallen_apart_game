import pygame
class NPC(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, width, height):
        self.width = width
        self.height = height
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        pygame.sprite.Sprite.__init__(self)
        base_sprite = pygame.image.load("image/fixed_base_sprite_facing_screen.png")
        self.scale_sprite = pygame.transform.scale(base_sprite, self.width, self.height)
        self.hitbox = self.scale_sprite.get_rect()
        self.hitbox.center = (self.spawn_x, self.spawn_y)
    def get_sprite():
        return 