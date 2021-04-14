import random
import pygame
from pygame.math import Vector2
from variables import *

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.choice(range(X_OFFSET, WIDTH + TILESIZE, TILESIZE)) // TILESIZE
        self.y = random.choice(range(Y_OFFSET, HEIGHT + TILESIZE, TILESIZE)) // TILESIZE
        self.pos = Vector2(self.x,self.y)
        
    def draw(self, surface):
        rect = pygame.Rect(self.pos.x * 32 + 1,self.pos.y * 32 + 1,30,30)
        pygame.draw.rect(surface, (255,255,0), rect)