import pygame as pg
from settings import *
from levels import *



class World:
    def __init__(self, win):
        self.win = win
        self.map = []

    def make_map(self):
        for row_id, rows in enumerate(level_one):
            for column_id, columns in enumerate(rows):
                if columns:
                    self.map.append([pg.Rect(column_id*TILE_SIZE, row_id*TILE_SIZE, TILE_SIZE, TILE_SIZE), columns])


    def draw_map(self):
        for tiles in self.map:
            if tiles[1] == 1:
                pg.draw.rect(self.win, BLUE, tiles[0])
            elif tiles[1] == 2:
                pg.draw.rect(self.win, DARKBLUE, tiles[0])
            elif tiles[1] == 3:
                pg.draw.rect(self.win, GRAY, tiles[0])
            elif tiles[1] == 4:
                pg.draw.rect(self.win, YELLOW, (tiles[0][0] + COIN_OFFSET, tiles[0][1] + COIN_OFFSET, COIN_SIZE, COIN_SIZE) )













