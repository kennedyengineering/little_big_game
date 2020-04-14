from sprite_object import spriteObject

class KidSprite(spriteObject):
    def __init__(self):
        super().__init__("assets/players/kid 16x16.png")

        self.left_sprites = self.spriteSheet.load_strip((0, 32, 16, 16), 3, colorkey=(255, 255, 255))
        self.right_sprites = self.spriteSheet.load_strip((0, 48, 16, 16), 3, colorkey=(255, 255, 255))
        self.up_sprites = self.spriteSheet.load_strip((0, 16, 16, 16), 3, colorkey=(255, 255, 255))
        self.down_sprites = self.spriteSheet.load_strip((0, 0, 16, 16), 3, colorkey=(255, 255, 255))
