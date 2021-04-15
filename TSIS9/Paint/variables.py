import pygame as pg

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGREY = (64,64,64)
LIGHTGREY = (200,200,200)

save = pg.image.load("assets/save.png")
pencil = pg.image.load("assets/pencil.png")
brush = pg.image.load("assets/brush.png")
eraser = pg.image.load("assets/eraser.png")
rectange = pg.image.load("assets/rectangle.png")
ellipse = pg.image.load("assets/ellipse.png")

buttons = [
    save,
    pencil,
    brush,
    eraser,
    rectange,
    ellipse
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