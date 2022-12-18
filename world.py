import pygame as pg
from settings import *
from levels import *
from npc import *



class World:
    def __init__(self, win):
        self.win = win
        self.map = [[], [], []]
        self.current_level = level_one
        self.ladder = pg.image.load("ladder.png")
        self.border = pg.image.load("border.png")
        self.basic_tile = pg.image.load("basic_tile.png")
        self.door = pg.image.load("door.png")
        self.door_first_half = False

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
                    npc = NPC(self.win)
                    self.map[2].append(pg.Rect(npc.x, npc.y, npc.width, npc.height))

                

    def draw_map(self):
        self.door_first_half = False
        for tile_id, tiles in enumerate(self.map[0]):
            if tiles[1] == 1:
                self.win.blit(self.basic_tile, (tiles[0][0], tiles[0][1]))
                #pg.draw.rect(self.win, BLUE, tiles[0])
            elif tiles[1] == 2:
                self.win.blit(self.border, (tiles[0][0], tiles[0][1]))
                #pg.draw.rect(self.win, DARKBLUE, tiles[0])
            elif tiles[1] == 3 and not self.door_first_half:
                self.win.blit(self.door, (tiles[0][0], tiles[0][1]))
                self.door_first_half = True
                #pg.draw.rect(self.win, GRAY, tiles[0])
            elif tiles[1] == 4:
                pg.draw.rect(self.win, YELLOW, (tiles[0][0] + COIN_OFFSET, tiles[0][1] + COIN_OFFSET, COIN_SIZE, COIN_SIZE) )
            elif tiles[1] == 5:
                self.win.blit(self.ladder, (tiles[0][0], tiles[0][1]))
                #pg.draw.rect(self.win, BROWN, tiles[0], 2)
            elif tiles[1] == 6:
                #pg.draw.rect(self.win, RED, tiles[0])
                pass













