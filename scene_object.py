import pygame


class Scene:
    def __init__(self):
        self.location = [0, 0]
        self.object_list = []

    def shift_scene(self, distance_vector):
        for object1 in self.object_list:
            object1.location[0] -= distance_vector[0]
            object1.location[1] -= distance_vector[1]

    def render(self, surface):
        for object1 in self.object_list:
            surface.blit(object1.get_surface(), object1.get_location())

    def update(self):
        for object1 in self.object_list:
            for object2 in self.object_list:
                if object1 is object2:
                    continue
                else:
                    if object1.rect.colliderect(object2.rect):
                        object1.action(object2)
