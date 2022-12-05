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
        self.state = 0
        self.state_change = False
        self.climbing = False
        self.ladder_check = False
        self.BLOCK_LIST = [1,2]
        self.ladder_map = []
        

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
        if self.climbing == False:
            self.vel_y += 1
            if self.vel_y >= JUMP_RATE:
                self.vel_y = JUMP_RATE
        
        
        self.dy += self.vel_y
            
    def ladders(self):
        keys = pg.key.get_pressed()
        if not self.ladder_check:
            for tiles in self.map:
                if tiles[1] == 5:
                    self.ladder_map.append(tiles[0])
            self.ladder_check = True

        for tiles in self.ladder_map:
            if tiles.colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)) and keys[pg.K_w]:
                self.climbing = True
                self.dy -= 5
            else:
                self.climbing = False

        
            
                
            

    def collision(self):
        #CHECK COLLISION FOR TILES
        for tiles in self.map:

            if tiles[0].colliderect(pg.Rect(self.x, self.y + self.dy, self.width, self.height)) and tiles[1] in self.BLOCK_LIST:
                if self.vel_y <= JUMP_RATE:
                    self.vel_y = 0
                self.dy = 0
                self.jumping = False
            elif tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y, self.width, self.height)) and tiles[1] in self.BLOCK_LIST:
                self.dx = 0

                
            #PICKUPS AND DOORS
            if tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)) and tiles[1] not in self.BLOCK_LIST:
                if tiles[1] == 3:
                    self.state += 1
                    self.state_change = False
                    self.ladder_map = []
                    self.ladder_check = False

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
        self.ladders()
        self.collision()
        
        self.update_player()  
        pg.display.update()