import pygame as pg
from game import *
from settings import *

_ = False

level_one = [

    [1,1,1,1,1,1,1,1,1,1,],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, 2, _, _, _, _, _, _, _, 1],
    [1, 2, 2, _, _, _, _, _, _, 1],
    [1, 2, 2, 2, _, _, _, _, _, 1],
    [1, 2, 2, 2, 2, _, _, _, _, 1],
    [1,1,1,1,1,1,1,1,1,1,]

]

class World:
    def __init__(self, win):
        self.win = win
        self.map = []

    def get_map(self):
        for row_id, rows in enumerate(level_one):
            for column_id, value in enumerate(rows):
                if value:
                    self.map.append([pg.Rect(column_id*TILE_SIZE, row_id*TILE_SIZE, TILE_SIZE, TILE_SIZE), value])


    def draw_tiles(self):
        for tiles in self.map:
            if tiles[1] == 1:
                pg.draw.rect(self.win, GREEN, tiles[0])
            elif tiles[1] == 2:
                pg.draw.rect(self.win, BLUE, tiles[0])