from scene_object import Scene
from block_definitions import *


class SceneTown(Scene):
    def __init__(self):
        super().__init__()

        #block = BlockGrass()
        #self.object_list.append(block)

        for i in range(11):
            for ii in range(10):
                self.object_list.append(BlockDirt(location=[i*64, ii*64], dimensions=[64, 64]))

        construct_stone_house(self.object_list, [0, 0], [64, 64])
        construct_stone_house(self.object_list, [6*64, 0], [64, 64])
