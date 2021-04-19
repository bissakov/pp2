import sys
import random
import pygame as pg
import pickle
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

SCORE = 0
LEVEL = 1

p1 = Player(LEVEL)
p2 = Player(LEVEL)
inteface = Interface()
f = Food(LEVEL)
wall = Wall()
menu = Menu()

menu.draw(screen,BLACK,SCORE)

if menu.load_data:
    load_file = open("save.dat","rb")
    p1 = pickle.load(load_file)
    p2 = pickle.load(load_file)
    f = pickle.load(load_file)
    wall = pickle.load(load_file)
    SCORE = pickle.load(load_file)
    LEVEL = pickle.load(load_file)

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
        # f2 = open("save.txt", "w")
        # f2.write(str(p1.body) + "\n" + str(p1.direction) + "\n" + str(f.pos) + "\n")
        save_file = open("save.dat","wb")
        pickle.dump(p1,save_file)
        pickle.dump(p2,save_file)
        pickle.dump(f,save_file)
        pickle.dump(wall,save_file)
        pickle.dump(SCORE,save_file)
        pickle.dump(LEVEL,save_file)
        save_file.close()

    
    eaten1 = False
    eaten2 = False
    
    # if p1.body[0] == f.pos:
    #     f.reset(LEVEL)
    #     eaten1 = True
    #     SCORE += 1
        
    if p1.body[0] == f.pos:
        f.reset(LEVEL)
        eaten1 = True
        SCORE += 1
        wall.regenerateWalls(SCORE,LEVEL)
        if wall.generate is True and LEVEL < 3:
            LEVEL += 1

    screen.fill((0, 0, 0))
    wall.draw(screen)
    inteface.draw(screen, SCORE, LEVEL)

    f.draw(screen)
    p1.draw(screen,eaten1,DARKBLUE)
    #p2.draw(screen,eaten2,DARKRED)
    
    if p1.check_fail(LEVEL) is True:# or p2.check_fail() is True:
        LEVEL = 1
        SCORE = 0
        p1.reset(LEVEL)
        p2.reset(LEVEL)
        wall.reset()
        f.reset(LEVEL)
        menu = Menu()
        menu.draw(screen,DARKRED,SCORE)
        if menu.load_data:
            load_file = open("save.dat","rb")
            p1 = pickle.load(load_file)
            p2 = pickle.load(load_file)
            f = pickle.load(load_file)
            wall = pickle.load(load_file)
            SCORE = pickle.load(load_file)
            LEVEL = pickle.load(load_file)

    pg.display.flip()
    FPS.tick(60)
