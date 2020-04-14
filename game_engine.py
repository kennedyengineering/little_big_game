import pygame
from KID_sprite import KidSprite
from player_object import Player

class gameEngine():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.player = Player(KidSprite())

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move_up()
                elif event.key == pygame.K_a:
                    self.player.move_left()
                elif event.key == pygame.K_s:
                    self.player.move_down()
                elif event.key == pygame.K_d:
                    self.player.move_right()

        self.window.fill((0, 0, 0))
        self.window.blit(self.player.get_sprite(), self.player.get_location())
        pygame.display.flip()

        self.clock.tick(self.FPS)

        return True