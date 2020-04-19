from block_object import Block


class BlockGrass(Block):
    def __init__(self, location=[0,0], dimensions=[16,16]):
        super().__init__(location, dimensions)
        self.surface.fill((0, 255, 0))
