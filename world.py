import pygame as pg
from game import *
from settings import *

level_one = [

    [1,1,1,1,1,1,1,1,1,1,],
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 9, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 2, 9, 9, 9, 9, 9, 9, 9, 1],
    [1, 2, 2, 9, 9, 9, 9, 9, 9, 1],
    [1, 2, 2, 2, 9, 9, 9, 9, 9, 1],
    [1, 2, 2, 2, 2, 9, 9, 9, 9, 1],
    [1,1,1,1,1,1,1,1,1,1,]

]

class World:
    def __init__(self, win):
        self.win = win
        self.map = {}

    def get_map(self):
        for row_id, rows in enumerate(level_one):
            for column_id, value in enumerate(rows):
                if value:
                    self.map[(column_id, row_id)] = value
        
        print(self.map)

    def draw_tiles(self):
        for tiles in self.map.items():
            if tiles[1] == 1:
                pg.draw.rect(self.win, GREEN, (tiles[0][0] * TILE_SIZE, tiles[0][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
            elif tiles[1] == 2:
                pg.draw.rect(self.win, RED, (tiles[0][0] * TILE_SIZE, tiles[0][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)

    
