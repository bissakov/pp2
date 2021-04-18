import random
import pygame
from pygame.math import Vector3
from player import Player
from variables import *

p1 = Player()
p2 = Player()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wall = []
        self.generate = False

    def generateLevel(self):
        if self.generate:
            x = random.choice(range(X_OFFSET, WIDTH + TILESIZE, TILESIZE))
            y = random.choice(range(Y_OFFSET, HEIGHT + TILESIZE, TILESIZE))
            size = random.choice([0,1])
            return Vector3(x,y,size)

    def draw(self, surface):
        for piece in self.wall:
            if piece.z == 1:
                rect = pygame.Rect(piece.x + 1,piece.y + 1,62,62)
                pygame.draw.rect(surface, LIGHTGREY, rect)
            elif piece.z == 0:
                rect = pygame.Rect(piece.x + 1,piece.y + 1,30,30)
                pygame.draw.rect(surface, LIGHTGREY, rect)
    
    def regenerateWalls(self,score,level):
        if score % 1 == 0 and level <= 3:
            self.wall.clear()
            i = 1
            self.generate = True
            while i <= level * 7:
                self.wall.append(self.generateLevel())
                i += 1
            p1.reset()
            p2.reset()

    def reset(self):
        self.wall = []
        self.generate = False