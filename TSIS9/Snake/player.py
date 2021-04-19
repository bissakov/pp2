import sys
import time
import random
import pygame
from pygame.math import Vector2
from variables import *

class Player(pygame.sprite.Sprite):
    def __init__(self,lvl):
        super().__init__()
        self.reset(lvl)

    def move(self,event,s):
        if s == "player1":
            if event.type == pygame.KEYDOWN:
                if len(self.body) == 1:
                    if event.key == pygame.K_LEFT:
                        self.direction = Vector2(-1,0)
                    elif event.key == pygame.K_RIGHT:
                        self.direction = Vector2(1,0)
                    elif event.key == pygame.K_UP:
                        self.direction = Vector2(0,-1)
                    elif event.key == pygame.K_DOWN:
                        self.direction = Vector2(0,1)
                else:
                    if event.key == pygame.K_LEFT and self.direction != Vector2(1,0):
                        self.direction = Vector2(-1,0)
                    elif event.key == pygame.K_RIGHT and self.direction != Vector2(-1,0):
                        self.direction = Vector2(1,0)
                    elif event.key == pygame.K_UP and self.direction != Vector2(0,1):
                        self.direction = Vector2(0,-1)
                    elif event.key == pygame.K_DOWN and self.direction != Vector2(0,-1):
                        self.direction = Vector2(0,1)
        else:
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
        
    def draw(self,surface,check,color):
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
            pygame.draw.rect(surface, color, self.rect)
        time.sleep(.1)

    def check_fail(self,lvl):
        self.gameover = False
        if self.body[0].x < 2 or self.body[0].x >= 38:
            self.gameover = True
        if self.body[0].y < 2 or self.body[0].y > 27:
            self.gameover = True

        if lvl > 1:
            for i in range(len(levels[lvl-2])):
                if self.body[0] == levels[lvl-2][i]:
                    self.gameover = True

        if len(self.body) > 2:
            for block in self.body[1:]:
                if block == self.body[0]:
                    self.gameover = True

        return self.gameover

    def reset(self,lvl):
        self.pos = random.choice(food_ranges[lvl-1])
        self.rect = pygame.Rect(self.pos.x * 32 + 1,self.pos.y * 32 + 1,30,30)
        self.body = [Vector2(self.pos.x,self.pos.y)]
        self.direction = Vector2(0,0)
        self.gameover = False
                