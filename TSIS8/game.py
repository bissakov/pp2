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

grass = pg.image.load("assets/grass.png")

score = 0
font = pg.font.Font("assets/ARCADECLASSIC.ttf", 72, bold=True)

WHITE = (255,255,255)
RED = (255,0,0)
menu.draw(screen,WHITE)

speed = 5
timer = 0

coin_collected = False

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
            sys.exit()

    #draw grass
    screen.blit(grass,(0,0))

    #draw score
    text = font.render(str(score), True, WHITE)
    screen.blit(text,(100,480))

    #draw every sprite and start moving
    for entity in all_sprites:
        entity.draw(screen)
        try:
            entity.move()
        except TypeError:
            entity.move(speed)

    #change speed with time
    timer += 1
    if (timer / 100) % 5 == 0 and speed <= 11:
        speed += 2

    #coin collision
    if pg.sprite.spritecollideany(player, coins):
        all_sprites.remove(coin)
        coin = collectable.Coin()
        all_sprites.add(coin)
        coins = pg.sprite.Group()
        coins.add(coin)
        score += 1
        
    #enemy collision and reset
    if pg.sprite.spritecollideany(player, enemies):
        for entity in all_sprites:
            entity.kill()

        menu = start_screen.Menu()
        menu.draw(screen,RED)

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
        score = 0

    pg.display.flip()
    FPS.tick(60)
