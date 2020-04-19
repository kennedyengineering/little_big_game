from block_object import Block
from sprite_object import spritesheet


class BlockGrass(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([0*16, 8*16, 16, 16]))


class BlockDirt(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([2*16, 1*16, 16, 16]))


class BlockStone(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([6*16, 1*16, 16, 16]))


class BlockDoor(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([2*16, 6*16, 16, 16]))

    def action(self, block):
        print("door activated", self)
