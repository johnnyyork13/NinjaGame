import pygame as pg
from settings import *
from world import *


class NPC:
    def __init__(self, win):
        self.win = win

    def move(self):
        pass


    def update(self, map):
        self.map = map