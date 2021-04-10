import pygame, sys
import player_car
import enemy_cars
import collectable
import start_screen
import road_speed

pygame.init()
screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Game")
FPS = pygame.time.Clock()

menu = start_screen.Menu()

move_road = road_speed.Speed()
player = player_car.Player()
enemy = enemy_cars.Enemy()
coin = collectable.Coin()

coins = pygame.sprite.Group()
coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(move_road)
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

grass = pygame.image.load("assets/grass.png")

score = 0
font = pygame.font.Font("assets/ARCADECLASSIC.ttf", 72, bold=True)

WHITE = (255,255,255)
RED = (255,0,0)
menu.draw(screen,WHITE)

speed = 5

timer = 0

coin_collected = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            sys.exit()

    screen.blit(grass,(0,0))
      

    text = font.render(str(score), True, WHITE)
    screen.blit(text,(100,480))

    for entity in all_sprites:
        entity.draw(screen)
        try:
            entity.move()
        except TypeError:
            entity.move(speed)

    timer += 1

    if (timer / 100) % 5 == 0 and speed <= 11:
        speed += 2
        

    if pygame.sprite.spritecollideany(player, coins):
        all_sprites.remove(coin)
        coin = collectable.Coin()
        all_sprites.add(coin)
        coins = pygame.sprite.Group()
        coins.add(coin)
        score += 1
       
    #all_sprites.add(coin)
        
    if pygame.sprite.spritecollideany(player, enemies):
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
        enemies = pygame.sprite.Group()
        enemies.add(enemy)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(move_road)
        all_sprites.add(player)
        all_sprites.add(enemy)
        all_sprites.add(coin)

        coins = pygame.sprite.Group()
        coins.add(coin)
        speed = 5
        score = 0
    
    pygame.display.flip()
    FPS.tick(60)
