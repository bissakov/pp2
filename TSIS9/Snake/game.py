import sys
import pygame as pg
import player as p
import collectable

WIDTH = 1152
HEIGHT = 864
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

pg.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Snake")
FPS = pg.time.Clock()

BLACK = (0,0,0)
DARKGREY = (64,64,64)

#rim = pg.image.load("rim.png")

def draw_grid():
    for x in range(64, WIDTH+65, TILESIZE):
        pg.draw.line(screen,DARKGREY,(x,48),(x,912))
    for y in range(48, HEIGHT+49, TILESIZE):
        pg.draw.line(screen,DARKGREY,(64,y),(1216,y))
    #screen.blit(rim,(0,0))



player = p.Player()
f = collectable.Food()
speed = 1

all_obj = pg.sprite.Group()
all_obj.add(player)
all_obj.add(f)

food = pg.sprite.Group()
food.add(f)

font = pg.font.Font("arial.ttf", 36)
score = 0



done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()
        player.move(event,speed)

    screen.fill((0, 0, 0))

    for entity in all_obj:
        entity.draw(screen)
    text = font.render("SCORE: " + str(score), True, (255,255,255))
    text_rect = text.get_rect(center=(640, 25))
    screen.blit(text,text_rect)

    draw_grid()

    if pg.sprite.spritecollideany(player, food):
        all_obj.remove(f)
        f = collectable.Food()
        all_obj.add(f)
        food = pg.sprite.Group()
        food.add(f)
        score += 1

        



    pg.display.flip()
    FPS.tick(60)