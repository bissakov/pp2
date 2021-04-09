import pygame, sys
import player_car, enemy_cars, collectable, start_screen

pygame.init()

screen = pygame.display.set_mode((1280, 960))

pygame.display.set_caption("Game")

menu = start_screen.Menu()

FPS = pygame.time.Clock()

player = player_car.Player()
enemy = enemy_cars.Enemy()
coin = collectable.Coin()

enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
coins = pygame.sprite.Group()
coins.add(coin)

grass = pygame.image.load("assets/grass.png")
road = pygame.image.load("assets/road.png")

road_velocity = 300
coin_velocity = 80

score = 0
font = pygame.font.Font("assets/arial.ttf", 48, bold=True)

WHITE = (255,255,255)
RED = (255,0,0)
menu.draw(screen,WHITE)

speed = 5

timer = 0

gameover = True

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            sys.exit()

    screen.blit(grass,(0,0))

    if road_velocity >= 960:
        road_velocity = 0
    if coin_velocity >= 800:
        coin_velocity = -200
        all_sprites.add(coin)

    road_velocity += speed
    coin_velocity += speed
    screen.blit(road,(320,road_velocity-960))
    screen.blit(road,(320,road_velocity))
    

    text = font.render(str(score), True, (0, 0, 0))
    screen.blit(text,(0,0))

    for entity in all_sprites:
        entity.draw(screen)
        try:
            entity.move()
        except TypeError:
            entity.move(speed)

    timer += 1

    if (timer / 100) % 5 == 0 and speed <= 11:
        speed += 2
        

    # if pygame.sprite.spritecollideany(player, coins):
    #     all_sprites.remove(coin)
    #     pygame.display.update()
    #     score += 1
       
    #all_sprites.add(coin)
        
    if pygame.sprite.spritecollideany(player, enemies):
        for entity in all_sprites:
            entity.kill()

        menu = start_screen.Menu()
        menu.draw(screen,RED)

        player = player_car.Player()
        enemy = enemy_cars.Enemy()
        coin = collectable.Coin()
        enemies = pygame.sprite.Group()
        enemies.add(enemy)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(enemy)
        all_sprites.add(coin)
        coins = pygame.sprite.Group()
        coins.add(coin)
    
        

    


    pygame.display.flip()
    FPS.tick(60)
