import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.in_menu = True
        self.rect = pygame.Rect(563,412,155,57)
        self.start = True
    def menuAnnotations(self,surface,s,y,color,size):
        font = pygame.font.Font("assets/ARCADECLASSIC.ttf", size, bold=True)
        text = font.render(s, True, color)
        text_rect = text.get_rect(center=(640, y))
        surface.blit(text,text_rect)
    def draw(self,surface):
        while self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.rect.midtop[1] >= 412 and self.rect.midtop[1] < 492:
                            self.in_menu = False
                        else:
                            pygame.quit()
                    if self.rect.midtop[1] < 492:
                        if event.key == pygame.K_DOWN:
                            self.start = False
                            self.rect.move_ip(0,80)
                    if self.rect.midtop[1] > 412:
                        if event.key == pygame.K_UP:
                            self.start = True
                            self.rect.move_ip(0,-80)
            surface.fill(WHITE)
            if self.start:
                self.menuAnnotations(surface,"START",440,BLUE,56)
                self.menuAnnotations(surface,"EXIT",520,BLACK,56)
            else:
                self.menuAnnotations(surface,"START",440,BLACK,56)
                self.menuAnnotations(surface,"EXIT",520,BLUE,56)
            pygame.display.flip()