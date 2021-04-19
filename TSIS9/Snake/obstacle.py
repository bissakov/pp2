import random
import pygame
from pygame.math import Vector3
from player import Player
from variables import *

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wall = []
        self.generate = False

    def draw(self, surface):
        if self.generate:
            for piece in self.wall:
                rect = pygame.Rect(piece.x * 32 + 1,piece.y * 32 + 1,30,30)
                pygame.draw.rect(surface, LIGHTGREY, rect)
    
    def regenerateWalls(self,score,level):
        if score % 1 == 0 and level <= 3:
            self.generate = True
            self.wall = levels[level-1]

    def reset(self):
        self.wall = []
        self.generate = False