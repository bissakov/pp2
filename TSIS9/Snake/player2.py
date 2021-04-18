import sys
import time
import random
import pygame
from pygame.math import Vector2
import collectable
from variables import *

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.choice(range(X_OFFSET, WIDTH + TILESIZE, TILESIZE)) / TILESIZE
        self.y = random.choice(range(Y_OFFSET, HEIGHT + TILESIZE, TILESIZE)) / TILESIZE
        self.rect = pygame.Rect(self.x + 1,self.y + 1,30,30)
        self.body = [Vector2(self.x,self.y)]
        self.direction = Vector2(0,0)
        self.gameover = False
        self.food = collectable.Food()

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if len(self.body) == 1:
                if event.key == pygame.K_a:
                    self.direction = Vector2(-1,0)
                elif event.key == pygame.K_d:
                    self.direction = Vector2(1,0)
                elif event.key == pygame.K_w:
                    self.direction = Vector2(0,-1)
                elif event.key == pygame.K_s:
                    self.direction = Vector2(0,1)
            else:
                if event.key == pygame.K_a and self.direction != Vector2(1,0):
                    self.direction = Vector2(-1,0)
                elif event.key == pygame.K_d and self.direction != Vector2(-1,0):
                    self.direction = Vector2(1,0)
                elif event.key == pygame.K_w and self.direction != Vector2(0,1):
                    self.direction = Vector2(0,-1)
                elif event.key == pygame.K_s and self.direction != Vector2(0,-1):
                    self.direction = Vector2(0,1)
        
    def draw(self,surface,check):
        if check:
            body_copy = self.body
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy
        else:
            body_copy = self.body
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:-1]
        for block in self.body:
            x_pos = int(block.x * 32)
            y_pos = int(block.y * 32)
            self.rect = pygame.Rect(x_pos + 1,y_pos + 1,30,30)
            pygame.draw.rect(surface, (255,255,255), self.rect)       
        time.sleep(.07)

    def check_fail(self):
        self.gameover = False
        if self.body[0].x < 2 or self.body[0].x >= 38:
            self.gameover = True
        if self.body[0].y < 2 or self.body[0].y > 27:
            self.gameover = True
        
        for block in self.body[1:]:
            if block == self.body[0]:
                self.gameover = True

        return self.gameover

    def reset(self):
        self.x = random.choice(range(X_OFFSET, WIDTH + TILESIZE, TILESIZE)) / TILESIZE
        self.y = random.choice(range(Y_OFFSET, HEIGHT + TILESIZE, TILESIZE)) / TILESIZE
        self.rect = pygame.Rect(self.x + 1,self.y + 1,30,30)
        self.body = [Vector2(self.x,self.y)]
        self.direction = Vector2(0,0)
        self.gameover = False