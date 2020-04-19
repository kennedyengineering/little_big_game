import pygame


class Block:
    def __init__(self, location=[0,0], dimensions=[16,16], surface=None):
        self.location = location
        self.dimensions = dimensions
        if surface is None:
            self.surface = pygame.Surface(self.dimensions)
        else:
            self.surface = surface
            self.surface = pygame.transform.scale(self.surface, dimensions)

    def action(self, block):
        pass

    def get_surface(self):
        return self.surface

    def get_rect(self):
        return pygame.Rect(self.location[0], self.location[1], self.dimensions[0], self.dimensions[1])

    def get_location(self):
        return self.location
