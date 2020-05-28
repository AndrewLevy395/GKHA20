import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import string

import glovars
import mainmenu
import franchiseload

def initImages():
    global backButtonClickCheck

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #fill in name
    pygame.draw.rect(glovars.screen,glovars.black,(328,96,367,50),0)

    pygame.draw.rect(glovars.screen,glovars.white,(324,92,375,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(324,146,375,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(324,96,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(695,96,4,50),0)

    #right arrow borders
    pygame.draw.rect(glovars.screen,glovars.white,(591,525,108,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(591,579,108,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(591,529,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(695,529,4,50),0)

    #left arrow borders
    pygame.draw.rect(glovars.screen,glovars.white,(324,525,108,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(324,579,108,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(324,529,4,50),0)
    pygame.draw.rect(glovars.screen,glovars.white,(428,529,4,50),0)

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)
    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

    #fill in arrows
    playerTeamLeft = pygame.draw.rect(glovars.screen,glovars.black,(328,529,100,50),0)
    playerTeamRight = pygame.draw.rect(glovars.screen,glovars.black,(595,529,100,50),0)

    #team select arrows
    glovars.screen.blit(pygame.image.load("assets/images/arrow.png"), (324,529))
    glovars.screen.blit(pygame.image.load("assets/images/arrowR.png"), (599,529))

    #franchise select
    glovars.message_display("new franchise",688,19,glovars.teamSelectFont,glovars.black)

def loopImages(selectedTeam, name_string):
    glovars.screen.blit(glovars.defaultTeams[selectedTeam].selectImage, (324,150))

    #fill in ovr
    pygame.draw.rect(glovars.screen,glovars.black,(534,480,90,45),0)
    glovars.message_display("OVR:",543,478,glovars.teamFont,glovars.white)
    glovars.message_display(str(glovars.defaultTeams[selectedTeam].overall),634,421,glovars.EALarge,glovars.white)

    #start button
    pygame.draw.rect(glovars.screen,glovars.white,(820,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(820,576,4,50),0)
    playButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/playButton.png"), (824,576))

    #name
    glovars.message_display("new franchise",332,98,glovars.teamSelectFont,glovars.white)


def runMenu(selectedTeam):

    exitLoop = False

    name_string = []

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
            if event.type == pygame.KEYDOWN:
                if event.key <= 127:
                    if len(name_string) < 10:
                        name_string.append(chr(event.key))
        seperator = ""
        sep_string = seperator.join(name_string)
        loopImages(selectedTeam, sep_string)
        pygame.display.flip()