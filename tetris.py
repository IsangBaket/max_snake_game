from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.tetromino = Tetromino(self)

    def draw_grid(self):
        for x in range(field_w):
            for y in range(field_h):
                pg.draw.rect(self.app.screen, 'black',
                             (x * title_Size, y * title_Size, title_Size, title_Size), 1)


    def update(self):
        self.tetromino.update()

    def draw(self):
        self.draw_grid()