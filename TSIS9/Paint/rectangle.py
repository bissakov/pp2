import pygame
from variables import *

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = (0,0)
        self.start = (0, 0)
        self.size = (0, 0)
        self.rect_list = []
        self.drawing = False
        
    def control(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start = event.pos
            self.size = 0, 0
            self.drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            self.size = end[0] - self.start[0], end[1] - self.start[1]
            rect = pygame.Rect(self.start, self.size)
            self.rect_list.append(rect)
            self.drawing = False
        elif event.type == pygame.MOUSEMOTION and self.drawing:
            end = event.pos
            self.size = end[0] - self.start[0], end[1] - self.start[1]

    def draw(self,surface,color,thickness):
        print(self.start,self.size,end="\t\t")
        print()
        surface.fill(WHITE)
        for rect in self.rect_list:
            pygame.draw.rect(surface, color, rect, thickness)
        pygame.draw.rect(surface, color, (self.start, self.size), thickness)