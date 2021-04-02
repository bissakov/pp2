import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
is_blue = True
x = 300
y = 300
x_change = 0
y_change = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0

    x += x_change
    y += y_change

    screen.fill((0, 0, 0))
        
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, [x, y, 10, 10])
        
    pygame.display.flip()
    clock.tick(60)