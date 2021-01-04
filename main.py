import os, sys, random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Eko Ninja")
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
background_image = pygame.image.load("Background.png").convert_alpha()

pygame.font.init()
title_font = pygame.font.Font("HanaleiFill-Regular.ttf", 32)
font = pygame.font.Font("BigShouldersText-Regular.ttf", 24)
location = "Home Menu"

player_skin = False
blue_skin = pygame.image.load("Skins/Blue.png").convert_alpha()
brown_skin = pygame.image.load("Skins/Brown.png").convert_alpha()
green_skin = pygame.image.load("Skins/Green.png").convert_alpha()
pink_skin = pygame.image.load("Skins/Pink.png").convert_alpha()
purple_skin = pygame.image.load("Skins/Purple.png").convert_alpha()
red_skin = pygame.image.load("Skins/Red.png").convert_alpha()

mouse_clicked = False

play_button = pygame.image.load("Buttons/Play.png").convert_alpha()
htp_button = pygame.image.load("Buttons/How To Play.png").convert_alpha()

def clicked(rect):
    if mouse_clicked and rect.collidepoint(pygame.mouse.get_pos()):
        return True
    return False

while 1:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            os._quit(0)
        if event.type == MOUSEBUTTONDOWN:
            mouse_clicked = True
        if event.type == MOUSEBUTTONUP:
            mouse_clicked = False
    screen.blit(background_image, (0, 0))
    if location == "Home Menu":
        screen.blit(blue_skin, (10, 10))
        screen.blit(pygame.transform.flip(green_skin, True, False), (705, 10))
        screen.blit(red_skin, (10, 430))
        screen.blit(pygame.transform.flip(purple_skin, True, False), (705, 430))

        screen.blit(play_button, (300, 245))
        screen.blit(htp_button, (300, 325))

        if clicked(Rect(300, 245, 200, 73)):
            print("You Clicked Play")
            location = "Town Hall"
            
        if clicked(Rect(300, 325, 200, 73)):
            print("You Clicked How To Play")
            location = "Instructions"
        
        title = title_font.render("Eko Ninja", False, (20, 54, 2))
        screen.blit(title, (340, 100))
    pygame.display.update()
