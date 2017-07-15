#!/usr/bin/env python3

import pygame as pg

pg.init();

white = (255, 255, 255);
black = (0, 0, 0);
red = (255, 0, 0);
green = (0, 255, 0);
blue = (0, 0, 255);

gameDisplay = pg.display.set_mode((800, 600));
gameDisplay.fill(black);

pixAr = pg.PixelArray(gameDisplay);
pixAr[10][20] = green;
pg.draw.line(gameDisplay, blue, (100,200), (300, 450), 5);
pg.draw.rect(gameDisplay,red, (400, 400, 100, 50) );
pg.draw.circle(gameDisplay, white, (150, 150), 75);
pg.draw.polygon(gameDisplay, green, ((25,75), (76, 125), (250, 375), (400, 25), (60, 540)));

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit();
            quit();

    pg.display.update();

