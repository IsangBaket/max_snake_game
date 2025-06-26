import pygame as pg

vec = pg.math.Vector2

fps = 60
field_color = (48, 39, 32)

anim_time_interval = 150

title_Size = 50
field_size = field_w, field_h = 10, 20
field_res = field_w* title_Size, field_h* title_Size

init_pos_offset = vec(field_w // 2 -1, 0)
move_directions = {'left' : vec(-1, 0), 'right' : vec(1, 0), 'down' : vec(0,1)}

tetrominoes = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}