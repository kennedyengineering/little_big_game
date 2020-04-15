import pygame
from sprite_object import spriteObject

class KidSprite(spriteObject):
    def __init__(self):
        super().__init__("assets/players/kid 16x16.png")

        #scaled_resolution = (32, 32)
        scaled_resolution = (64, 64)


        #self.left_sprites = self.spriteSheet.load_strip((0, 32, 16, 16), 3, colorkey=(255, 255, 255))
        for sprite in self.spriteSheet.load_strip((0, 32, 16, 16), 3, colorkey=(255, 255, 255)):
            self.left_sprites.append(pygame.transform.scale(sprite, scaled_resolution))

        #self.right_sprites = self.spriteSheet.load_strip((0, 48, 16, 16), 3, colorkey=(255, 255, 255))
        for sprite in self.spriteSheet.load_strip((0, 48, 16, 16), 3, colorkey=(255, 255, 255)):
            self.right_sprites.append(pygame.transform.scale(sprite, scaled_resolution))

        #self.up_sprites = self.spriteSheet.load_strip((0, 16, 16, 16), 3, colorkey=(255, 255, 255))
        for sprite in self.spriteSheet.load_strip((0, 16, 16, 16), 3, colorkey=(255, 255, 255)):
            self.up_sprites.append(pygame.transform.scale(sprite, scaled_resolution))

        #self.down_sprites = self.spriteSheet.load_strip((0, 0, 16, 16), 3, colorkey=(255, 255, 255))
        for sprite in self.spriteSheet.load_strip((0, 0, 16, 16), 3, colorkey=(255, 255, 255)):
            self.down_sprites.append(pygame.transform.scale(sprite, scaled_resolution))
