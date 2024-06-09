import pygame
from pygame.locals import *
from settings import *
import math

class player:

    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_rot

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.dt
        speed_cos = cos_a * speed
        speed_sin = sin_a * speed

        mouse_rel = pygame.mouse.get_rel()
        if self.game.tp % 2 == 0:
            pygame.mouse.set_pos(320,320)
        pygame.mouse.set_visible(False)

        keys = pygame.key.get_pressed()
        if keys[K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_collision(dx, dy)

        self.angle += mouse_rel[0] * player_rot_speed * self.game.dt

        self.angle %= math.tau

    def check(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_collision(self, dx, dy):
        if self.check(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pygame.draw.circle(self.game.screen, (255,0,0), (self.x * 10 + 20, self.y * 10 + 20), 3)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
