import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import glovars
import mainmenu
import franchiseload

def initImages():
    global backButtonClickCheck

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)
    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    #franchise select
    glovars.message_display("new franchise",688,19,glovars.teamSelectFont,glovars.black)

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
                    return franchiseload.runMenu()
        pygame.display.flip()