import sys
import random
import time
import pygame as pg
from pygame import gfxdraw
from variables import *
from rectangle import Rectangle
from ellipse import Ellipse

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
clock = pg.time.Clock()

def clear():
    screen.fill(WHITE)

screen.fill((255,255,255))

font = pg.font.Font("arial.ttf", 36)

#tools
rectangle_tool = Rectangle()
ellipse_tool = Ellipse()

color_surface = pg.Surface.subsurface(screen, (1086,20,174,130))
tool_surface = pg.Surface.subsurface(screen, (0,0,1280,172))


done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        #rectangle_tool.control(event)
        ellipse_tool.control(event)

    #rectangle_tool.draw(screen,BLACK,2)
    ellipse_tool.draw(screen,BLACK,2)


    tool_surface.fill(LIGHTGREY)

    j = 1
    for i in range(8):
        for j in range(8):
            #print(i)
            #print(j + 8*i)
            if j + 8*i < len(colors):
                pg.draw.rect(color_surface, colors[j + 8*i], (22 * j,22 * i,20,20))
                pg.draw.rect(color_surface, BLACK, (22 * j,22 * i,20,20), 1)


        #pg.draw.rect(screen, (0,0,0), (10 * (i+1),10,20,20), 1, 10)


    # rect = pg.Surface.get_rect(brush)
    # pg.draw.rect(brush, (0,0,0), rect, 1, 10)
    # screen.blit(brush, (10,0))

    # pg.draw.rect(eraser, (0,0,0), rect, 1, 10)
    # screen.blit(eraser, (86,0))

    for i in range(len(buttons)):
        if i % 2:
            rect = buttons[i].get_rect(center = (45*(i-1) + 43,125))
        else:
            rect = buttons[i].get_rect(center = (45*i + 43,45))
        screen.blit(buttons[i], rect)

    



    # pg.draw.line(screen,(0,0,0),(0,20),(1280,20),1)
    pg.draw.line(screen,(0,0,0),(0,172),(1280,172),1)

    text = font.render("CURRENT TOOL: " + "BRUSH", True, (0,0,0))
    text_rect = text.get_rect(center=(640, 480))
    screen.blit(text,text_rect)




    pg.display.flip()