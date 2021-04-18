import pygame as pg
from variables import *

class Interface(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pg.font.Font("arial.ttf", 36)

    def draw_grid(self, surface):
        for x in range(X_OFFSET, WIDTH + X_OFFSET + 1, TILESIZE):
            if x == X_OFFSET or x == WIDTH + X_OFFSET:
                pg.draw.line(surface,LIGHTGREY,(x,Y_OFFSET),(x,HEIGHT + Y_OFFSET), 3)
            else:
                pg.draw.line(surface,DARKGREY,(x,Y_OFFSET),(x,HEIGHT + Y_OFFSET))
        for y in range(Y_OFFSET, HEIGHT + Y_OFFSET + 1, TILESIZE):
            if y == Y_OFFSET or y == HEIGHT + Y_OFFSET:
                pg.draw.line(surface,LIGHTGREY,(X_OFFSET,y),(WIDTH + X_OFFSET,y), 3)
            else:
                pg.draw.line(surface,DARKGREY,(X_OFFSET+2,y),(WIDTH + X_OFFSET-2,y))

    def draw(self, surface, SCORE, LEVEL):
        score_label = self.font.render("SCORE: " + str(SCORE), True, WHITE)
        text_rect = score_label.get_rect(center=(640, 30))
        surface.blit(score_label,text_rect)

        level_label = self.font.render("LEVEL: " + str(LEVEL), True, WHITE)
        level_rect = level_label.get_rect(center=(640, 930))
        surface.blit(level_label,level_rect)

        self.draw_grid(surface)