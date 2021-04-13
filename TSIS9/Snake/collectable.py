import random
import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.choice(range(96,1184,32)),random.choice(range(80,880,32)),32,32)

    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,0), self.rect)