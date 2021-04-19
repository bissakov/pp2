import sys
import pygame
import pickle
from variables import *

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.in_menu = True
        self.load_data = False
        self.rect = pygame.Rect(550,372,180,57)
        self.start = 1

    def menuAnnotations(self,surface,s,y,color,size):
        font = pygame.font.Font("assets/arial.ttf", size)
        text = font.render(s, True, color)
        text_rect = text.get_rect(center=(640, y))
        surface.blit(text,text_rect)
    
    def scale_buttons(self):
        if self.rect.y == 372:
            self.rect.w = 180
            self.rect.x = (1280 - self.rect.w) / 2
        elif self.rect.y == 452:
            self.rect.w = 300
            self.rect.x = (1280 - self.rect.w) / 2
        elif self.rect.y == 532:
            self.rect.w = 130
            self.rect.x = (1280 - self.rect.w) / 2

    def draw(self,surface,color,SCORE):
        while self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.in_menu = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.rect.midtop[1] >= 372 and self.rect.midtop[1] < 452:
                            self.in_menu = False
                            self.load_data = False
                        elif self.rect.midtop[1] >= 452 and self.rect.midtop[1] < 532:
                            self.in_menu = False
                            self.load_data = True
                        else:
                            self.in_menu = False
                            self.load_data = False
                            sys.exit()
                    if event.key == pygame.K_DOWN:
                        self.rect.move_ip(0,80)
                        if self.rect.y > 532:
                            self.rect.move_ip(0,-240)
                        self.scale_buttons()
                    elif event.key == pygame.K_UP:
                        self.rect.move_ip(0,-80)
                        if self.rect.y < 372:
                            self.rect.move_ip(0,240)
                        self.scale_buttons()
            surface.fill(color)

            if color == DARKRED:
                score = "Current Score     " + str(SCORE)
                self.menuAnnotations(surface,score,170,YELLOW,48)

                pygame.draw.rect(surface,BLACK,self.rect)
                self.menuAnnotations(surface,"START",400,WHITE,56)
                self.menuAnnotations(surface,"CONTINUE",480,WHITE,56)
                self.menuAnnotations(surface,"EXIT",560,WHITE,56)
            else:
                pygame.draw.rect(surface,DARKBLUE,self.rect)
                self.menuAnnotations(surface,"START",400,WHITE,56)
                self.menuAnnotations(surface,"CONTINUE",480,WHITE,56)
                self.menuAnnotations(surface,"EXIT",560,WHITE,56)
                
            pygame.display.flip()