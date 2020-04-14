
class Player():
    def __init__(self, sprite):
        self.sprite = sprite
        self.current_sprite = sprite.down_sprites[0] ###!!!###
        self.location = [0, 0]

    def move_left(self):
        self.current_sprite = self.sprite.move_left()

    def move_right(self):
        self.current_sprite = self.sprite.move_right()

    def move_up(self):
        self.current_sprite = self.sprite.move_up()

    def move_down(self):
        self.current_sprite = self.sprite.move_down()

    def get_sprite(self):
        return self.current_sprite

    def get_location(self):
        return self.location
