import random
import time
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.choice(range(64,1216,32))/32
        self.y = random.choice(range(48,912,32))/32
        self.rect = pygame.Rect(self.x,self.y,32,32)
        self.dx = 0
        self.dy = 0
    def move(self,event,speed):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -speed
                self.dy = 0
            elif event.key == pygame.K_RIGHT:
                self.dx = speed
                self.dy = 0
            elif event.key == pygame.K_UP:
                self.dx = 0
                self.dy = -speed
            elif event.key == pygame.K_DOWN:
                self.dx = 0
                self.dy = speed
    def draw(self, surface):
        self.x += self.dx
        self.y += self.dy
        if self.x < 2:
            self.x = 38
        elif self.x >= 38:
            self.x = 2
        elif self.y < 1.5:
            self.y = 28.5
        elif self.y >= 28.5:
            self.y = 1.5
        self.rect = pygame.Rect(self.x*32,self.y*32,32,32)
        pygame.draw.rect(surface, (255,255,255), self.rect)
        time.sleep(.07)