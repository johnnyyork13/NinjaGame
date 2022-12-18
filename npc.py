import pygame as pg
from settings import *
from world import *


class NPC:
    def __init__(self, win):
        self.win = win
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50

    def move(self):
        #checking github contribution thing
        pass


    def update(self, map):
        self.map = map
