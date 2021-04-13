import random
import time
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.choice(range(64,1216,32))/32
        self.y = random.choice(range(48,912,32))/32
        self.head = pygame.Rect(self.x,self.y,32,32)
        self.tail = self.head
        self.link_count = 1
        self.snake = pygame.sprite.Group()
        self.snake.add(self.head)
        self.dx = 0
        self.dy = 0
    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -1
                self.dy = 0
            elif event.key == pygame.K_RIGHT:
                self.dx = 1
                self.dy = 0
            elif event.key == pygame.K_UP:
                self.dx = 0
                self.dy = -1
            elif event.key == pygame.K_DOWN:
                self.dx = 0
                self.dy = 1
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
        self.head = pygame.Rect(self.x*32,self.y*32,32,32)
        pygame.draw.rect(surface, (255,255,255), self.head)
        time.sleep(.07)
    def grow(self,surface,check):
        if check:
            self.link_count += 1
            self.tail = pygame.Rect(self.x*32+32,self.y*32,32,32)
            if self.dx == -1:
                pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x*32+32,self.y*32,32,32))
            elif self.dx == 1:
                pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x*32-32,self.y*32,32,32))
            elif self.dy == -1:
                pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x*32,self.y*32+32,32,32))
            elif self.dy == 1:
                pygame.draw.rect(surface, (255,255,255), pygame.Rect(self.x*32,self.y*32-32,32,32))