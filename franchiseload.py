import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import json

import glovars
import mainmenu
import franchisenew

def initImages():
    global backButtonClickCheck, selected_franchise

    data = open("savedata.json", "r")
    num_franchises = len(json.load(data)["franchises"])

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)
    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    #franchise select
    glovars.message_display("franchise select",668,19,glovars.teamSelectFont,glovars.black)

    #franchises that cannot be selected
    if num_franchises < 5:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,480,824,50),0)
    if num_franchises < 4:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,380,824,50),0)
    if num_franchises < 3:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,280,824,50),0)
    if num_franchises < 2:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,180,824,50),0)

    #franchises that can be selected to load
    if num_franchises > 0:
        pygame.draw.rect(glovars.screen,glovars.white,(100,80,824,50),0)
    if num_franchises > 1:
        pygame.draw.rect(glovars.screen,glovars.white,(100,180,824,50),0)
    if num_franchises > 2:
        pygame.draw.rect(glovars.screen,glovars.white,(100,280,824,50),0)
    if num_franchises > 3:
        pygame.draw.rect(glovars.screen,glovars.white,(100,380,824,50),0)
    if num_franchises > 4:
        pygame.draw.rect(glovars.screen,glovars.white,(100,480,824,50),0)

    #franchises that can be selected as new
    if num_franchises == 4:
        selected_franchise = pygame.draw.rect(glovars.screen,glovars.black,(100,480,824,50),0)
        glovars.message_display("new franchise",110,488,glovars.EASmall30,glovars.white)
    elif num_franchises == 3:
        selected_franchise = pygame.draw.rect(glovars.screen,glovars.black,(100,380,824,50),0)
        glovars.message_display("new franchise",110,388,glovars.EASmall30,glovars.white)
    elif num_franchises == 2:
        selected_franchise = pygame.draw.rect(glovars.screen,glovars.black,(100,280,824,50),0)
        glovars.message_display("new franchise",110,288,glovars.EASmall30,glovars.white)
    elif num_franchises == 1:
        selected_franchise = pygame.draw.rect(glovars.screen,glovars.black,(100,180,824,50),0)
        glovars.message_display("new franchise",110,188,glovars.EASmall30,glovars.white)
    elif num_franchises == 0:
        selected_franchise = pygame.draw.rect(glovars.screen,glovars.black,(100,80,824,50),0)
        glovars.message_display("new franchise",110,88,glovars.EASmall30,glovars.white)

    pygame.draw.rect(glovars.screen,glovars.white,(698,80,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,180,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,280,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,380,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,480,226,50),0)

def runMenu():
    exitLoop = False

    initImages()

    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitLoop = 0
                pygame.quit()
                exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                    return mainmenu.runMenu()
                elif selected_franchise.collidepoint(pygame.mouse.get_pos()):
                    dfile = open("savedata.json", "r")
                    data = json.load(dfile)
                    dfile.close()
                    data["franchises"].append({"test":"test"})
                    dfile = open("savedata.json", "w")
                    json.dump(data, dfile)
                    dfile.close()
                    return franchisenew.runMenu(0)
        pygame.display.flip()