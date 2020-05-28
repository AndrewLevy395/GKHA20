import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import glovars
import mainmenu

def initImages():
    global backButtonClickCheck

    #background
    glovars.screen.blit(pygame.image.load("assets/images/storyModeBG.png"), (0,0))

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)
    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    #franchise select
    glovars.message_display("story select",748,19,glovars.teamSelectFont,glovars.black)

    #franchises to select background fill
    s1 = pygame.draw.rect(glovars.screen,glovars.black,(100,80,824,50),0)
    s2 = pygame.draw.rect(glovars.screen,glovars.black,(100,180,824,50),0)
    s3 = pygame.draw.rect(glovars.screen,glovars.black,(100,280,824,50),0)
    s4 = pygame.draw.rect(glovars.screen,glovars.black,(100,380,824,50),0)
    s5 = pygame.draw.rect(glovars.screen,glovars.black,(100,480,824,50),0)

    pygame.draw.rect(glovars.screen,glovars.white,(698,80,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,180,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,280,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,380,226,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(698,480,226,50),0)

    #franchise info
    glovars.message_display("new story",110,88,glovars.EASmall,glovars.white)
    glovars.message_display("new story",110,188,glovars.EASmall,glovars.white)
    glovars.message_display("new story",110,288,glovars.EASmall,glovars.white)
    glovars.message_display("new story",110,388,glovars.EASmall,glovars.white)
    glovars.message_display("new story",110,488,glovars.EASmall,glovars.white)


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
            if event.type == pygame.MOUSEBUTTONDOWN and backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                return mainmenu.runMenu()
        pygame.display.flip()