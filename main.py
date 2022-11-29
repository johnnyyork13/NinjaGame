import pygame as pg
from game import *
from world import *
from settings import *
from player import *


if __name__ == "__main__":
    game = Game()
    player = Player(game.win)
    world = World(game.win)
    world.make_map()

    while True:


        world.draw_map()
        player.update(world.map)
        game.update()