import pygame as pg
from settings import *
from levels import *



class World:
    def __init__(self, win):
        self.win = win
        self.map = [[], [], []]
        self.current_level = level_one

    def check_map(self, state):
        #change displayed map
        #No default state for level_one, so don't check for it
        if state == 1:
            self.current_level = level_two
        

    def make_map(self):
        self.map[0] = []
        self.map[1] = []
        self.map[2] = []
        for row_id, rows in enumerate(self.current_level):
            for column_id, columns in enumerate(rows):
                if columns:
                    self.map[0].append([pg.Rect(column_id*TILE_SIZE, row_id*TILE_SIZE, TILE_SIZE, TILE_SIZE), columns])
                if columns == 5: #ladders
                    self.map[1].append(pg.Rect(column_id*TILE_SIZE, row_id*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if columns == 6: #grunts
                    self.map[2].append(pg.Rect(column_id*TILE_SIZE, row_id*TILE_SIZE, TILE_SIZE, TILE_SIZE))

                

    def draw_map(self):
        for tiles in self.map[0]:
            if tiles[1] == 1:
                pg.draw.rect(self.win, BLUE, tiles[0])
            elif tiles[1] == 2:
                pg.draw.rect(self.win, DARKBLUE, tiles[0])
            elif tiles[1] == 3:
                pg.draw.rect(self.win, GRAY, tiles[0])
            elif tiles[1] == 4:
                pg.draw.rect(self.win, YELLOW, (tiles[0][0] + COIN_OFFSET, tiles[0][1] + COIN_OFFSET, COIN_SIZE, COIN_SIZE) )
            elif tiles[1] == 5:
                pg.draw.rect(self.win, BROWN, tiles[0], 2)
            elif tiles[1] == 6:
                pg.draw.rect(self.win, RED, tiles[0])













