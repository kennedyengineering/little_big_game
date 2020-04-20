

class Scene:
    def __init__(self):
        self.object_list = []

    def shift_scene(self, distance_vector):
        for object1 in self.object_list:
            object1.location[0] += distance_vector[0]
            object1.location[1] += distance_vector[1]

    def render(self, surface):
        for object1 in self.object_list:
            surface.blit(object1.get_surface(), object1.get_location())

    def update(self, player):
        player_rect = player.get_rect()
        for object1 in self.object_list:
            object1_rect = object1.get_rect()
            if object1_rect.colliderect(player_rect):
                object1.action(player)
