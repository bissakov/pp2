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
    Vector2(368, 20),
    Vector2(368, 98),
    Vector2(452, 20),
    Vector2(452, 98),
    Vector2(536, 20),
    Vector2(536, 98),
    Vector2(368, 20),
    Vector2(368, 98),
]

color_rects = [
    Vector2(738, 20),
    Vector2(760, 20),
    Vector2(782, 20),
    Vector2(804, 20),
    Vector2(826, 20),
    Vector2(848, 20),
    Vector2(870, 20),
    Vector2(892, 20),
    Vector2(738, 42),
    Vector2(760, 42),
    Vector2(782, 42),
    Vector2(804, 42),
    Vector2(826, 42),
    Vector2(848, 42),
    Vector2(870, 42),
    Vector2(892, 42),
    Vector2(738, 64),
    Vector2(760, 64),
    Vector2(782, 64),
    Vector2(804, 64),
    Vector2(826, 64),
    Vector2(848, 64),
    Vector2(870, 64),
    Vector2(892, 64),
    Vector2(738, 86),
    Vector2(760, 86),
    Vector2(782, 86),
    Vector2(804, 86),
    Vector2(826, 86),
    Vector2(848, 86),
    Vector2(870, 86),
    Vector2(892, 86),
    Vector2(738, 108),
    Vector2(760, 108),
    Vector2(782, 108),
    Vector2(804, 108),
    Vector2(826, 108),
    Vector2(848, 108),
    Vector2(870, 108),
    Vector2(892, 108),
    Vector2(738, 130),
    Vector2(760, 130),
    Vector2(782, 130),
    Vector2(804, 130),
    Vector2(826, 130),
    Vector2(848, 130),
    Vector2(870, 130),
    Vector2(892, 130),
    Vector2(738, 20),
    Vector2(760, 20)
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

#active_color = BLACK