from scene_object import Scene
from block_definitions import *


class SceneRoom(Scene):
    def __init__(self, engine):
        super().__init__()

        # making the floor
        for i in range(11):
            for ii in range(10):
                self.object_list.append(BlockWood(location=[i*64, 6*64+ii*64], dimensions=[64, 64]))

        # exit door # place door at these coordinates to make it look like the character walked through it
        self.object_list.append(BlockDoor(engine, "town", location=[6*64, 5*64], dimensions=[64, 64]))
