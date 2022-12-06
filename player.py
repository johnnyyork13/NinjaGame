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
        

        if keys[pg.K_SPACE] and not self.jumping and self.climbing == False:
            self.vel_y -= 15
            self.jumping = True
        

        #GRAVITY
        self.vel_y += 1
        if self.vel_y >= JUMP_RATE:
            self.vel_y = JUMP_RATE
        
        
        self.dy += self.vel_y
            
    def ladders(self):
        keys = pg.key.get_pressed()

        if self.ladder_map != []:
            for ladder_blocks in self.ladder_map:
                if ladder_blocks.colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, TILE_SIZE+LADDER_OFFSET, TILE_SIZE+LADDER_OFFSET)) and keys[pg.K_w]:
                    self.climbing = True
                    self.dy -= LADDER_SPEED
                else:
                    self.climbing = False

            
    def collision(self):
        #CHECK COLLISION FOR TILES
        for tiles in self.map:
            #PLATFORM BLOCKS
            if tiles[0].colliderect(pg.Rect(self.x, self.y + self.dy, self.width, self.height)) and tiles[1] in self.BLOCK_LIST:
                if self.vel_y <= JUMP_RATE:
                    self.vel_y = 0
                self.dy = 0
                self.jumping = False
            elif tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y, self.width, self.height)) and tiles[1] in self.BLOCK_LIST:
                self.dx = 0

                
            #PICKUPS AND DOORS
            if tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)) and tiles[1] not in self.BLOCK_LIST:
                #DOORS
                if tiles[1] == 3:
                    self.state += 1
                    self.state_change = False
                #COINS
                if tiles[1] == 4:
                    tiles[0][0] = 1000

                
    def subroutines(self, map):
        self.map = map[0]
        self.ladder_map = map[1]
        self.ladders()

    def update_player(self):
        #update player position
        self.x += self.dx
        self.y += self.dy

        #draw player
        pg.draw.rect(self.win, GREEN, (self.x, self.y, self.width, self.height))
        #pg.draw.circle(self.win, YELLOW, (self.x+self.width/2, self.y+self.height/2), 20)
    
    def update(self, map):
        self.move()
        self.subroutines(map)
        self.collision()
        
        self.update_player()  
        pg.display.update()