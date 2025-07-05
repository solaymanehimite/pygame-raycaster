import pygame
import sys
from pygame.locals import *

from src.settings import *
from src.map import *
from src.player import *
from src.raycaster import *


class game:

    def __init__(self):
        pygame.init()
        self.tp = 0
        self.screen = pygame.display.set_mode(res)
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.reset()

    def reset(self):
        self.map = Map(self)
        self.player = player(self)
        self.raycaster = raycaster(self)

    def update(self):
        self.player.update()
        pygame.display.update()
        self.dt = self.clock.tick(fps)
        pygame.display.set_caption(f'{self.player.x}-{self.player.y}')
        self.tp += 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.raycaster.update()
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


game().run()
