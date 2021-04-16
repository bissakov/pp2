import pygame as pg
from pygame.math import Vector2

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGREY = (64,64,64)
LIGHTGREY = (200,200,200)

save = pg.image.load("assets/save.png")
clear = pg.image.load("assets/clear.png")
brush = pg.image.load("assets/brush.png")
eraser = pg.image.load("assets/eraser.png")
rectange = pg.image.load("assets/rectangle.png")
ellipse = pg.image.load("assets/ellipse.png")

buttons = [
    save,
    clear,
    brush,
    eraser,
    rectange,
    ellipse
]

#[0]save,[1]pencil,[2]brush,[3]eraser,[4]rectangle,[5]ellipse
button_rects = [
    Vector2(419, 20),
    Vector2(419, 98),
    Vector2(503, 20),
    Vector2(503, 98),
    Vector2(587, 20),
    Vector2(587, 98)
]

color_rects = [
    Vector2(686.5, 20),
    Vector2(708.5, 20),
    Vector2(730.5, 20),
    Vector2(752.5, 20),
    Vector2(774.5, 20),
    Vector2(796.5, 20),
    Vector2(818.5, 20),
    Vector2(840.5, 20),
    Vector2(686.5, 42),
    Vector2(708.5, 42),
    Vector2(730.5, 42),
    Vector2(752.5, 42),
    Vector2(774.5, 42),
    Vector2(796.5, 42),
    Vector2(818.5, 42),
    Vector2(840.5, 42),
    Vector2(686.5, 64),
    Vector2(708.5, 64),
    Vector2(730.5, 64),
    Vector2(752.5, 64),
    Vector2(774.5, 64),
    Vector2(796.5, 64),
    Vector2(818.5, 64),
    Vector2(840.5, 64),
    Vector2(686.5, 86),
    Vector2(708.5, 86),
    Vector2(730.5, 86),
    Vector2(752.5, 86),
    Vector2(774.5, 86),
    Vector2(796.5, 86),
    Vector2(818.5, 86),
    Vector2(840.5, 86),
    Vector2(686.5, 108),
    Vector2(708.5, 108),
    Vector2(730.5, 108),
    Vector2(752.5, 108),
    Vector2(774.5, 108),
    Vector2(796.5, 108),
    Vector2(818.5, 108),
    Vector2(840.5, 108),
    Vector2(686.5, 130),
    Vector2(708.5, 130),
    Vector2(730.5, 130),
    Vector2(752.5, 130),
    Vector2(774.5, 130),
    Vector2(796.5, 130),
    Vector2(818.5, 130),
    Vector2(840.5, 130),
    Vector2(686.5, 20),
    Vector2(708.5, 20)
]

colors = [
    #row 1
    (255,128,128),
    (255,255,128),
    (128,255,128),
    (0,255,128),
    (128,255,255),
    (0,128,255),
    (255,128,192),
    (255,128,255),
    #row 2
    (255,0,0),
    (255,255,0),
    (128,255,0),
    (0,255,64),
    (0,255,255),
    (0,128,192),
    (128,128,192),
    (255,0,255),
    #row 3
    (128,64,64),
    (255,128,64),
    (0,255,0),
    (0,128,128),
    (0,64,128),
    (128,128,255),
    (128,0,64),
    (255,0,128),
    #row 4
    (128,0,0),
    (255,128,0),
    (0,128,0),
    (0,128,64),
    (0,0,255),
    (0,0,160),
    (128,0,128),
    (128,0,255),
    #row 5
    (64,0,0),
    (128,64,0),
    (0,64,0),
    (0,64,64),
    (0,0,128),
    (0,0,64),
    (64,0,64),
    (64,0,128),
    #row 6
    (0,0,0),
    (128,128,0),
    (128,128,64),
    (128,128,128),
    (64,128,128),
    (192,192,192),
    (64,0,64),
    (255,255,255)
]