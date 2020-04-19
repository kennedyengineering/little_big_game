from scene_object import Scene
from block_definitions import *


class SceneTown(Scene):
    def __init__(self):
        super().__init__()

        # making the floor all grass
        for i in range(11):
            for ii in range(10):
                self.object_list.append(BlockGrass(location=[i*64, ii*64], dimensions=[64, 64]))

        # creating the stone houses
        for i in range(5):
            for ii in range(3):
                self.object_list.append(BlockStone(location=[i*64, ii*64], dimensions=[64, 64]))
        self.object_list.append(BlockDoor(location=[2*64, 2*64], dimensions=[64, 64]))

        for i in range(5):
            for ii in range(3):
                self.object_list.append(BlockStone(location=[6*64+i*64, ii*64], dimensions=[64, 64]))
        self.object_list.append(BlockDoor(location=[6*64+2*64, 2*64], dimensions=[64, 64]))
