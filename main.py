import pygame
#import the pygame library

from random import randint
#import random

import math
#import math

from savedata import *

#---------------DEFINES-----------------

def generate_save():
    f = open("savedata.py", "w")
    f.write("savedata = [0.04,0,0]")

def save():
    f = open("savedata.py", "w")
    f.write("savedata = " + str(savedata))
    f.close()

#--------------VARIABLES----------------
x = 50
#x of the player
y = 240
#y of the player
height = 50
#height of the player
width = 50
#width of the player
vel = 5
#idk velocity maybe?

score = 0
#score

game_run = False
#should the game run?
menu = True


pipe_x = 544
#x for all the pipes
pipe_width = 96
#width for the pipes
top_pipe_height = randint(25,360)
#where to stop drawing the pipe
bottom_pipe_y = top_pipe_height + 113
#y of the bottom pipe
bottom_pipe_height = 480 - bottom_pipe_y
# how high the bottom pipe is

isJump = False
#is the player jumping?
jumpCount = 6
#how much to jump
gravity = 5
#how fast to fall

score_image = pygame.image.load('score.png')
#load an image


pygame.init()
#initialize pygame
mainScreen = pygame.display.set_mode((640, 480))
#set display resolution

pygame.display.set_caption("Jumping Birb")
#change the title

run = True
#should the loop run?

while run:
    pygame.time.delay(75)
    #set the delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #close the program if the window closes

    keys = pygame.key.get_pressed()
    #make it simpler to get input



    if game_run:

        if keys[pygame.K_SPACE]:
            isJump = True
            jumpCount = 6
            gravity = 5
            #is the spacebar pressed?

        if keys[pygame.K_r]:
            y = 240

        else:
            gravity = gravity + 1
            y = y + gravity


        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                #maths
                jumpCount -= 1
                #x=x-1
            else:
                jumpCount = 10
                isJump = False
                #reset the jump variables



        mainScreen.fill((0, 213, 255))
        #fill the screen

        #pygame.draw.rect(mainScreen, (220,0,0), (x, round(y), width, height))
        mainScreen.blit(pygame.image.load("birb.png"), (x, round(y)))
        #draw a rectange on screen win, color is #FF0000, the x and y and width and height

        if pipe_x <= 0:
            pipe_x = 544
            #put the pipe back to start
            top_pipe_height = randint(25,360)
            #where to stop drawing the pipe
            bottom_pipe_y = top_pipe_height + 113
            #y of the bottom pipe
            bottom_pipe_height = 480 - bottom_pipe_y
            # how high the bottom pipe is
            score = score + 1
            #change the score
        else:
            pipe_x = pipe_x - 10

        if y < top_pipe_height or y > bottom_pipe_y and pipe_x <= 100:
            game_run = False

        if y + height < top_pipe_height or y + height > bottom_pipe_y and pipe_x <= 100:
            game_run = False

        if pipe_x > 100:
            game_run = True

        if y > 480:
            game_run = False

        #pygame.draw.rect(mainScreen, (0, 191, 35), (pipe_x, 0, pipe_width, top_pipe_height))
        mainScreen.blit(pygame.image.load("pipeb.png"), (pipe_x, top_pipe_height-480))
        #draw the top pipe

        #pygame.draw.rect(mainScreen, (0, 191, 35), (pipe_x, bottom_pipe_y, pipe_width, bottom_pipe_height))
        mainScreen.blit(pygame.image.load("pipe.png"), (pipe_x, bottom_pipe_y))
        #draw the bottom pipe

        mainScreen.blit(score_image, (0, 0))

        if score < 10:
            mainScreen.blit(pygame.image.load(str(score)+".png"), (240, 0))
        if score >= 10:
            mainScreen.blit(pygame.image.load(str(math.floor(score/10))+".png"), (240, 0))
            mainScreen.blit(pygame.image.load(str(score - math.floor(score/10)*10)+".png"), (288, 0))

        pygame.display.update()
        #update the display

    elif menu:
        if keys[pygame.K_SPACE]:
            menu = False
            game_run = True

        mainScreen.fill((0, 213, 255))

        mainScreen.blit(pygame.image.load("back.png"), (0, 0))

        mainScreen.blit(pygame.image.load("logo.png"), (80, 0))

        mainScreen.blit(pygame.image.load("play.png"), (192, 240))

        pygame.display.update()


    else:
        if keys[pygame.K_a]:
            menu = True

        if keys[pygame.K_s]:
            if score > savedata[1]:
                savedata[1] = score
                print("You beat your high score! It is now "+str(score))

            savedata[2] = savedata[2] + score
            print("You have travelled through " + str(savedata[2]) + " pipes!")
            save()

pygame.quit()
#quit pygame
