import random
import pygame
from pygame.math import Vector2
from variables import *

class Food(pygame.sprite.Sprite):
    def __init__(self,level):
        super().__init__()
        self.reset(level)
        
    def draw(self, surface):
        rect = pygame.Rect(self.pos.x * 32 + 1,self.pos.y * 32 + 1,30,30)
        pygame.draw.rect(surface, (255,255,0), rect)

    def reset(self,lvl):
        self.pos = random.choice(food_ranges[lvl-1])