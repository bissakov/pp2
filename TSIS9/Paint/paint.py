import sys
import random
import time
import pygame as pg
from pygame import gfxdraw

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
clock = pg.time.Clock()

pos = (0,0)
screen.fill((255,255,255))

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        pressed_keys = pg.mouse.get_pressed()
        if pressed_keys == (1,0,0):
            pos = pg.mouse.get_pos()
            screen.fill((0,0,0), (pos, (5, 5)))


    

    #print(pos)



    pg.display.flip()