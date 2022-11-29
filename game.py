import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        self.win = pg.display.set_mode(SCREEN_RESOLUTION)
        self.clock = pg.time.Clock()

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def window(self):
        self.win.fill(BLACK)
        self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() : .1f}")
        

    def update(self):
        self.events()
        self.window()