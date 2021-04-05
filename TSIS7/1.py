import pygame
import math
from fractions import Fraction
from pygame import gfxdraw

black = [0, 0, 0]
white = [255, 255, 255]
red = [255,0,120]
blue = [120,0,255]
w = 640
h = 480

screen = pygame.display.set_mode((w + 160, h))

screen.fill([255, 255, 255])

def clear(surface,col,thickness): # font bug
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, w, thickness))
    pygame.draw.rect(surface, col, pygame.Rect(0, 0, thickness, h))
    pygame.draw.rect(surface, col, pygame.Rect(w-thickness, 0, thickness + 130, h))
    pygame.draw.rect(surface, col, pygame.Rect(0, h-thickness, w, thickness))

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

    for i in range(0,9):
        pygame.draw.line(surface, col, (30,vbound - 50*i), (w - 30,vbound - 50*i),1)
        annotation(str(format(j, '.2f')),5,vbound - 50*i - 7,black,10)
        j += 0.25
        if i < 7:
            pygame.draw.line(surface, col, (hbound - 80*i,30), (hbound - 80*i,h - 30),1)


def writePi(x):
    if x != 0:
        num = str(Fraction(x))
        num = num.replace("1","pi")
        if len(num) == 1 or len(num) == 2 and num != "pi": num = num + "pi"
        if num.find("pi") < 0: num = num[0:num.find("/")] + "pi" + num[num.find("/"):]
        return num

def drawPlot():
    font = pygame.font.Font("arial.ttf", 12)
    vbound = h - 39.8
    j = 1
    for i in range(1,32):
        if i % 4 == 0: continue
        j = i + 2
        if j % 4 == 0:
            pygame.draw.line(screen, black, (30,vbound - i*12.5), (40,vbound - i*12.5),2)
            pygame.draw.line(screen, black, (w-30,vbound - i*12.5), (w-40,vbound - i*12.5),2)
        else:
            pygame.draw.line(screen, black, (30,vbound - i*12.5), (35,vbound - i*12.5),2)
            pygame.draw.line(screen, black, (w-30,vbound - i*12.5), (w-35,vbound - i*12.5),2)

    text = font.render("0", True, (0, 0, 0))
    screen.blit(text,(320,460))

    hbound = 540
    j = 1
    for i in range(0,26):
        if i % 2 != 0:
            if j % 2 != 0 and i < 23:
                #pygame.draw.rect(screen, black, pygame.Rect(hbound - 20*i,444, 2, 6))
                #pygame.draw.rect(screen, black, pygame.Rect(hbound - 20*i,h-448, 2, 6))
                pygame.draw.line(screen,black,(hbound - 20*i,450),(hbound - 20*i,445),2)
                pygame.draw.line(screen,black,(hbound - 20*i,h-450),(hbound - 20*i,h-444),2)
            
            j += 1
            num = writePi(3 - (j-2)*(1/2))
            text = font.render(num, True, (0, 0, 0))
            try:
                if len(num) == 2:
                    screen.blit(text,(hbound+17-(i-1)*20,460))
                elif len(num) <= 5:
                    screen.blit(text,(hbound+10-(i-1)*20,460))
                else:
                    screen.blit(text,(hbound+8-(i-1)*20,460))
            except TypeError: continue
            
        elif i < 23:
            # pygame.draw.rect(screen, black, pygame.Rect(hbound - 20*i,446, 2, 4))
            # pygame.draw.rect(screen, black, pygame.Rect(hbound - 20*i,h-448, 2, 4))
            pygame.draw.line(screen,black,(hbound - 20*i,450),(hbound - 20*i,447),2)
            pygame.draw.line(screen,black,(hbound - 20*i,h-450),(hbound - 20*i,h-446),2)
        
        

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
        pygame.draw.lines(screen, red, False, plotPoints, 3)
    elif s == "cos":
        for x in range(80, 560, 2):
            y = int(math.cos(x/640.0 * 8 * math.pi + math.pi) * 200 + 240)
            plotPoints.append([x,y])
        for i in range(0,len(plotPoints),2):
            pygame.draw.line(screen, blue, plotPoints[i], plotPoints[i+1],3)

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