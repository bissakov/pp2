import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car = pygame.image.load("assets/player.png")
        self.shadow = pygame.image.load("assets/player_shadow.png")
        self.rect = pygame.Rect(580,750,80,160)
        self.rect_shadow = pygame.Rect(660,750,30,160)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 420:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)
                self.rect_shadow.move_ip(-10, 0)
        if self.rect.right < 860:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)
                self.rect_shadow.move_ip(10, 0)
        if self.rect.top > 0:        
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -10)
                self.rect_shadow.move_ip(0, -10)
        if self.rect.bottom < 920:        
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 10)
                self.rect_shadow.move_ip(0, 10)
    def draw(self, surface):
        surface.blit(self.car, self.rect)
        surface.blit(self.shadow, self.rect_shadow)