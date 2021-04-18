import pygame
from pygame.math import Vector2
from variables import *

class Eraser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.positions = []
        self.relpos = []
        self.color_list = []

    def control(self, event, tool):
        if tool == "eraser":
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed() == (1,0,0):
                pos, rel = event.pos, event.rel
                pos = Vector2(pos[0],pos[1])
                rel = Vector2(rel[0],rel[1])
                self.positions.append(pos)
                self.relpos.append(rel)
                self.color_list.append(WHITE)
                
    def draw(self, surface):
        for i in range(len(self.positions)):
            # pygame.draw.line(surface, self.color_list[i], self.positions[i], (self.positions[i].x-self.relpos[i].x, self.positions[i].y-self.relpos[i].y), 10)
            # pygame.draw.circle(surface, self.color_list[i], self.positions[i], 4)
            pygame.draw.circle(surface, self.color_list[i], self.positions[i], 30)