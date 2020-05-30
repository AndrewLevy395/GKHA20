import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import json

import glovars
import mainmenu
from franchise import franchisenew
from franchise import franchisemenu

def initImages():
    global backButtonClickCheck, franchises, num_franchises

    data = open("savedata.json", "r")
    franchises = json.load(data)["franchises"]
    num_franchises = len(franchises)
    data.close()

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)

    #franchise select
    glovars.message_display("franchise select",668,19,glovars.teamSelectFont,glovars.black)

def loopImages(tint):
    global selected_franchise, loadFranchise

    loadFranchise = [False] * 5

    if tint == True:
        newColor = glovars.blackTint
    else:
        newColor = glovars.black

    #franchises that cannot be selected
    if num_franchises < 5:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,480,824,50),0)
    if num_franchises < 4:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,380,824,50),0)
    if num_franchises < 3:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,280,824,50),0)
    if num_franchises < 2:
        pygame.draw.rect(glovars.screen,glovars.grey,(100,180,824,50),0)

    #franchises that can be selected as new
    if num_franchises == 5:
        selected_franchise = False
    elif num_franchises == 4:
        selected_franchise = pygame.draw.rect(glovars.screen,newColor,(100,480,598,50),0)
        glovars.message_display("new franchise",110,488,glovars.EASmall30,glovars.white)
    elif num_franchises == 3:
        selected_franchise = pygame.draw.rect(glovars.screen,newColor,(100,380,598,50),0)
        glovars.message_display("new franchise",110,388,glovars.EASmall30,glovars.white)
    elif num_franchises == 2:
        selected_franchise = pygame.draw.rect(glovars.screen,newColor,(100,280,598,50),0)
        glovars.message_display("new franchise",110,288,glovars.EASmall30,glovars.white)
    elif num_franchises == 1:
        selected_franchise = pygame.draw.rect(glovars.screen,newColor,(100,180,598,50),0)
        glovars.message_display("new franchise",110,188,glovars.EASmall30,glovars.white)
    elif num_franchises == 0:
        selected_franchise = pygame.draw.rect(glovars.screen,newColor,(100,80,598,50),0)
        glovars.message_display("new franchise",110,88,glovars.EASmall30,glovars.white)

    #white boxes where scorebugs are
    pygame.draw.rect(glovars.screen,glovars.white,(698,80,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,180,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,280,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,380,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,480,226,50),0)

    
    #franchises that can be selected to load
    if num_franchises > 0:
        loadFranchise[0] = pygame.draw.rect(glovars.screen,glovars.white,(100,80,824,50),0)
        glovars.message_display("coach  " + str(franchises[0]["info"][0]["name"]),110,88,glovars.EASmall30,glovars.black)
        printScoreBug(0, 698, 80)
    if num_franchises > 1:
        loadFranchise[1] = pygame.draw.rect(glovars.screen,glovars.white,(100,180,824,50),0)
        glovars.message_display("coach  " + str(franchises[1]["info"][0]["name"]),110,188,glovars.EASmall30,glovars.black)
        printScoreBug(1, 698, 180)
    if num_franchises > 2:
        loadFranchise[2] = pygame.draw.rect(glovars.screen,glovars.white,(100,280,824,50),0)
        glovars.message_display("coach  " + str(franchises[2]["info"][0]["name"]),110,288,glovars.EASmall30,glovars.black)
        printScoreBug(2, 698, 280)
    if num_franchises > 3:
        loadFranchise[3] = pygame.draw.rect(glovars.screen,glovars.white,(100,380,824,50),0)
        glovars.message_display("coach  " + str(franchises[3]["info"][0]["name"]),110,388,glovars.EASmall30,glovars.black)
        printScoreBug(3, 698, 380)
    if num_franchises > 4:
        loadFranchise[4] = pygame.draw.rect(glovars.screen,glovars.white,(100,480,824,50),0)
        glovars.message_display("coach  " + str(franchises[4]["info"][0]["name"]),110,488,glovars.EASmall30,glovars.black)
        printScoreBug(4, 698, 480)

def printScoreBug(fnum, x, y):
    for i in glovars.defaultTeams:
        if i.name == str(franchises[fnum]["info"][0]["team"]):
            glovars.screen.blit(i.scorebug, (x,y))

def drawSlot(fnum, color):
    location = 80 + (100 * fnum)
    pygame.draw.rect(glovars.screen,color,(100,location,824,50),0)


def runMenu():
    global selected_franchise
    exitLoop = False
    tint = False
    selected_franchise = False

    initImages()

    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitLoop = 0
                pygame.quit()
                exit()
                break
            if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButtonHover.png"), (0,576))
            else:
                backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                    return mainmenu.runMenu()
                if selected_franchise:
                    if selected_franchise.collidepoint(pygame.mouse.get_pos()):
                        return franchisenew.runMenu(0)
                for i in range(len(loadFranchise)):
                    if loadFranchise[i]:
                        if loadFranchise[i].collidepoint(pygame.mouse.get_pos()):
                            return franchisemenu.runMenu(franchises[i], 0)
            if selected_franchise:
                if selected_franchise.collidepoint(pygame.mouse.get_pos()):
                    tint = True
                else: tint = False
        loopImages(tint)
        pygame.display.flip()