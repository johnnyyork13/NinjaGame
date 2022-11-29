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
        self.collide_x = False
        self.collide_y = False

    def move(self):
        dx = 0
        dy = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_d] and not self.collide_x:
            dx += self.vel
        if keys[pg.K_a] and not self.collide_x:
            dx -= self.vel
        if keys[pg.K_w] and not self.collide_y:
            dy -= self.vel
        if keys[pg.K_s] and not self.collide_y:
            dy += self.vel

        #GRAVITY
        dy += self.vel / 2

        #COLLISION
            #CHECK IF OUT OF SCREEN
        if self.x + dx < 0 or (self.x + self.width + dx) > SCREEN_RESOLUTION[0]:
            self.collide_x = True
        else:
            self.collide_y = False

        if self.y + dy < 0 or (self.y + self.height + dy) > SCREEN_RESOLUTION[1]:
            self.collide_y = True
            dx -= 1
        else:
            self.collide_y = False
            
            
        #CHECK COLLISION FOR TILES
        for tiles in self.map:
            tile = pg.Rect(tiles[0])
            player = pg.Rect(int(self.x + dx), int(self.y + dy), TILE_SIZE, TILE_SIZE)
            #LEFT TO RIGHT COLLISION
            if player.colliderect(tile):
                if player.left < tile.right:
                    dx = 0
                if player.top < tile.bottom:
                    dy = 0

            
        


        self.x += dx
        self.y += dy

        pg.draw.rect(self.win, RED, (self.x, self.y, self.width, self.height))

    
    def update(self, map):
        self.map = map
        self.move()
        pg.display.update()