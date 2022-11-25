import pygame as pg
from game import *
from settings import *

level_one = [

    [0,0,0,0,0,0,0,0,0,0,],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0,0,0,0,0,0,0,0,0,0,]

]

class World:
    def __init__(self, win):
        self.win = win

    def draw_tiles(self):
        for row_id, rows in enumerate(level_one):
            for column_id, columns in enumerate(rows):
                if columns == 0:
                    pg.draw.rect(self.win, BLUE, (row_id * TILE_SIZE, column_id * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2 )