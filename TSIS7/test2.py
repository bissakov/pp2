import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
is_blue = True
x = 300
y = 300
x_change = 0
y_change = 0




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    color = (0, 128, 255)
    pygame.draw.circle(screen, color, (500,500), 50)
    pygame.display.flip()