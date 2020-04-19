from scene_object import Scene
from block_grass import BlockGrass


class SceneTown(Scene):
    def __init__(self):
        super().__init__()

        block = BlockGrass()
        self.object_list.append(block)