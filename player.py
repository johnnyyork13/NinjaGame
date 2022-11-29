import pygame as pg
from game import *

class Player():
    def __init__(self, win):
        self.win = win
        self.x = 500
        self.y = 500
        self.vel = 5
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        dx = 0
        dy = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            dx += self.vel
        if keys[pg.K_a]:
            dx -= self.vel
        if keys[pg.K_w]:
            dy -= self.vel
        if keys[pg.K_s]:
            dy += self.vel

        #COLLISION
        for tiles in self.map:
            #LEFT TO RIGHT COLLISION
            if self.x + dx < 0 or (self.x + self.width + dx) > SCREEN_RESOLUTION[0]:
                if pg.Rect(self.x )
               self.x + dx < pg.Rect(tiles[0]).right or self.x + self.width + dx > pg.Rect(tiles[0]).left):
            
                print('here')
                dx = 0
            #TOP TO BOTTOM COLLISION
            if self.y + dy < 0 or (self.y + self.height + dy) > SCREEN_RESOLUTION[1]:
                dy = 0


        self.x += dx
        self.y += dy

        pg.draw.rect(self.win, RED, (self.x, self.y, self.width, self.height))

    
    def update(self, map):
        self.map = map
        self.move()
        pg.display.update()