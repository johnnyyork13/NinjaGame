import pygame as pg
from game import *

class Player():
    def __init__(self, win):
        self.win = win
        self.x = PLAYER_START[0]
        self.y = PLAYER_START[1]
        self.vel_x = 5
        self.vel_y = 0
        self.width = PLAYER_SIZE[0]
        self.height = PLAYER_SIZE[1]
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        self.collide_x = False
        self.collide_y = False
        self.jumping = False
        self.dx = 0
        self.dy = 0
        self.door = False
        self.coin = False

    def move(self):
        self.dx = 0
        self.dy = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_d] and not self.collide_x:
            self.dx += self.vel_x
        if keys[pg.K_a] and not self.collide_x:
            self.dx -= self.vel_x

        if keys[pg.K_SPACE] and not self.jumping:
            self.vel_y -= 15
            self.jumping = True
        

        #GRAVITY
        self.vel_y += 1
        if self.vel_y >= JUMP_RATE:
            self.vel_y = JUMP_RATE
        
        self.dy += self.vel_y
            

    def collision(self):
        #CHECK COLLISION FOR TILES
        for tiles in self.map:
            if tiles[0].colliderect(pg.Rect(self.x, self.y + self.dy, self.width, self.height)) and (tiles[1] in [1,2]):
                if self.vel_y <= JUMP_RATE:
                    self.vel_y = 0
                self.dy = 0
                self.jumping = False

            if tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y, self.width, self.height)) and (tiles[1] in [1,2]):
                self.dx = 0
            
            if tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)) and (tiles[1] not in [1,2]):
                if tiles[1] == 3:
                    print('door')
                if tiles[1] == 4:
                    tiles[0][0] = 1000

    def update_player(self):
        #update player position
        self.x += self.dx
        self.y += self.dy

        #draw player
        pg.draw.rect(self.win, RED, (self.x, self.y, self.width, self.height))
    
    def update(self, map):
        self.map = map
        self.move()
        self.collision()
        self.update_player()  
        pg.display.update()