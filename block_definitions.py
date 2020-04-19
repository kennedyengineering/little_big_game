from block_object import Block
from sprite_object import spritesheet
import pygame


class BlockGrass(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        super().__init__(location, dimensions)

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")
        self.surface = block_spritesheet.image_at([0*16, 8*16, 16, 16])
        self.surface = pygame.transform.scale(self.surface, dimensions)


class BlockDirt(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        super().__init__(location, dimensions)

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")
        self.surface = block_spritesheet.image_at([2*16, 1*16, 16, 16])
        self.surface = pygame.transform.scale(self.surface, dimensions)
