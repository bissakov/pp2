import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        num = str(random.randint(1,3))
        self.image = pygame.image.load("assets/sprites/enemy" + num + ".png")
        centerx = random.randint(465, 840)
        self.rect = self.image.get_rect(center = (centerx,0))
    def move(self,speed):
        random_speed = speed + random.randint(5, 15)
        self.rect.move_ip(0,random_speed)
        if self.rect.bottom > 1200:
            self.rect.top = 0
            centerx = random.randint(465, 840)
            self.rect.center = (centerx,-200)
            num = str(random.randint(1,3))
            self.image = pygame.image.load("assets/sprites/enemy" + num + ".png")
    def draw(self, surface):
        surface.blit(self.image, self.rect)