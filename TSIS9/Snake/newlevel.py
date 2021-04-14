import random
import pygame
from pygame.math import Vector2
from variables import *

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        
    def draw(self, surface):
        rect = pygame.Rect(self.pos.x * 32 + 1,self.pos.y * 32 + 1,30,30)
        pygame.draw.rect(surface, LIGHTGREY, rect)

    def randomize(n):
