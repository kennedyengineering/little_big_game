import pygame


class Block:
    def __init__(self, location=[0,0], dimensions=[16,16], surface=None):
        self.location = location
        self.dimensions = dimensions
        self.rect = pygame.Rect(location[0], location[1], self.dimensions[0], self.dimensions[1])
        if surface is None: self.surface = pygame.Surface(self.dimensions)
        else: self.surface = surface

    def action(self, block):
        pass

    def get_surface(self):
        return self.surface

    def get_location(self):
        return self.location
