import math

res = WIDTH, HEIGHT = 800, 640
HW, HH = WIDTH // 2, HEIGHT // 2
fps = 0

#player
player_pos = (1, 1)
player_rot = 0
player_speed = 0.004
player_rot_speed = 0.000052


#raycasting settings
FOV = math.pi / 2
HALF_FOV = FOV / 2
NUMRAYS = WIDTH // 2
HALF_NUMRAYS = NUMRAYS // 2
DELTA_ANGLE = FOV / NUMRAYS
MAXD = 26
SD = HW / math.tan(HALF_FOV)
SCALE = WIDTH // NUMRAYS
