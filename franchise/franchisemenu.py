import pygame

import glovars
from franchise import franchiseload

def initImages():
    
    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #franchise name
    glovars.message_display("coach " + franchise_name + " of the " + franchise_team,40,20,glovars.teamSelectFont,glovars.black)

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)

def loopImages():
    global menuplay, menuteam, menuleague

    #phone
    glovars.screen.blit(pygame.image.load("assets/images/phone.png"), (698,148))

    #highlights selected option and prints it's menu
    if selected_menu == 0:
        pygame.draw.rect(glovars.screen,glovars.white,(94,76,234,58),0) #selected

        #outline franchise images
        pygame.draw.rect(glovars.screen,glovars.white,(94,152,202,400),0)
        pygame.draw.rect(glovars.screen,glovars.white,(426,152,202,400),0)

        #draw franchise images
        glovars.screen.blit(glovars.defaultTeams[4].franchiseImage, (98,156))
        glovars.screen.blit(glovars.defaultTeams[0].franchiseImage, (430,156))

        #overall
        pygame.draw.rect(glovars.screen,glovars.black,(208,328,46,24),0)
        pygame.draw.rect(glovars.screen,glovars.black,(540,328,46,24),0)
        glovars.message_display("OVR:",544,327,glovars.teamFontSmall,glovars.white)
        glovars.message_display("OVR:",212,327,glovars.teamFontSmall,glovars.white)
        glovars.message_display(str(glovars.defaultTeams[0].overall),591,297,glovars.EASmall50,glovars.white)
        glovars.message_display(str(glovars.defaultTeams[4].overall),259,297,glovars.EASmall50,glovars.white)

        #play and sim
        pygame.draw.rect(glovars.screen,glovars.white,(94,350,534,202),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)

        #vs box
        pygame.draw.rect(glovars.screen,glovars.white,(328,225,70,50),0)
        pygame.draw.rect(glovars.screen,glovars.black,(332,229,62,42),0)
        glovars.message_display("vs.", 341, 229, glovars.teamSelectFont, glovars.white)
        
    elif selected_menu == 1:
        pygame.draw.rect(glovars.screen,glovars.white,(394,76,234,58),0)
    elif selected_menu == 2:
        pygame.draw.rect(glovars.screen,glovars.white,(694,76,234,58),0)

    #fill menu options
    menuplay = pygame.draw.rect(glovars.screen,tintmenus[0],(98,80,226,50),0)
    menuteam = pygame.draw.rect(glovars.screen,tintmenus[1],(398,80,226,50),0)
    menuleague = pygame.draw.rect(glovars.screen,tintmenus[2],(698,80,226,50),0)

    #text on menu options
    glovars.message_display("next  game",132,88,glovars.EASmall30,glovars.white)
    glovars.message_display("team",473,88,glovars.EASmall30,glovars.white)
    glovars.message_display("league",763,88,glovars.EASmall30,glovars.white)



def runMenu(f, menu):
    global franchise_name, franchise_team, tintmenus, allmenus, selected_menu
    
    selected_menu = menu
    franchise_info = f["info"][0]
    franchise_name = str(franchise_info["name"])
    franchise_team = str(franchise_info["team"])
    exitLoop = False
    allmenus = False

    tintmenus = [glovars.black, glovars.black, glovars.black]

    initImages()

    backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

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
            if allmenus:
                for i in range(3):
                    if allmenus[i].collidepoint(pygame.mouse.get_pos()):
                        tintmenus[i] = glovars.blackTint
                    else: 
                        tintmenus[i] = glovars.black
        loopImages()
        allmenus = [menuplay, menuteam, menuleague]
        if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButtonHover.png"), (0,576))
        else:
            backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))
        pygame.display.flip()