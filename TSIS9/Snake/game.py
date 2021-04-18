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

player = Player()
inteface = Interface()
f = Food()
wall = Wall()
menu = Menu()

all_obj = pg.sprite.Group()
all_obj.add(player)
all_obj.add(f)

food = pg.sprite.Group()
food.add(f)

SCORE = 0
HIGHSCORE = 0
LEVEL = 1

menu.draw(screen,BLACK,SCORE,HIGHSCORE)

eaten = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        player.move(event)

    all_keys = pg.key.get_pressed()
    if all_keys[pg.K_LCTRL] and all_keys[pg.K_s]:
        f2 = open("save.txt", "w")
        f2.write(str(player.body) + "\n" + str(player.direction) + "\n" + str(f.pos) + "\n")

    screen.fill((0, 0, 0))

    for entity in all_obj:
        try:
            entity.draw(screen)
        except TypeError:
            entity.draw(screen,eaten)
            eaten = False

    wall.draw(screen)
    inteface.draw(screen, SCORE, LEVEL)
    
    if player.body[0] == f.pos:
        all_obj.remove(f)
        f = Food()
        all_obj.add(f)
        food = pg.sprite.Group()
        food.add(f)
        eaten = True
        SCORE += 1
        wall.regenerateWalls(SCORE,LEVEL)
        if wall.generate is True:
            LEVEL += 1
    
    if player.check_fail():
        if SCORE > HIGHSCORE:
            HIGHSCORE = SCORE
        player.reset()
        wall.reset()
        menu = Menu()
        menu.draw(screen,DARKRED,SCORE,HIGHSCORE)
        SCORE = 0
        LEVEL = 0

    pg.display.flip()
    FPS.tick(60)
