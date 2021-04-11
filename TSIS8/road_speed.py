import pygame

class Speed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.road = pygame.image.load("assets/sprites/road.png")
        self.road_velocity = 300
        self.speed = 5
    def move(self,speed):
        if self.road_velocity >= 960:
            self.road_velocity = 0
        self.road_velocity += speed
    def draw(self, surface):
        surface.blit(self.road,(320,self.road_velocity-960))
        surface.blit(self.road,(320,self.road_velocity))