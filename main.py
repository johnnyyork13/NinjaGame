import pygame as pg
from settings import *
from game import *
from world import *



if __name__ == '__main__':

    while True:
        game = Game()

        world = World(game.win)
        world.draw_tiles()


        game.update()
        game.events()


