import sys
import random
import time
import pygame as pg
import player as p
import collectable
from pygame.math import Vector2, Vector3
from variables import *

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
FPS = pg.time.Clock()

def draw_grid():
    for x in range(X_OFFSET, WIDTH + X_OFFSET + 1, TILESIZE):
        if x == X_OFFSET or x == WIDTH + X_OFFSET:
            pg.draw.line(screen,LIGHTGREY,(x,Y_OFFSET),(x,HEIGHT + Y_OFFSET), 3)
        else:
            pg.draw.line(screen,DARKGREY,(x,Y_OFFSET),(x,HEIGHT + Y_OFFSET))
    for y in range(Y_OFFSET, HEIGHT + Y_OFFSET + 1, TILESIZE):
        if y == Y_OFFSET or y == HEIGHT + Y_OFFSET:
            pg.draw.line(screen,LIGHTGREY,(X_OFFSET,y),(WIDTH + X_OFFSET,y), 3)
        else:
            pg.draw.line(screen,DARKGREY,(X_OFFSET+2,y),(WIDTH + X_OFFSET-2,y))

player = p.Player()
f = collectable.Food()

def GenerateLevel(check):
    if check:
        x = random.choice(list(range(X_OFFSET, int(f.pos.x) * 32 - 64, TILESIZE)) + list(range(int(f.pos.x) * 32 + 64, WIDTH + TILESIZE, TILESIZE)))
        y = random.choice(list(range(Y_OFFSET, int(f.pos.y) * 32 - 64, TILESIZE)) + list(range(int(f.pos.y) * 32 + 64, HEIGHT + TILESIZE, TILESIZE)))
        size = random.choice([0,1])
        return Vector3(x,y,size)

all_obj = pg.sprite.Group()
all_obj.add(player)
all_obj.add(f)

food = pg.sprite.Group()
food.add(f)

font = pg.font.Font("arial.ttf", 36)
score = 0
level = 1

wall = []

eaten = False
generate = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        player.move(event)

    screen.fill((0, 0, 0))

    for entity in all_obj:
        try:
            entity.draw(screen)
        except TypeError:
            entity.draw(screen,eaten)
            eaten = False

    generate = False

    for piece in wall:
        if piece.z == 1:
            rect = pg.Rect(piece.x + 1,piece.y + 1,62,62)
            pg.draw.rect(screen, LIGHTGREY, rect)
        elif piece.z == 0:
            rect = pg.Rect(piece.x + 1,piece.y + 1,30,30)
            pg.draw.rect(screen, LIGHTGREY, rect)

    score_label = font.render("SCORE: " + str(score), True, (255,255,255))
    text_rect = score_label.get_rect(center=(640, 30))
    screen.blit(score_label,text_rect)

    level_label = font.render("LEVEL: " + str(level), True, (255,255,255))
    level_rect = level_label.get_rect(center=(640, 930))
    screen.blit(level_label,level_rect)

    draw_grid()
    
    if player.body[0] == f.pos:
        all_obj.remove(f)
        f = collectable.Food()
        all_obj.add(f)
        food = pg.sprite.Group()
        food.add(f)
        eaten = True
        score += 1
        # if score % 1 == 0 and level <= 3:
        #     wall.clear()
        #     i = 1
        #     generate = True
        #     while i <= level * 7:
        #         wall.append(GenerateLevel(generate)
        #         i += 1
        #     level += 1
        

    

    #player.check_collision()
    # if player.check_collision():
        

    # if pg.sprite.spritecollideany(player, food):
    #     all_obj.remove(f)
    #     f = collectable.Food()
    #     all_obj.add(f)
    #     food = pg.sprite.Group()
    #     food.add(f)
    #     eaten = True
    #     score += 1
    
    # if player.check_fail():
    #     print("fail")
    #     #done = True

        



    pg.display.flip()
    FPS.tick(60)