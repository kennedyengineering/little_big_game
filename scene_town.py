from scene_object import Scene
from block_definitions import BlockGrass


class SceneTown(Scene):
    def __init__(self):
        super().__init__()

        #block = BlockGrass()
        #self.object_list.append(block)

        for i in range(10):
            for ii in range(10):
                self.object_list.append(BlockGrass(location=[i*64, ii*64], dimensions=[64, 64]))
