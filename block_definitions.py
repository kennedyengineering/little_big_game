from block_object import Block
from sprite_object import spritesheet


class BlockGrass(Block):
    def __init__(self, location=[0,0], dimensions=[16,16], is_obstacle=False):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([0*16, 8*16, 16, 16]), is_obstacle=is_obstacle)


class BlockDirt(Block):
    def __init__(self, location=[0,0], dimensions=[16,16], is_obstacle=False):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([2*16, 1*16, 16, 16]), is_obstacle=is_obstacle)


class BlockStone(Block):
    def __init__(self, location=[0,0], dimensions=[16,16], is_obstacle=False):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([6*16, 1*16, 16, 16]), is_obstacle=is_obstacle)


class BlockWood(Block):
    def __init__(self, location=[0,0], dimensions=[16,16], is_obstacle=False):

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([0*16, 2*16, 16, 16]), is_obstacle=is_obstacle)


class BlockDoor(Block):
    def __init__(self, engine, scene_key, location=[0,0], dimensions=[16,16], is_obstacle=False):
        self.engine = engine
        self.scene_key = scene_key

        block_spritesheet = spritesheet("assets/tiles/basic_tiles.png")

        super().__init__(location, dimensions, surface=block_spritesheet.image_at([2*16, 6*16, 16, 16]), is_obstacle=is_obstacle)

    def action(self, player):
        super().action(player)

        print("door activated", self)

        self.engine.switch_scene(self.scene_key)
