import pygame
from KID_sprite import KidSprite
from player_object import Player
from scene_town import SceneTown

class gameEngine():
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((832, 640))
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.player = Player(KidSprite())
        self.current_scene = SceneTown()

    def render(self):

        self.window.fill((0, 0, 0))

        if self.current_scene is not None:
            self.current_scene.render(self.window)

        self.window.blit(self.player.get_sprite(), self.player.get_location())

        pygame.display.flip()

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move_up(self.current_scene)
                elif event.key == pygame.K_a:
                    self.player.move_left(self.current_scene)
                elif event.key == pygame.K_s:
                    self.player.move_down(self.current_scene)
                elif event.key == pygame.K_d:
                    self.player.move_right(self.current_scene)

        if self.current_scene is not None:
            self.current_scene.update()

        self.render()

        self.clock.tick(self.FPS)

        return True
