import pygame
from pygame.mouse import get_pos
from variables import *
import os

class Interface(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pg.display.set_mode((1280, 960))
        self.color_surface = pg.Surface.subsurface(self.screen, (738,20,174,130))
        self.tool_surface = pg.Surface.subsurface(self.screen, (0,0,1280,200))
        self.current_color_surface = pg.Surface.subsurface(self.screen, (620,36,100,100))
        self.eyedropper = pg.image.load("assets/eyedropper-9.png")
        self.cursor_rect = self.eyedropper.get_rect()
        self.font = pg.font.Font("arial.ttf", 22)
    
    def hover(self,surface):        
        cursor_hidden = False
        for color_rect in color_rects:
            if get_pos()[0] >= color_rect.x and get_pos()[0] <= color_rect.x + 20 and get_pos()[1] >= color_rect.y and get_pos()[1] <= color_rect.y + 20:
                cursor_hidden = True
                pg.mouse.set_visible(False)
                self.cursor_rect.center = (get_pos()[0] + 6,get_pos()[1] - 7) 
                surface.blit(self.eyedropper, self.cursor_rect)
        if cursor_hidden is False:
            pg.mouse.set_visible(True)

    def choose_color(self):
        for i in range(len(color_rects)):
            if pg.mouse.get_pressed() == (1,0,0):
                if get_pos()[0] >= color_rects[i].x and get_pos()[0] <= color_rects[i].x + 20 and get_pos()[1] >= color_rects[i].y and get_pos()[1] <= color_rects[i].y + 20:
                    return colors[i]


    def draw(self,color,active_tool):
        self.tool_surface.fill(LIGHTGREY)
        self.current_color_surface.fill(color)
        pg.draw.rect(self.current_color_surface, BLACK, (0,0,100,100), 1)

        #colors
        j = 1
        for i in range(8):
            for j in range(8):
                if j + 8*i < len(colors):
                    pg.draw.rect(self.color_surface, colors[j + 8*i], (22 * j,22 * i,20,20))
                    pg.draw.rect(self.color_surface, BLACK, (22 * j,22 * i,20,20), 1)
                    num_lines = sum(1 for line in open('color_rects.txt'))
                    if num_lines <= 48:
                        f = open("color_rects.txt", "a")
                        f.write(str(22 * j + 738) + ", " + str(22 * i + 20) + "\n")

        #tools
        for i in range(len(buttons)):
            if i % 2:
                rect = pg.Rect(368 + 42*(i-1), 98, 66, 52)
            else:
                rect = pg.Rect(368 + 42*i, 20, 66, 52)

            # num_lines = sum(1 for line in open('button_rects.txt'))
            # if num_lines <= 6:
            #     f = open("button_rects.txt", "a")
            #     f.write(str(rect) + "\n")

            self.screen.blit(buttons[i], rect)

        text = self.font.render("Current tool: " + active_tool.upper(), True, (0,0,0))
        text_rect = text.get_rect(center=(640, 180))
        self.screen.blit(text,text_rect)

        pg.draw.line(self.screen,(0,0,0),(0,200),(1280,200),1)