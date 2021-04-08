import pygame,random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/enemy1.png")
        self.rect = self.image.get_rect(center = (random.randint(465, 840),0))
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 1200):
            self.rect.top = 0
            self.rect.center = (random.randint(465, 840),-200)
            self.image = pygame.image.load("assets/enemy" + str(random.randint(1,3)) + ".png")
    def draw(self, surface):
        surface.blit(self.image, self.rect)