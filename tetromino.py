from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetrommino, pos):
        self.tetromino = tetrommino
        self.pos = vec(pos) + init_pos_offset

        super().__init__(tetrommino.tetris.sprite_group)
        self.image = pg.Surface([title_Size, title_Size])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * title_Size

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(tetrominoes.keys()))
        self.blocks = [Block(self, pos) for pos in tetrominoes[self.shape]]

    
    def update(self):
        pass