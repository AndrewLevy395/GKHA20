import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import glovars
import defaultTeam
import mainmenu
import gameplay

def initImages():
    global computerTeamLeft, computerTeamInfo, computerTeamRight, playerTeamLeft, playerTeamInfo, playerTeamRight, backButtonClickCheck, playButtonClickCheck

    #background
    glovars.screen.blit(pygame.image.load("assets/images/playNowDrop.jpg"), (0,0))

    #player team info border
    pygame.draw.rect(glovars.screen,glovars.white,(926,112,38,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(926,146,38,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(960,116,4,30),0)
    pygame.draw.rect(glovars.screen,glovars.white,(926,116,4,30),0)

    #player team arrow border
    pygame.draw.rect(glovars.screen,glovars.white,(589,92,212,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(589,146,212,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(589,96,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(797,96,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(693,96,4,50),0)

    #opposing team info border
    pygame.draw.rect(glovars.screen,glovars.white,(223,92,212,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(223,146,212,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(223,96,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(431,96,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(327,96,4,50),0)

    #opposing team arrow border
    pygame.draw.rect(glovars.screen,glovars.white,(60,112,38,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(60,146,38,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(60,116,4,30),0)
    pygame.draw.rect(glovars.screen,glovars.white,(94,116,4,30),0)

    #fill in player team arrows and info
    playerTeamLeft = pygame.draw.rect(glovars.screen,glovars.black,(593,96,100,50),0)
    playerTeamInfo = pygame.draw.rect(glovars.screen,glovars.black,(930,116,30,30),0)
    playerTeamRight = pygame.draw.rect(glovars.screen,glovars.black,(697,96,100,50),0)
    glovars.screen.blit(pygame.image.load("assets/images/arrow.png"), (595,96))
    glovars.screen.blit(pygame.image.load("assets/images/arrowR.png"), (699,96))
    glovars.message_display("i",941,121,glovars.ESPNSmall,glovars.white)

    #fill in computer team arrows and info
    computerTeamLeft = pygame.draw.rect(glovars.screen,glovars.black,(227,96,100,50),0)
    computerTeamInfo = pygame.draw.rect(glovars.screen,glovars.black,(64,116,30,30),0)
    computerTeamRight = pygame.draw.rect(glovars.screen,glovars.black,(331,96,100,50),0)
    glovars.screen.blit(pygame.image.load("assets/images/arrow.png"), (229,96))
    glovars.screen.blit(pygame.image.load("assets/images/arrowR.png"), (333,96))
    glovars.message_display("i",75,121,glovars.ESPNSmall,glovars.white)

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)
    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    #play button
    pygame.draw.rect(glovars.screen,glovars.white,(820,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(820,576,4,50),0)
    playButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/playButton.png"), (824,576))

    #team select
    glovars.message_display("team select",748,19,glovars.teamSelectFont,glovars.white)

def loopImages(listPlayer, listComputer):
    glovars.screen.blit(glovars.defaultTeams[listPlayer].selectImage, (589,150))
    glovars.screen.blit(glovars.defaultTeams[listComputer].selectImage, (60,150))

    #fill in ovr
    pygame.draw.rect(glovars.screen,glovars.black,(270,480,90,45),0)
    pygame.draw.rect(glovars.screen,glovars.black,(799,480,90,45),0)
    glovars.message_display("OVR:",279,478,glovars.teamFont,glovars.white)
    glovars.message_display("OVR:",808,478,glovars.teamFont,glovars.white)
    glovars.message_display(str(glovars.defaultTeams[listComputer].overall),370,421,glovars.EALarge,glovars.white)
    glovars.message_display(str(glovars.defaultTeams[listPlayer].overall),899,421,glovars.EALarge,glovars.white)

    #mouse image to signify player controlled
    pygame.draw.rect(glovars.screen,glovars.black,(589,425,75,100),0)
    glovars.screen.blit(pygame.image.load("assets/images/mouse.png"), (587,425))

def runMenu(listPlayer, listComputer):
    nextmenu = -1
    exitLoop = False

    initImages()

    while not exitLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitLoop = 0
                pygame.quit()
                exit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN and computerTeamRight.collidepoint(pygame.mouse.get_pos()):
                listComputer += 1
                if listComputer >= len(glovars.defaultTeams):
                    listComputer = 0
            if event.type == pygame.MOUSEBUTTONDOWN and computerTeamLeft.collidepoint(pygame.mouse.get_pos()):
                listComputer -= 1
                if listComputer < 0:
                    listComputer = len(glovars.defaultTeams) - 1
            if event.type == pygame.MOUSEBUTTONDOWN and playerTeamRight.collidepoint(pygame.mouse.get_pos()):
                listPlayer += 1
                if listPlayer >= len(glovars.defaultTeams):
                    listPlayer = 0
            if event.type == pygame.MOUSEBUTTONDOWN and playerTeamLeft.collidepoint(pygame.mouse.get_pos()):
                listPlayer -= 1
                if listPlayer < 0:
                    listPlayer = len(glovars.defaultTeams) - 1
            if event.type == pygame.MOUSEBUTTONDOWN and backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                return mainmenu.runMenu()
            if event.type == pygame.MOUSEBUTTONDOWN and playButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                return gameplay.knockeyGame(glovars.defaultTeams[listPlayer], glovars.defaultTeams[listComputer])
        loopImages(listPlayer, listComputer)
        pygame.display.flip()