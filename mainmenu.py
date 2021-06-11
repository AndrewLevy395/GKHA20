from os import path
import pygame
import time
import random
import json

import glovars
import playnowmenu
from franchise import franchiseload
from storymode import storyload


#initialize main menu images
def initImages():
    
    glovars.screen.fill(glovars.black) #background

    #panels when hovering over
    hovers[0] = (pygame.image.load("assets/images/playNow.png"))
    hovers[1] = (pygame.image.load("assets/images/franchise.png"))
    hovers[2] = (pygame.image.load("assets/images/storyMode.png"))
    hovers[3] = (pygame.image.load("assets/images/extras.png"))
    hovers[4] = (pygame.image.load("assets/images/settings.png"))
    hovers[5] = (pygame.image.load("assets/images/credits.png"))
    
    #blurred panels when not hovering over
    blurs[0] = (pygame.image.load("assets/images/playNowBlur.png"))
    blurs[1] = (pygame.image.load("assets/images/franchiseBlur.png"))
    blurs[2] = (pygame.image.load("assets/images/storyModeBlur.png"))
    blurs[3] = (pygame.image.load("assets/images/extrasBlur.png"))
    blurs[4] = (pygame.image.load("assets/images/settingsBlur.png"))
    blurs[5] = (pygame.image.load("assets/images/creditsBlur.png"))

    #list of all background images
    BG1 = pygame.image.load("assets/images/BG1.png")
    BG2 = pygame.image.load("assets/images/BG2.jpg")
    BG3 = pygame.image.load("assets/images/BG3.jpg")
    BG4 = pygame.image.load("assets/images/BG4.jpg")
    BG5 = pygame.image.load("assets/images/BG5.jpg")
    BG6 = pygame.image.load("assets/images/BG6.jpg")
    BG7 = pygame.image.load("assets/images/BG7.jpg")
    BG8 = pygame.image.load("assets/images/BG8.jpg")
    BG9 = pygame.image.load("assets/images/BG9.jpg")
    BGA = pygame.image.load("assets/images/BGA.png")
    BGB = pygame.image.load("assets/images/BGB.png")
    BGC = pygame.image.load("assets/images/BGC.png")
    BGD = pygame.image.load("assets/images/BGD.png")
    BGE = pygame.image.load("assets/images/BGE.png")
    BGF = pygame.image.load("assets/images/BGF.png")
    BGG = pygame.image.load("assets/images/BGG.png")
    BGH = pygame.image.load("assets/images/BGH.png")
    BGI = pygame.image.load("assets/images/BGI.png")

    global bglist
    bglist = [BG1,BG2,BG3,BG4,BG5,BG6,BG7,BG8,BG9,BGA,BGB,BGC,BGD,BGE,BGF,BGG,BGH,BGI]

    #gkha20 logo
    glovars.screen.blit(pygame.image.load("assets/images/gkha20Main.png"), (342, 0))


#draw borders
def initBorders():
    pygame.draw.rect(glovars.screen,glovars.black,(0,0,1024,4),0)
    pygame.draw.rect(glovars.screen,glovars.black,(0,207,1024,4),0)
    pygame.draw.rect(glovars.screen,glovars.black,(0,416,1024,4),0)
    pygame.draw.rect(glovars.screen,glovars.black,(0,622,1024,4),0)
    pygame.draw.rect(glovars.screen,glovars.black,(0,0,4,626),0)
    pygame.draw.rect(glovars.screen,glovars.black,(340,0,4,626),0)
    pygame.draw.rect(glovars.screen,glovars.black,(682,0,4,626),0)
    pygame.draw.rect(glovars.screen,glovars.black,(1020,0,4,626),0)


#initializes and runs menu loop
def runMenu():

    #check for save data
    if(not path.exists("savedata.json")):
        data = {}
        data["franchises"] = []
        data["stories"] = []
        data["codes"] = []
        dfile = open("savedata.json", "w")
        json.dump(data, dfile)
        dfile.close()
    
    #all game data
    rfile = open("savedata.json", "r")
    rdata = json.load(rfile)
    rfile.close()

    nextmenu = -1
    exitLoop = False
    click = False

    global hovers, blurs
    hovers = [None] * 6
    blurs = [None] * 6
    location = [(0,0),(0,209),(0,418),(684,0),(684,209),(684,418)]

    wait = False
    background = None

    initImages()

    menuStartTime = time.perf_counter() #keep track of time passed
    menuElapsedTime = 0
    menuTotalTime = 0

    #menu loop
    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitLoop = 0
                pygame.quit()
                exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        if background == None:
            background = random.choice(bglist)
            wait = True
        glovars.screen.blit(background, (342, 209))
        for i in range(len(blurs)):
            hoverCheck = glovars.screen.blit(blurs[i], location[i])
            if hoverCheck.collidepoint(pygame.mouse.get_pos()):
                glovars.screen.blit(hovers[i],location[i])
                if click == True:
                    nextmenu = i
        
        initBorders()
    
        pygame.display.flip()

        if int(menuTotalTime) % 4 == 0 and wait == False:
            background = None
        elif int(menuTotalTime) % 4 == 1:
            wait = False
        menuElapsedTime = time.perf_counter()
        menuTotalTime = menuElapsedTime - menuStartTime
        if(nextmenu == 0):
            return playnowmenu.runMenu(0,1,rdata["codes"])
        if(nextmenu == 1):
            return franchiseload.runMenu()
        if(nextmenu == 2):
            return storyload.runMenu()
        click = False