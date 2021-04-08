import pygame,random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/coin1.png")
        self.image = pygame.transform.scale(self.image,(80,128))
        self.rect = self.image.get_rect(center = (random.randint(465, 840),0))
    def move(self):
        self.rect.move_ip(0,5)
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect.center = (random.randint(465, 840),-500)
            self.image = pygame.image.load("assets/coin" + str(random.randint(1,3)) + ".png")
            self.image = pygame.transform.scale(self.image,(80,128))
    def draw(self, surface):
        surface.blit(self.image, self.rect)