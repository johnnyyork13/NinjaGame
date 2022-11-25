import pygame as pg
from settings import *
import sys

class Game:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.win = pg.display.set_mode(SCREEN_RESOLUTION)

    def update(self):
        self.clock.tick(FPS)
        pg.display.flip()
        pg.display.set_caption(f"{self.clock.get_fps() : .1f}")

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                pg.quit()
                sys.exit()

