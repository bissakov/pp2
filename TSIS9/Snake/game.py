import sys
import pygame as pg
import player as p
import collectable
from variables import *

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
FPS = pg.time.Clock()

def draw_grid():
    for x in range(X_OFFSET, WIDTH + X_OFFSET + 1, TILESIZE):
        pg.draw.line(screen,DARKGREY,(x,Y_OFFSET),(x,HEIGHT + Y_OFFSET))
    for y in range(Y_OFFSET, HEIGHT + Y_OFFSET + 1, TILESIZE):
        pg.draw.line(screen,DARKGREY,(X_OFFSET,y),(WIDTH + X_OFFSET,y))

player = p.Player()
f = collectable.Food()

all_obj = pg.sprite.Group()
all_obj.add(player)
all_obj.add(f)

food = pg.sprite.Group()
food.add(f)

font = pg.font.Font("arial.ttf", 36)
score = 0

eaten = False

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

    text = font.render("SCORE: " + str(score), True, (255,255,255))
    text_rect = text.get_rect(center=(640, 25))
    screen.blit(text,text_rect)

    draw_grid()
    
    if player.body[0] == f.pos:
        all_obj.remove(f)
        f = collectable.Food()
        all_obj.add(f)
        food = pg.sprite.Group()
        food.add(f)
        eaten = True
        score += 1

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