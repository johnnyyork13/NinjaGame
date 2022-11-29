import pygame as pg
from world import *
from settings import *
from game import *

class Player:
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.x = PLAYER_START[0]
        self.y = PLAYER_START[1]
        self.vel = 5
        self.player_img = pg.image.load('ninja.png')

    def move(self):
        dx = 0
        dy = 0
        keys = pg.key.get_pressed()

        #GRAVITY
        dy += 1

        if keys[pg.K_d]:
            dx += self.vel
        if keys[pg.K_a]:
            dx -= self.vel
        if keys[pg.K_SPACE]:
            dy -= 10

        #COLLISION
        for rects in self.map:
            if rects[0].colliderect(pg.Rect(int(self.x + dx), int(self.y + dy), TILE_SIZE, TILE_SIZE)):
                dy = 0

        self.x += dx
        self.y += dy

        pg.draw.rect(self.win, RED, (self.x, self.y, TILE_SIZE, TILE_SIZE))        

    def attack(self):
        pass
            
    
    def update(self):
        self.move()
        self.attack()