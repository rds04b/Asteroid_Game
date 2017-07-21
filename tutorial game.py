##Modified pygame project from Sentdex tutorials. Hi-score functionality inspired by M41k Dev3lops

import pygame
import time
import random
import pickle

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (250,0,0)
bright_green = (0,250,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Shooting Game')
clock = pygame.time.Clock()

shipImg = pygame.image.load('falcon.png')
astImg_s = pygame.image.load('s_asteroid.png')
astImg_m = pygame.image.load('m_asteroid.png')
astImg_l = pygame.image.load('l_asteroid.png')
background = pygame.image.load('purple.png')
(ship_width,ship_height) = shipImg.get_rect().size
(asteroid_width,asteroid_height) = astImg_l.get_rect().size
(asteroidM_width,asteroidM_height) = astImg_m.get_rect().size
(asteroidS_width,asteroidS_height) = astImg_s.get_rect().size

pause = False

def asteroids(asteroidx, asteroidy, asteroid_width, asteroid_height):
    gameDisplay.blit(astImg_l, (asteroidx, asteroidy))

def asteroidsM(asteroidx, asteroidy, asteroidM_width, asteroidM_height):
    gameDisplay.blit(astImg_m, (asteroidx, asteroidy))

def asteroidsS(asteroidx, asteroidy, asteroidS_width, asteroidS_height):
    gameDisplay.blit(astImg_s, (asteroidx, asteroidy))

def button(msg,x,y,w,h,ic,ac,font_size,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        
    smallText = pygame.font.Font('joystix.ttf',font_size)
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ( (x + (w/2)), (y + (h/2)) )
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('joystix.ttf',50)
        TextSurf, TextRect = text_objects("Pause", largeText, white)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150,450,185,50,green,bright_green,20,unpause)
        button("Quit",550,450,100,50,red,bright_red,20,quitgame)
        
        pygame.display.update()
        clock.tick(5)
    
def game_intro():
    intro = True

    high_score = show_high_score()


    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('joystix.ttf',50)
        smallText = pygame.font.Font('joystix.ttf',20)
        TextSurf, TextRect = text_objects("Asteroid Field", largeText,white)
        TextSurf2, TextRect2 = text_objects("Successful Navigation Odds: 3720 to 1", smallText,white)
        TextRect.center = ((display_width/2),(display_height/2))
        TextRect2.center = ((display_width/2), (display_height/1.75))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)

        button("Start",150,450,100,50,green,bright_green,20,game_loop)
        button("Quit",550,450,100,50,red,bright_red,20,quitgame)
    
        most_dodged(high_score) 


 
        pygame.display.update()
        clock.tick(5)

def quitgame():
    pygame.quit()
    quit()

def asteroids_dodged(count):
    font = pygame.font.Font('joystix.ttf',25)
    text = font.render("Score: "+str(count), True, white)
    gameDisplay.blit(text, (0,0))

def most_dodged(high_score):
    font = pygame.font.Font('joystix.ttf',25)
    text = font.render("Hi-Score: "+str(high_score), True, white)
    gameDisplay.blit(text, (0,25))

def ship(x,y):
    gameDisplay.blit(shipImg, (x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, size, color, text_x, text_y):
    font = pygame.font.Font('joystix.ttf',size)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = (text_x, text_y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(3)

def crash(dodged):
    crash = True

    random_quote = random.choice(["Pulverised?", "I think I'm melting!" "This is all your fault", "It's our lot in life", "We're Doomed"])
    
    high_score = show_high_score()
    most_dodged(high_score)
    
    high_score_file = open('high_score.txt', 'w')
    dodged = int(dodged)
    str_dodged = str(dodged)
    if high_score is not None:
        if dodged > int(high_score):
           high_score_file.write(str_dodged)
        else:
            high_score_file.write(str(high_score))
       
    
    high_score_file.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('joystix.ttf',50)
        smallText = pygame.font.Font('joystix.ttf',20)
        TextSurf, TextRect = text_objects("Game Over", largeText, white)
        TextSurf2, TextRect2 = text_objects(random_quote, smallText, white)
        TextRect.center = ((display_width/2),(display_height/2))
        TextRect2.center = ((display_width/2), (display_height/1.75))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)

        button("Play Again",150,450,190,50,green,bright_green,20,game_loop)
        button("Quit",550,450,100,50,red,bright_red,20,quitgame)

        pygame.display.update()
        clock.tick(5)

def collision(ax,ay,aw,ah,bx,by,bw,bh):
    return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah

def show_high_score():
    high_score = 0
    try:
        high_score_file = open('high_score.txt', 'r')
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("High Score:", high_score)
    except IOError:
        print("No High Score Yet")
    except ValueError:
        print("I Am Error")
    return high_score

def save_high_score(new_high_score):
    try:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("I Am Error")

def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0
    y_change = 0

    asteroid_startx = random.randrange(0, display_width)
    asteroid_starty = -500
    asteroidM_startx = random.randrange(0, display_width)
    asteroidM_starty = -200
    asteroidS_startx = random.randrange(0, display_width)
    asteroidS_starty = -100
    asteroid_speed = 3
    asteroidM_speed = 6
    asteroidS_speed = 8

    dodged = 0

    high_score = show_high_score()

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -5
                if event.key == pygame.K_RIGHT:
                    x_change += 5
                if event.key == pygame.K_UP:
                    y_change += -5
                if event.key == pygame.K_DOWN:
                    y_change += 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
            
        gameDisplay.fill(black)
        asteroids(asteroid_startx, asteroid_starty, asteroid_width, asteroid_height)
        asteroidsM(asteroidM_startx, asteroidM_starty, asteroidM_width, asteroidM_height)
        asteroidsS(asteroidS_startx, asteroidS_starty, asteroidS_width, asteroidS_height)
        asteroid_starty += asteroid_speed
        asteroidM_starty += asteroidM_speed
        asteroidS_starty += asteroidS_speed
        ship(x,y)
        asteroids_dodged(dodged)
        most_dodged(high_score)

        if x > display_width - ship_width or x < 0:
            x_change = 0

        if y > display_height - ship_height:
            y_change = 0

        if asteroid_starty > display_height:
            asteroid_starty = 0 - asteroid_height
            asteroid_startx = random.randrange(0,display_width)
            dodged += 1
            if dodged % 10 == 0:
                asteroid_speed += 1
 
        if asteroidM_starty > display_height:
            asteroidM_starty = 0 - asteroidM_height
            asteroidM_startx = random.randrange(0,display_width)
            dodged += 1
            if dodged % 10 == 0:
                asteroidM_speed += 1

        if asteroidS_starty > display_height:
            asteroidS_starty = 0 - asteroidS_height
            asteroidS_startx = random.randrange(0,display_width)
            dodged += 1
            if dodged % 10 == 0:
                asteroidS_speed += 1 
 
            
        if collision(x,y,ship_width,ship_height,asteroid_startx,asteroid_starty,asteroid_width,asteroid_height):
            crash(dodged)

        if collision(x,y,ship_width,ship_height,asteroidM_startx,asteroidM_starty,asteroidM_width,asteroidM_height):
            crash(dodged)

        if collision(x,y,ship_width,ship_height,asteroidS_startx,asteroidS_starty,asteroidS_width,asteroidS_height):
            crash(dodged) 

        if high_score is not None:
            high_score = int(high_score)
            if dodged > high_score:
                high_score = dodged
            

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
