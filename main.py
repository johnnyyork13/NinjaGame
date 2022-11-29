import pygame as pg
from settings import *
from game import *
from world import *
from player import *

win = pg.display.set_mode(SCREEN_RESOLUTION)

if __name__ == '__main__':

    game = Game(win)
    world = World(game.win)
    world.get_map()

    player = Player(game.win, world.map)

    while True:
        
        world.draw_tiles()

        player.update()
        
        pg.display.update()
        game.update()
        game.events()


