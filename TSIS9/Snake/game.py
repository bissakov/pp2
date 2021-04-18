import sys
import random
import pygame as pg
from player import Player
from interface import Interface
from collectable import Food
from obstacle import Wall
from start_screen import Menu
from pygame.math import Vector2, Vector3
from variables import *

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
FPS = pg.time.Clock()

p1 = Player()
p2 = Player()
inteface = Interface()
f = Food()
wall = Wall()
menu = Menu()

food = pg.sprite.Group()
food.add(f)

SCORE = 0
HIGHSCORE = 0
LEVEL = 1

menu.draw(screen,BLACK,SCORE,HIGHSCORE)

eaten1 = False
eaten2 = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        p1.move(event,"player1")
        p2.move(event,"player2")

    all_keys = pg.key.get_pressed()
    if all_keys[pg.K_LCTRL] and all_keys[pg.K_s]:
        f2 = open("save.txt", "w")
        f2.write(str(p1.body) + "\n" + str(p1.direction) + "\n" + str(f.pos) + "\n")

    screen.fill((0, 0, 0))

    f.draw(screen)
    p1.draw(screen,eaten1,DARKBLUE)
    #p2.draw(screen,eaten2,DARKRED)
    eaten1 = False
    eaten2 = False

    wall.draw(screen)
    inteface.draw(screen, SCORE, LEVEL)
    
    if p1.body[0] == f.pos:
        f.reset()
        eaten1 = True
        SCORE += 1
        wall.regenerateWalls(SCORE,LEVEL)
        if wall.generate is True:
            LEVEL += 1
    # if p2.body[0] == f.pos:
    #     f.reset()
    #     eaten2 = True
    #     SCORE += 1
    #     wall.regenerateWalls(SCORE,LEVEL)
    #     if wall.generate is True:
    #         LEVEL += 1
    
    if p1.check_fail() is True or p2.check_fail() is True:
        if SCORE > HIGHSCORE:
            HIGHSCORE = SCORE
        p1.reset()
        p2.reset()
        wall.reset()
        menu = Menu()
        menu.draw(screen,DARKRED,SCORE,HIGHSCORE)
        SCORE = 0
        LEVEL = 0

    pg.display.flip()
    FPS.tick(60)
