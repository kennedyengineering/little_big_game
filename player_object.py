# human controlled player
import pygame


class Player:
    def __init__(self, sprite):
        self.sprite = sprite
        self.current_sprite = sprite.down_sprites[0] ###!!!###
        self.location = [0, 0]

        self.is_on_block = []

    def move_left(self, scene):
        self.current_sprite = self.sprite.move_left()
        rect = self.current_sprite.get_rect()
        #self.location[0] -= rect[2]
        scene.shift_scene([-rect[2], 0])
        scene.update(self)
        if False in self.is_on_block or (len(self.is_on_block) == 0):
            scene.shift_scene([rect[2], 0])
        self.is_on_block = []

    def move_right(self, scene):
        self.current_sprite = self.sprite.move_right()
        rect = self.current_sprite.get_rect()
        #self.location[0] += rect[2]
        scene.shift_scene([rect[2], 0])
        scene.update(self)
        if False in self.is_on_block or (len(self.is_on_block) == 0):
            scene.shift_scene([-rect[2], 0])
        self.is_on_block = []

    def move_up(self, scene):
        self.current_sprite = self.sprite.move_up()
        rect = self.current_sprite.get_rect()
        #self.location[1] -= rect[3]
        scene.shift_scene([0, -rect[3]])
        scene.update(self)
        if False in self.is_on_block or (len(self.is_on_block) == 0):
            scene.shift_scene([0, rect[3]])
        self.is_on_block = []

    def move_down(self, scene):
        self.current_sprite = self.sprite.move_down()
        rect = self.current_sprite.get_rect()
        #self.location[1] += rect[3]
        scene.shift_scene([0, rect[3]])
        scene.update(self)
        if False in self.is_on_block or (len(self.is_on_block) == 0):
            scene.shift_scene([0, -rect[3]])
        self.is_on_block = []

    def get_rect(self):
        return pygame.Rect(self.location[0], self.location[1],
                           self.current_sprite.get_rect()[2], self.current_sprite.get_rect()[3])

    def get_sprite(self):
        return self.current_sprite

    def get_location(self):
        return self.location
