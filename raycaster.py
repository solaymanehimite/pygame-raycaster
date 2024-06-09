import pygame, math
from settings import *


class raycaster:

    def __init__(self, game):
        self.game = game

    def raycast(self):
        pygame.draw.rect(self.game.screen, (100,100,255), (0,0,800,320))
        pygame.draw.rect(self.game.screen, (100,100,100), (0,320,800,320))
        ox, oy = self.game.player.pos
        xm, ym = self.game.player.map_pos


        ray_angle = self.game.player.angle - HALF_FOV + 0.0000001
        for ray in range(NUMRAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horzs
            yh, dy = (ym + 1, 1) if sin_a > 0 else (ym - 1e-6, -1)
            depth_h = (yh - oy) / sin_a
            xh = ox + depth_h * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAXD):
                tile_h = int(xh), int(yh)
                if tile_h in self.game.map.world_map:
                    break
                xh += dx
                yh += dy
                depth_h += delta_depth

            #verts
            xv, dx = (xm + 1, 1) if cos_a > 0 else (xm - 1e-6, -1)
            depth_v = (xv - ox) / cos_a
            yv = oy + depth_v * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAXD):
                tile_v = int(xv), int(yv)
                if tile_v in self.game.map.world_map:
                    break
                xv += dx
                yv += dy
                depth_v += delta_depth


            #SMALLEST depth
            if depth_v < depth_h:
                depth = depth_v
                color = 100

            else:
                depth = depth_h
                color = 255

            depth *= math.cos(self.game.player.angle - ray_angle)

            #color = 255 / (1 + depth ** 5 * 0.0002)
            proj_h = SD / (depth + 0.0000001)
            pygame.draw.rect(self.game.screen, (0,color,0), (ray * SCALE, HH - proj_h // 2, SCALE, proj_h))
            pygame.draw.rect(self.game.screen, (0,color,0), (ray * SCALE, HH + proj_h // 2, SCALE, proj_h))

            #pygame.draw.line(self.game.screen, (0,255,0), ((20 * ox) + 20, (20 * oy) + 20), (20 * ox + 20 * depth * cos_a, 20 * oy + 20 * depth * sin_a), 1)

            ray_angle += DELTA_ANGLE

    def update(self):
        self.raycast()
