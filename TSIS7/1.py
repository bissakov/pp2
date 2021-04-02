import pygame
import math

black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [0,0,255]
w = 640
h = 480

screen = pygame.display.set_mode((w, h))

screen.fill([255, 255, 255])

def clearFromBord(surface,col,thickness):
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness, w, thickness))

def drawBorder(surface,col,thickness):
    pygame.draw.rect(surface, col, pygame.Rect(30, 30, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(30, 30, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness-30, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness-30, w, thickness))

def drawPlot():
    pygame.draw.line(screen, black, (0, h/2), (w, h/2), 2)
    pygame.draw.line(screen, black, (w/2, 0), (w/2, h), 2)

    i = h/2+15.4
    while i <= h:
        pygame.draw.rect(screen, black, pygame.Rect((w/2)-4, i, 10, 2))
        i += 15.4

    i = h/2-15.4
    while i >= 0:
        pygame.draw.rect(screen, black, pygame.Rect((w/2)-4, i, 10, 2))
        i -= 15.4

    i = w/2 + 40
    while i <= w:
        pygame.draw.rect(screen, black, pygame.Rect(i,(h/2)-6.5, 2, 15))
        i += 40

    i = w/2 + 40
    while i >= 0:
        pygame.draw.rect(screen, black, pygame.Rect(i,(h/2)-6.5, 2, 15))
        i -= 40


pygame.init()

done = False

plotPoints1 = []
plotPoints2 = []

for x in range(0, w):
    y1 = int(math.sin(x/640.0 * 4 * math.pi + math.pi) * 200 + 240)
    y2 = int(math.cos(x/640.0 * 4 * math.pi + math.pi) * 200 + 240)

    plotPoints1.append([x, y1])
    plotPoints2.append([x, y2])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    pygame.draw.lines(screen, red, False, plotPoints1, 2)
    pygame.draw.lines(screen, blue, False, plotPoints2, 2)

    drawPlot()
    
    drawBorder(screen,black,1)
    clearFromBord(screen,white,30)
    pygame.display.flip()