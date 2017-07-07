import pygame as pg
import time
import random as rd
pg.init()

# Screen size
display_width = 800;
display_height = 600;

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0 , 255)
block_color = (53, 115, 255);

gameDisplay = pg.display.set_mode((display_width, display_height));
pg.display.set_caption('A bit Racey');
clock = pg.time.Clock();

carImg = pg.image.load('index.png');

def game_intro():
    intro = True;

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit();
                quit();

        gameDisplay.fill(white);
        largeText = pg.font.Font('freesansbold.ttf', 100);
        TextSurf, TextRect = text_objects("GRAND PRIX", largeText);
        TextRect.center = ((display_width/2), (display_height/2));
        gameDisplay.blit(TextSurf, TextRect);

        pg.draw.rect(gameDisplay, green , (150, 450, 100, 50));
        pg.draw.rect(gameDisplay, red , (550, 450, 100, 50));

        pg.display.update();
        clock.tick(15);


def things_dogded(count):
    font = pg.font.SysFont(None, 25);
    text = font.render("Score : " + str(count), True, black);
    gameDisplay.blit(text, (0,0));

def things(thingx, thingy, thingw, thingh, block_color):
    pg.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingw])

def text_objects(text, font):
	text_surface = font.render(text, True, black);
	return text_surface, text_surface.get_rect();

def message_display(display_text):
    largeText = pg.font.Font('freesansbold.ttf', 100);
    TextSurf, TextRect = text_objects(display_text, largeText);
    TextRect.center = ((display_width/2), (display_height/2));
    gameDisplay.blit(TextSurf, TextRect);
    pg.display.update();
    time.sleep(2);
    game_loop();

def car(x, y):
        gameDisplay.blit(carImg, (x,y));

def crashed():
	message_display('You crashed');

def game_loop():
    x = display_width * 0.4;
    y = display_height * 0.75;
    x_change = 0 ;
    thing_startx = rd.randrange(0, display_width);
    thing_starty = -600;
    thing_speed = 7;
    thing_width = 75;
    thing_height = 75;
    
    dogded = 0;

    # game loop
    
    gameExit = False
    
    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit();
                quit();
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -5;
                
                if event.key == pg.K_RIGHT:
                    x_change = 5;
                    
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0;

        x += x_change;
            
        gameDisplay.fill(white);
            
        things(thing_startx, thing_starty, thing_width, thing_height, block_color);
        thing_starty += thing_speed ;
            
        car(x,y);

        things_dogded(dogded);
            
        if x > display_width - 150 or x < 0:
            crashed();

        if thing_starty > display_height:
            thing_starty = 0 - thing_height;
            thing_startx = rd.randrange(0, display_width);
            dogded += 10;
            thing_speed += 1;
            thing_width += 1;
               
        if y < thing_starty + thing_height :
            if x > thing_startx and x < (thing_startx + thing_width) or (x + 100) > thing_startx and x + 100 < (thing_startx + thing_width) :
                print('x - crossover');
                crashed();

        pg.display.update();
        clock.tick(60);

game_intro();
game_loop();
pg.quit();
quit();

