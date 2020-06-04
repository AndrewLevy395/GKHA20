import pygame
import string
import json

import glovars
import mainmenu
from franchise import franchiseload
from franchise import franchisemenu
from franchise import schedule

def loopImages(selectedTeam, name_string, franchises):
    global backButtonClickCheck, playerTeamRight, playerTeamLeft

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #name border
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

    #fill in arrows
    playerTeamLeft = pygame.draw.rect(glovars.screen,glovars.black,(328,529,100,50),0)
    playerTeamRight = pygame.draw.rect(glovars.screen,glovars.black,(595,529,100,50),0)

    #team select arrows
    glovars.screen.blit(pygame.image.load("assets/images/arrow.png"), (324,529))
    glovars.screen.blit(pygame.image.load("assets/images/arrowR.png"), (599,529))

    #franchise select
    glovars.message_display("new franchise",688,19,glovars.teamSelectFont,glovars.black)
    glovars.screen.blit(glovars.defaultTeams[selectedTeam].selectImage, (324,150))

    #fill in ovr
    pygame.draw.rect(glovars.screen,glovars.black,(534,480,90,45),0)
    glovars.message_display("OVR:",543,478,glovars.teamFont40,glovars.white)
    glovars.message_display(str(glovars.defaultTeams[selectedTeam].overall),634,421,glovars.EALarge,glovars.white)

    #fill in name
    pygame.draw.rect(glovars.screen,glovars.black,(328,96,367,50),0)

    #variables for play button
    duplicate = False
    playButtonClickCheck = False

    #check if name is valid
    for i in range(len(franchises)):
        if franchises[i]["info"][0]["name"] == name_string:
            duplicate = True

    #display name and play button
    if len(name_string) > 0:
        #start button
        glovars.message_display(name_string,338,100,glovars.teamSelectFont,glovars.white)
        if not duplicate:
            pygame.draw.rect(glovars.screen,glovars.white,(820,572,204,4),0)
            pygame.draw.rect(glovars.screen,glovars.white,(820,576,4,50),0)
            playButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/playButton.png"), (824,576))
    else:
        #name text
        glovars.message_display("type name:",338,100,glovars.teamSelectFont,glovars.white)
    
    return playButtonClickCheck
        

def runMenu(selectedTeam, franchises):

    exitLoop = False

    name_string = []

    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))
    playButtonClickCheck = False

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
                if playButtonClickCheck != False:
                    if playButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                        rfile = open("savedata.json", "r")
                        data = json.load(rfile)
                        rfile.close()
                        data["franchises"].append({"info":[{"name":sep_string,"userteam":glovars.defaultTeams[selectedTeam].name, "season": 8, "day": 0, "freeAgentMoves": 3}], 
                        "teamdata":glovars.franchiseTeamData, "schedule": schedule.createSchedule(10), "results":[],
                        "playerdata": glovars.franchisePlayerData, "freeagents": glovars.franchiseFreeAgents})
                        wfile = open("savedata.json", "w")
                        json.dump(data, wfile)
                        wfile.close()
                        rfile = open("savedata.json", "r")
                        franchises = json.load(rfile)["franchises"]
                        num_franchises = len(franchises)
                        rfile.close()
                        franchisemenu.runMenu(0, num_franchises - 1)
            if event.type == pygame.KEYDOWN:
                if event.key <= 122 and event.key >= 97:
                    if len(name_string) < 15:
                        name_string.append(chr(event.key))
                if event.key <= 57 and event.key >= 48:
                    if len(name_string) < 15:
                        name_string.append(chr(event.key))
                if event.key == pygame.K_BACKSPACE:
                    if len(name_string) > 0:
                        name_string.pop()
                if event.key == pygame.K_SPACE:
                    if len(name_string) < 14:
                        name_string.append(chr(event.key))
            if event.type == pygame.MOUSEBUTTONDOWN and playerTeamRight.collidepoint(pygame.mouse.get_pos()):
                selectedTeam += 1
                if selectedTeam >= len(glovars.defaultTeams):
                    selectedTeam = 0
            if event.type == pygame.MOUSEBUTTONDOWN and playerTeamLeft.collidepoint(pygame.mouse.get_pos()):
                selectedTeam -= 1
                if selectedTeam < 0:
                    selectedTeam = len(glovars.defaultTeams) - 1
            
        seperator = ""
        sep_string = seperator.join(name_string)
        playButtonClickCheck = loopImages(selectedTeam, sep_string, franchises)
        if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButtonHover.png"), (0,576))
        else:
            backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))
        if playButtonClickCheck:
            if playButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                playButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/playButtonHover.png"), (824,576))
            else:
                playButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/playButton.png"), (824,576))
        pygame.display.flip()