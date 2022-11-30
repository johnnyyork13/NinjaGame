import pygame as pg
from game import *

class Player():
    def __init__(self, win):
        self.win = win
        self.x = 500
        self.y = 500
        self.vel_x = 5
        self.vel_y = 0
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        self.collide_x = False
        self.collide_y = False

    def move(self):
        dx = 0
        dy = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_d] and not self.collide_x:
            dx += self.vel_x
        if keys[pg.K_a] and not self.collide_x:
            dx -= self.vel_x
        

        #GRAVITY
        dy += 5
            
            
        #CHECK COLLISION FOR TILES
        for tiles in self.map:
            if tiles[0].colliderect(pg.Rect(self.x, self.y + dy, self.width, self.height)):
                dy = 0

            if tiles[0].colliderect(pg.Rect(self.x + dx, self.y, self.width, self.height)):
                dx = 0

            
        


        self.x += dx
        self.y += dy

        pg.draw.rect(self.win, RED, (self.x, self.y, self.width, self.height))

    
    def update(self, map):
        self.map = map
        self.move()
        pg.display.update()