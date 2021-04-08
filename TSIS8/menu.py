import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

def menuAnnotations(s,y,color,surface):
    font = pygame.font.Font("ARCADECLASSIC.ttf", 56, bold=True)
    text = font.render(s, True, color)
    text_rect = text.get_rect(center=(640, y))
    surface.blit(text,text_rect)

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.in_menu = True
        self.rect = pygame.Rect(563,412,155,57)
        self.active = 0
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
                            self.active = 1
                            self.rect.move_ip(0,80)
                    if self.rect.midtop[1] > 412:
                        if event.key == pygame.K_UP:
                            self.active = 0
                            self.rect.move_ip(0,-80)
            surface.fill(WHITE)
            if self.active == 0:
                menuAnnotations("START",440,BLUE,surface)
                menuAnnotations("EXIT",520,BLACK,surface)
            else:
                menuAnnotations("START",440,BLACK,surface)
                menuAnnotations("EXIT",520,BLUE,surface)
            pygame.display.flip()