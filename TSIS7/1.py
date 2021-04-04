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

def clearFromBord(surface,col,thickness):
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness, 0, thickness + 130, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness, w, thickness))
    #pygame.draw.rect(surface, col, pygame.Rect(w, h-thickness, w, thickness))

def drawBorder(surface,col,thickness):
    pygame.draw.rect(surface, col, pygame.Rect(30, 30, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(30, 30, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness-30, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness-30, w, thickness))

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
    while i <= h - 30:
        if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(24, i, 15, 2))
        else: pygame.draw.rect(screen, black, pygame.Rect(27, i, 7, 2))
        #text = font.render("", True, (0, 128, 0))
        i += 15.4
        j += 1

    i = h/2 - 15.4
    j = 1
    while i >= 30:
        if j % 2 != 0: pygame.draw.rect(screen, black, pygame.Rect(24, i, 15, 2))
        else: pygame.draw.rect(screen, black, pygame.Rect(27, i, 7, 2))
        i -= 15.4
        j += 1

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

def annotation(s,x,y,col):
    font = pygame.font.Font("arial.ttf", 32)
    text = font.render(s, True, col)
    screen.blit(text,(x,y))

def writeAnnotations():
    annotation("-",640,50,red)
    annotation("sinus",660,50,black)
    annotation("-",640,80,blue)
    annotation("cosinus",660,80,black)

def drawTrig(s):
    plotPoints = []
    if s == "sin":
        for x in range(0, w):
            y = int(math.sin(x/640.0 * 8 * math.pi + math.pi) * 200 + 240)
            plotPoints.append([x,y])
        pygame.draw.lines(screen, red, False, plotPoints, 2)
        # for i in range(0,len(plotPoints)):
        #     try:
        #         pygame.gfxdraw.line(screen, plotPoints[i][0], plotPoints[i][1], plotPoints[i+1][0], plotPoints[i+1][1], red)
        #     except IndexError:
        #         break
    elif s == "cos":
        for x in range(0, w, 2):
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
    
    drawTrig("sin")
    drawTrig("cos")

    pygame.draw.line(screen, black, (0, h/2), (w, h/2), 2)
    pygame.draw.line(screen, black, (w/2, 0), (w/2, h), 2)

    drawBorder(screen,black,1)
    clearFromBord(screen,white,30)

    writeAnnotations()

    drawPlot()
    
    pygame.display.flip()