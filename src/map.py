import pygame

map = ['WWWWWWWWWWWWWWWW',
       'W              W',
       'W              W',
       'W  W           W',
       'W              W',
       'W              W',
       'W      WW WWW  W',
       'W      W    W  W',
       'W      W    W  W',
       'W      WWWWWW  W',
       'W              W',
       'W              W',
       'W              W',
       'W              W',
       'W              W',
       'WWWWWWWWWWWWWWWW']

class Map:

    def __init__(self, game):
        self.game = game
        self.mini_map = map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val == 'W':
                    self.world_map[(i, j)] = True
    def draw(self):
        pygame.draw.rect(self.game.screen, (0,0,0), (20,20,160,160))
        for pos in self.world_map:
            pygame.draw.rect(self.game.screen, (255,255,255), (pos[0] * 10 + 20, pos[1] * 10 + 20, 10, 10))
