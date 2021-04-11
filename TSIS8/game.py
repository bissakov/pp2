import sys
import pygame as pg
import player_car
import enemy_cars
import collectable
import start_screen
import road_speed

pg.init()
screen = pg.display.set_mode((1280, 960))
pg.display.set_caption("Game")
FPS = pg.time.Clock()

menu = start_screen.Menu()

move_road = road_speed.Speed()
player = player_car.Player()
enemy = enemy_cars.Enemy()
coin = collectable.Coin()

coins = pg.sprite.Group()
coins.add(coin)

enemies = pg.sprite.Group()
enemies.add(enemy)
all_sprites = pg.sprite.Group()
all_sprites.add(move_road)
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

grass = pg.image.load("assets/sprites/grass.png")

SCORE = 0
HIGHSCORE = 0 #session highscore
font = pg.font.Font("assets/ARCADECLASSIC.ttf", 72, bold=True)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
menu.draw(screen,WHITE,SCORE,HIGHSCORE)

speed = 5

INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 2000)

coin_collected = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == INC_SPEED and speed < 10:
              speed += 0.5
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()

    screen.blit(grass,(0,0))

    #draw SCORE
    text = font.render(str(SCORE), True, WHITE)
    if len(str(SCORE)) == 1:
        pg.draw.rect(screen,BLACK,(1200,0,100,70))
        screen.blit(text,(1220,0))
    else:
        pg.draw.rect(screen,BLACK,(1170,0,110,70))
        screen.blit(text,(1190,0))

    #draw every sprite and start moving
    for entity in all_sprites:
        entity.draw(screen)
        try:
            entity.move()
        except TypeError:
            entity.move(speed)

    #coin collision
    if pg.sprite.spritecollideany(player, coins):
        all_sprites.remove(coin)
        pg.mixer.Sound('assets/sounds/mixkit-bonus-earned-in-video-game-2058.wav').play()
        coin = collectable.Coin()
        all_sprites.add(coin)
        coins = pg.sprite.Group()
        coins.add(coin)
        SCORE += 1
        
    #enemy collision and reset
    if pg.sprite.spritecollideany(player, enemies):
        pg.mixer.Sound('assets/sounds/bomb.ogg').play()
        for entity in all_sprites:
            entity.kill()

        if HIGHSCORE == 0 or SCORE > HIGHSCORE:
            HIGHSCORE = SCORE

        menu = start_screen.Menu()
        menu.draw(screen,RED,SCORE,HIGHSCORE)
        SCORE = 0

        all_sprites.empty()
        enemies.empty()
        coins.empty()

        move_road = road_speed.Speed()
        player = player_car.Player()
        enemy = enemy_cars.Enemy()
        coin = collectable.Coin()
        enemies = pg.sprite.Group()
        enemies.add(enemy)
        all_sprites = pg.sprite.Group()
        all_sprites.add(move_road)
        all_sprites.add(player)
        all_sprites.add(enemy)
        all_sprites.add(coin)

        coins = pg.sprite.Group()
        coins.add(coin)
        speed = 5

    pg.display.flip()
    FPS.tick(60)
