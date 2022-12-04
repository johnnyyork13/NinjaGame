import pygame as pg
from game import *
from world import *
from settings import *
from player import *

checked_state = False

if __name__ == "__main__":
    game = Game()
    player = Player(game.win)
    world = World(game.win)
    

    while True:
        if player.state_change == False:
            
            world.make_map()
            player.state_change = True

        world.check_map(player.state)
        world.draw_map()
        player.update(world.map)
        game.update()