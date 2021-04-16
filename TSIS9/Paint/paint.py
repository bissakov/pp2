import sys
import random
import time
import pygame as pg
from pygame import gfxdraw
from variables import *
from rectangle import Rectangle
from ellipse import Ellipse
from interface import Interface
from pygame.mouse import get_pos

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
clock = pg.time.Clock()
paint_surface = pg.Surface.subsurface(screen, (0,172,1280,788))


def cl(tool):
    if tool == "clear":
        paint_surface.fill(WHITE)


#tools
rect_tool = Rectangle()
ellp_tool = Ellipse()

interface = Interface()

active_tool = "NONE"



paint_surface.fill(WHITE)

active_color = BLACK
l = []

done = False
while not done:    
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        if active_tool == "rectangle":
            rect_tool.control(event,active_color)
        elif active_tool == "ellipse":
            ellp_tool.control(event,active_color)

    if interface.choose_color() is not None:
        active_color = interface.choose_color()

    if pg.mouse.get_pressed() == (1,0,0):
        if get_pos()[0] >= button_rects[4].x and get_pos()[0] <= button_rects[4].x+66:
            if get_pos()[1] >= button_rects[4].y and get_pos()[1] <= button_rects[4].y+52:
                active_tool = "rectangle"
            elif get_pos()[1] >= button_rects[5].y and get_pos()[1] <= button_rects[5].y+52:
                active_tool = "ellipse"
        if get_pos()[0] >= button_rects[0].x and get_pos()[0] <= button_rects[0].x+66:
            if get_pos()[1] >= button_rects[0].y and get_pos()[1] <= button_rects[0].y+52:
                drawing = True
                active_tool = "save"
            if get_pos()[1] >= button_rects[1].y and get_pos()[1] <= button_rects[1].y+52:
                drawing = True
                active_tool = "clear"

    paint_surface.fill(WHITE)
    #if active_tool == "rectangle":
    rect_tool.draw(screen,5)
    #elif active_tool == "ellipse":
    ellp_tool.draw(screen,5)

    cl(active_tool)
    
    interface.draw(active_color,active_tool)
    interface.hover(screen)
    
    

    
    





    pg.display.flip()