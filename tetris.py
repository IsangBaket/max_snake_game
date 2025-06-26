from settings import *
import math

class Tetris:
    def __init__(self, app):
        self.app = app

    def draw_grid(self):
        for x in range(field_w):
            for y in range(field_h):
                pg.draw.rect(self.app.screeb, 'black',
                             (x * title_Size, y * title_Size, title_Size, title_Size), 1)


    def update(self):
        pass

    def draw(self):
        self.draw_grid()