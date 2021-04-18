import pygame
from variables import *

class Ellipse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = (0,0)
        self.start = (0, 0)
        self.size = (0, 0)
        self.shape_list = []
        self.clr_list = []
        self.drawing = False

    def control(self, event, clr):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start = event.pos
            self.size = 0, 0
            self.drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            self.size = end[0] - self.start[0], end[1] - self.start[1]
            rect = pygame.Rect(self.start, self.size)
            self.clr_list.append(clr)
            self.shape_list.append(rect)
            self.drawing = False
        elif event.type == pygame.MOUSEMOTION and self.drawing:
            end = event.pos
            self.size = end[0] - self.start[0], end[1] - self.start[1]

    def draw(self,surface,thickness):
        color = BLACK
        for i in range(len(self.shape_list)):
            self.shape_list[i].normalize()
            pygame.draw.ellipse(surface, self.clr_list[i], self.shape_list[i], thickness)
            color = self.clr_list[i]
        rect = pygame.Rect(self.start, self.size)
        rect.normalize()
        pygame.draw.ellipse(surface, color, rect, thickness)
    
    def reset(self, flag):
        if flag:
            self.shape_list = []
            self.clr_list = []