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


class BlockDoor(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([2*16, 6*16, 16, 16]))


class BlockStone(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([6*16, 1*16, 16, 16]))


def construct_stone_house(object_list, location, dimensions=[16, 16]):
    object_list.append(BlockStone([location[0]+dimensions[0]*0, location[1]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*1, location[1]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*2, location[1]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*3, location[1]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*4, location[1]], dimensions))

    object_list.append(BlockStone([location[0]+dimensions[0]*0, location[1] + dimensions[0]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*1, location[1] + dimensions[0]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*2, location[1] + dimensions[0]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*3, location[1] + dimensions[0]], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*4, location[1] + dimensions[0]], dimensions))

    object_list.append(BlockStone([location[0]+dimensions[0]*0, location[1] + dimensions[0]*2], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*1, location[1] + dimensions[0]*2], dimensions))
    object_list.append(BlockDoor([location[0]+dimensions[0]*2, location[1] + dimensions[0]*2], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*3, location[1] + dimensions[0]*2], dimensions))
    object_list.append(BlockStone([location[0]+dimensions[0]*4, location[1] + dimensions[0]*2], dimensions))
