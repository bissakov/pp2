import random
import pygame
from pygame.math import Vector3
from collectable import Food
from player import Player
from variables import *

f = Food()
player = Player()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wall = []
        self.generate = False

    def generateLevel(self):
        if self.generate:
            x = random.choice(list(range(X_OFFSET, int(f.pos.x) * 32 - 64, TILESIZE)) + list(range(int(f.pos.x) * 32 + 64, WIDTH + TILESIZE, TILESIZE)))
            y = random.choice(list(range(Y_OFFSET, int(f.pos.y) * 32 - 64, TILESIZE)) + list(range(int(f.pos.y) * 32 + 64, HEIGHT + TILESIZE, TILESIZE)))
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
            player.reset()

    def reset(self):
        self.wall = []
        self.generate = False