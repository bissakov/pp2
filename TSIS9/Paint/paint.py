import sys
import random
import time
import pygame as pg
from pygame import gfxdraw
from variables import *
from shapes import Shape
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

font = pg.font.Font("arial.ttf", 36)

#tools
shapes_tool = Shape()

interface = Interface()


# save_button = pg.Rect(button_rects[0].x, button_rects[0].y, 66, 52)
# penc_button = pg.Rect(button_rects[1].x, button_rects[1].y, 66, 52)
# brsh_button = pg.Rect(button_rects[2].x, button_rects[2].y, 66, 52)
# ersr_button = pg.Rect(button_rects[3].x, button_rects[3].y, 66, 52)
# rect_button = pg.Rect(button_rects[4].x, button_rects[4].y, 66, 52)
# ellp_button = pg.Rect(button_rects[5].x, button_rects[5].y, 66, 52)

active_tool = "NONE"

paint_surface.fill(WHITE)

active_color = BLACK

drawing = False

done = False
while not done:    
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        shapes_tool.control(event)

    if interface.choose_color() is not None:
        active_color = interface.choose_color()

    if pg.mouse.get_pressed() == (1,0,0):
        if get_pos()[0] >= button_rects[4].x and get_pos()[0] <= button_rects[4].x+66:
            if get_pos()[1] >= button_rects[4].y and get_pos()[1] <= button_rects[4].y+52:
                drawing = True
                active_tool = "rectangle"
            # if get_pos()[1] >= button_rects[5].y and get_pos()[1] <= button_rects[5].y+52:
            #     drawing = True
            #     active_tool = "ellipse"
        # if get_pos()[0] >= button_rects[0].x and get_pos()[0] <= button_rects[0].x+66:
        #     if get_pos()[1] >= button_rects[0].y and get_pos()[1] <= button_rects[0].y+52:
        #         drawing = True
        #         active_tool = "save"
        #     if get_pos()[1] >= button_rects[1].y and get_pos()[1] <= button_rects[1].y+52:
        #         drawing = True
        #         active_tool = "clear"

    paint_surface.fill(WHITE)
    shapes_tool.draw(screen,active_color,1,active_tool)

    #cl(active_tool)
    
    interface.draw()
    interface.hover(screen)
    
    

    
    
    text = font.render("CURRENT TOOL: " + active_tool, True, (0,0,0))
    text_rect = text.get_rect(center=(640, 480))
    screen.blit(text,text_rect)




    pg.display.flip()