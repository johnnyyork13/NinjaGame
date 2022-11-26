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
        self.dx = 0
        self.dy = 0
        self.vel = 5
        self.player_img = pg.image.load('ninja.png')

    def move(self):
        self.dx = 0
        self.dy = 0
        keys = pg.key.get_pressed()

        #GRAVITY
        self.dy += 5

        if keys[pg.K_d]:
            self.dx += self.vel
        if keys[pg.K_a]:
            self.dx -= self.vel
        if keys[pg.K_SPACE]:
            self.dy -= 10

        

    def attack(self):
        pass

    def collision(self):
        print(self.dx)
        player = pg.Rect(self.x + self.dx, self.y + self.dy, TILE_SIZE, TILE_SIZE)
        for tiles in self.map.items():
            #LEFT TO RIGHT COLLISION
            if (tiles[1] != 9 and (player.colliderect(pg.Rect(tiles[0][0]*TILE_SIZE, tiles[0][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)))) and (player.left < tiles[0][0] * TILE_SIZE or player.right > tiles[0][0] * TILE_SIZE):
                pg.draw.rect(self.win, RED, player, 5)
                self.dx = 0
            #TOP TO DOWN COLLISION
            if (tiles[1] != 9 and (player.colliderect(pg.Rect(tiles[0][0]*TILE_SIZE, tiles[0][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)))) and (player.top < tiles[0][1] * TILE_SIZE or player.bottom > tiles[0][1] * TILE_SIZE):
                self.dy = 0
                
            

    def draw(self):
        self.x += self.dx
        self.y += self.dy

        self.win.blit(self.player_img, (self.x, self.y))
        print(str(self.dx) + "new dx")
    
    def update(self):
        self.move()
        self.attack()
        self.collision()
        self.draw()