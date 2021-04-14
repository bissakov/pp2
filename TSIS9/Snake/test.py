import sys
import pygame as pg
from variables import *

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
FPS = pg.time.Clock()

screen.fill((255,255,255))



done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
    

    

        



    pg.display.flip()
    FPS.tick(60)