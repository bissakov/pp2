import random
import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/coin" + str(random.randint(1,3)) + ".png")
        self.rect = self.image.get_rect(center = (random.randint(465, 840),-500))
    def move(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 1200:
            self.rect.top = 0
            self.rect.center = (random.randint(465, 840),-500)
            self.image = pygame.image.load("assets/sprites/coin" + str(random.randint(1,3)) + ".png")
    def draw(self, surface):
        surface.blit(self.image, self.rect)