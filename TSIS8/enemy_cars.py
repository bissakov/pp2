import pygame,random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        num = str(random.randint(1,3))
        self.image = pygame.image.load("assets/enemy" + num + ".png")
        self.shadow = pygame.image.load("assets/enemy" + num + "_shadow.png")
        centerx = random.randint(465, 840)
        self.rect = self.image.get_rect(center = (centerx,0))
        self.rect_shadow = self.image.get_rect(center = (centerx+80,0))
    def move(self,speed):
        random_speed = speed + random.randint(5, 15)
        self.rect.move_ip(0,random_speed)
        self.rect_shadow.move_ip(0,random_speed)
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect_shadow.top = 0
            centerx = random.randint(465, 840)
            self.rect.center = (centerx,-200)
            self.rect_shadow.center = (centerx+80,-200)
            num = str(random.randint(1,3))
            self.image = pygame.image.load("assets/enemy" + num + ".png")
            self.shadow = pygame.image.load("assets/enemy" + num + "_shadow.png")
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.shadow, self.rect_shadow)