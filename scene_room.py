from scene_object import Scene
from block_definitions import *


class SceneRoom(Scene):
    def __init__(self, engine):
        super().__init__()

        # making the floor
        for i in range(11):
            for ii in range(10):
                self.object_list.append(BlockWood(location=[i*64, ii*64], dimensions=[64, 64]))

        # exit door
        self.object_list.append(BlockDoor(engine, "town", location=[2*64, 2*64], dimensions=[64, 64]))
