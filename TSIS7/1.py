import pygame
import math
from fractions import Fraction
from pygame import gfxdraw

black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,0]
blue = [0,0,255]
w = 640
h = 480

screen = pygame.display.set_mode((w + 160, h))

screen.fill([255, 255, 255])

def clear(surface,col,thickness):
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness, 0, thickness + 130, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness, w, thickness))
    #pygame.draw.rect(surface, col, pygame.Rect(w, h-thickness, w, thickness))

def annotation(s,x,y,col,sz):
    font = pygame.font.Font("arial.ttf", sz, bold=False)
    text = font.render(s, True, col)
    screen.blit(text,(x,y))

def drawBorder(surface,col,thickness):
    pygame.draw.line(surface, col, (30,30), (w-30,30),thickness)
    pygame.draw.line(surface, col, (30,30), (30,h-30),thickness)
    pygame.draw.line(surface, col, (30,h-30), (w-30,h-30),thickness)
    pygame.draw.line(surface, col, (w-30,30), (w-30,h-30),thickness)
    
    vbound = h - 39.8
    hbound = 560
    j = -1.00
    # pygame.draw.line(surface, col, (0,440.2), (w-thickness-30,440.2),2)
    # pygame.draw.line(surface, col, (0,340.2), (w-thickness-30,340.2),2)
    for i in range(0,9):
        pygame.draw.line(surface, col, (30,vbound - 50*i), (w - 30,vbound - 50*i),1)
        annotation(str(format(j, '.2f')),5,vbound - 50*i - 7,black,10)
        j += 0.25
        if i < 7:
            pygame.draw.line(surface, col, (hbound - 80*i,30), (hbound - 80*i,h - 30),1)


def writePi(x):
    num = str(Fraction(x, 2))
    num = num.replace("1","pi")
    if len(num) == 1: num = num + "pi"
    if num.find("pi") < 0: num = num[0:num.find("/")] + "pi" + num[num.find("/"):]
    return num

def drawPlot():
    font = pygame.font.Font(None, 20)
    
    i = h/2 + 15.4
    j = 1
    # while i <= h - 30:
    #     if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(24, i, 15, 2))
    #     else: pygame.draw.rect(screen, black, pygame.Rect(27, i, 7, 2))
    #     i += 15.4
    #     j += 1

    # i = h/2 - 15.4
    # j = 1
    # while i >= 30:
    #     if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(24, i, 15, 2))
    #     else: pygame.draw.rect(screen, black, pygame.Rect(27, i, 7, 2))
    #     i -= 15.4
    #     j += 1

    i = w/2 + 40
    j = 1
    while i <= w-30:
        if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(i,446, 2, 8))
        else: pygame.draw.rect(screen, black, pygame.Rect(i,443.5, 2, 15))

        text = font.render(writePi(j), True, (0, 0, 0))
        
        screen.blit(text,(i-8,460))
        i += 40
        j += 1

    i = w/2 - 40
    j = 1
    while i >= 30:
        if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(i,446, 2, 8))
        else: pygame.draw.rect(screen, black, pygame.Rect(i,443.5, 2, 15))
        text = font.render("-" + writePi(j), True, (0, 0, 0))
        screen.blit(text,(i-8,460))
        i -= 40
        j += 1

def writeAnnotations():
    annotation("-",637,50,red,32)
    annotation("-",645,50,red,32)
    annotation("sinus",660,50,black,32)
    annotation("-",635,80,blue,32)
    annotation("-",647,80,blue,32)
    annotation("cosinus",660,80,black,32)
    pygame.draw.line(screen,white,(636,40),(636,120),3)
    pygame.draw.line(screen,white,(656,40),(656,120),3)

def drawTrig(s):
    plotPoints = []
    if s == "sin":
        for x in range(80, 561):
            y = int(math.sin(x/640.0 * 8 * math.pi + math.pi) * 200 + 240)
            plotPoints.append([x,y])
        pygame.draw.lines(screen, red, False, plotPoints, 2)
        # for i in range(0,len(plotPoints)):
        #     try:
        #         pygame.gfxdraw.line(screen, plotPoints[i][0], plotPoints[i][1], plotPoints[i+1][0], plotPoints[i+1][1], red)
        #     except IndexError:
        #         break
    elif s == "cos":
        for x in range(80, 560, 2):
            y = int(math.cos(x/640.0 * 8 * math.pi + math.pi) * 200 + 240)
            plotPoints.append([x,y])
        for i in range(0,len(plotPoints),2):
            pygame.draw.line(screen, blue, plotPoints[i], plotPoints[i+1],2)
            #pygame.gfxdraw.line(screen, plotPoints[i][0], plotPoints[i][1], plotPoints[i+1][0], plotPoints[i+1][1], blue)

pygame.init()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clear(screen,white,30)
    drawBorder(screen,black,2)

    drawTrig("sin")
    drawTrig("cos")

    pygame.draw.line(screen, black, (30, h/2), (w-30, h/2), 2)
    pygame.draw.line(screen, black, (w/2, 30), (w/2, h-30), 2)

    
    

    writeAnnotations()

    drawPlot()

    
    
    pygame.display.flip()