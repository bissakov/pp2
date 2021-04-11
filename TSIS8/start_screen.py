import sys
import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.in_menu = True
        self.rect = pygame.Rect(563,412,155,57)
        self.start = True
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.BLUE = (0,0,255)
        self.YELLOW = (255,255,0)
    def menuAnnotations(self,surface,s,y,color,size):
        font = pygame.font.Font("assets/ARCADECLASSIC.ttf", size, bold=True)
        text = font.render(s, True, color)
        text_rect = text.get_rect(center=(640, y))
        surface.blit(text,text_rect)
    def draw(self,surface,color,SCORE,HIGHSCORE):
        while self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.in_menu = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.rect.midtop[1] >= 412 and self.rect.midtop[1] < 492:
                            self.in_menu = False
                        else:
                            self.in_menu = False
                            sys.exit()
                    if self.rect.midtop[1] < 492:
                        if event.key == pygame.K_DOWN:
                            self.start = False
                            self.rect.move_ip(0,80)
                    else:
                        if event.key == pygame.K_DOWN:
                            self.start = True
                            self.rect.move_ip(0,-80)
                    if self.rect.midtop[1] > 412:
                        if event.key == pygame.K_UP:
                            self.start = True
                            self.rect.move_ip(0,-80)
                    else:
                        if event.key == pygame.K_UP:
                            self.start = False
                            self.rect.move_ip(0,80)
            surface.fill(color)
            if color == (255,0,0):
                pygame.draw.line(surface, self.BLACK, (385,350), (890,350), 10)
                pygame.draw.line(surface, self.BLACK, (385,250), (890,250), 10)
                self.menuAnnotations(surface,"GAME    OVER",300,self.BLACK,96)
                highscore = "Highscore                   " + str(HIGHSCORE)
                self.menuAnnotations(surface,highscore,100,self.YELLOW,48)
                score = "Current Score     " + str(SCORE)
                self.menuAnnotations(surface,score,170,self.YELLOW,48)
                if self.start:
                    self.menuAnnotations(surface,"CONTINUE",440,self.WHITE,56)
                    self.menuAnnotations(surface,"EXIT",520,self.BLACK,56)
                else:
                    self.menuAnnotations(surface,"CONTINUE",440,self.BLACK,56)
                    self.menuAnnotations(surface,"EXIT",520,self.WHITE,56)
            else:
                if self.start:
                    self.menuAnnotations(surface,"START",440,self.BLUE,56)
                    self.menuAnnotations(surface,"EXIT",520,self.BLACK,56)
                else:
                    self.menuAnnotations(surface,"START",440,self.BLACK,56)
                    self.menuAnnotations(surface,"EXIT",520,self.BLUE,56)
            pygame.display.flip()