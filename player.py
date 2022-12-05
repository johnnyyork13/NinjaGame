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
        self.ladder = False
        

    def move(self):
        self.dx = 0
        self.dy = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_d] and not self.collide_x:
            self.dx += self.vel_x
        if keys[pg.K_a] and not self.collide_x:
            self.dx -= self.vel_x
        if keys[pg.K_w] and self.ladder:
            self.climbing = True
            self.dy -= 5
        elif not self.ladder:
            self.climbing = False


        if keys[pg.K_SPACE] and not self.jumping:
            self.vel_y -= 15
            self.jumping = True
        

        #GRAVITY
        self.vel_y += 1
        if self.vel_y >= JUMP_RATE:
            self.vel_y = JUMP_RATE
        
        if not self.climbing:
            self.dy += self.vel_y
            

    def collision(self):
        #CHECK COLLISION FOR TILES
        for tiles in self.map:
            if tiles[1] != 5 and not self.climbing:
                if tiles[0].colliderect(pg.Rect(self.x, self.y + self.dy, self.width, self.height)) and (tiles[1] in [1,2]):
                    if self.vel_y <= JUMP_RATE:
                        self.vel_y = 0
                    self.dy = 0
                    self.jumping = False

                elif tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y, self.width, self.height)) and (tiles[1] in [1,2]):
                    self.dx = 0
                
                #PICKUPS AND DOORS
                elif tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)):
                    if tiles[1] == 3:
                        self.state += 1
                        self.state_change = False

                    if tiles[1] == 4:
                        tiles[0][0] = 1000
            elif tiles[1] == 5 and tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)):
                self.ladder = True
            elif tiles[1] == 5 and tiles[0].colliderect(pg.Rect(self.x + self.dx, self.y + self.dy, self.width, self.height)) == False and not self.climbing:
                self.ladder = False
                print('here')
                
    
        
                

            
                
                    
                    
            
                
                    
                


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