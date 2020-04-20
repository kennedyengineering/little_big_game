import pygame
from sprite_object import spriteObject


class BKSprite(spriteObject):
    def __init__(self):
        super().__init__("assets/players/BK 16x16 sprite.png")

        scaled_resolution = (64, 64)

        for sprite in self.spriteSheet.load_strip((0, 32, 16, 16), 3, colorkey=(255, 255, 255)):
            self.left_sprites.append(pygame.transform.scale(sprite, scaled_resolution))

        for sprite in self.left_sprites:
            self.right_sprites.append(pygame.transform.flip(pygame.transform.scale(sprite, scaled_resolution), 1, 0))

        for sprite in self.spriteSheet.load_strip((0, 16, 16, 16), 3, colorkey=(255, 255, 255)):
            self.up_sprites.append(pygame.transform.scale(sprite, scaled_resolution))

        for sprite in self.spriteSheet.load_strip((0, 0, 16, 16), 3, colorkey=(255, 255, 255)):
            self.down_sprites.append(pygame.transform.scale(sprite, scaled_resolution))
