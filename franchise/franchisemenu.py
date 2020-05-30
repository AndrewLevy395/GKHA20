import pygame

import glovars
from franchise import franchiseload
from franchise import phone

def loopImages():
    global menuplay, menuteam, menuleague

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #franchise name
    glovars.message_display("coach " + franchise_name + " of the " + franchise_team,40,20,glovars.teamSelectFont,glovars.black)

    #franchise season
    if int(franchise_season) >= 100:
        glovars.message_display("season " + franchise_season,800,575,glovars.teamSelectFont,glovars.black)
    elif int(franchise_season) >= 10:
        glovars.message_display("season " + franchise_season,820,575,glovars.teamSelectFont,glovars.black)
    else:
        glovars.message_display("season " + franchise_season,840,575,glovars.teamSelectFont,glovars.black)

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)

    #phone
    glovars.screen.blit(pygame.image.load("assets/images/phone.png"), (698,148))

    #highlights selected option and prints it's menu
    if selected_menu == 0:
        
        pygame.draw.rect(glovars.screen,glovars.white,(94,76,234,58),0) #selected

        #determine home and away team for next game
        hometeam = "Florida Tropics"
        awayteam = "Southside Spartans"

        #outline franchise images playing
        pygame.draw.rect(glovars.screen,glovars.white,(94,152,202,400),0)
        pygame.draw.rect(glovars.screen,glovars.white,(426,152,202,400),0)

        #draw franchise images playing
        for i in glovars.defaultTeams:
            if hometeam == i.name: 
                glovars.screen.blit(i.franchiseImage, (430,156))
            elif awayteam == i.name:
                glovars.screen.blit(i.franchiseImage, (98,156))

        #overall
        pygame.draw.rect(glovars.screen,glovars.black,(208,328,46,24),0)
        pygame.draw.rect(glovars.screen,glovars.black,(540,328,46,24),0)
        glovars.message_display("OVR:",544,327,glovars.teamFont20,glovars.white)
        glovars.message_display("OVR:",212,327,glovars.teamFont20,glovars.white)
        glovars.message_display(str(team_info[hometeam][0]["overall"]),591,297,glovars.EASmall50,glovars.white)
        glovars.message_display(str(team_info[awayteam][0]["overall"]),259,297,glovars.EASmall50,glovars.white)

        #play and sim buttons
        pygame.draw.rect(glovars.screen,glovars.white,(94,350,534,202),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)

        glovars.message_display("play game",110,506,glovars.teamFont30,glovars.white)
        glovars.message_display("sim game",375,506,glovars.teamFont30,glovars.white)

        #vs box
        pygame.draw.rect(glovars.screen,glovars.white,(328,225,70,50),0)
        pygame.draw.rect(glovars.screen,glovars.black,(332,229,62,42),0)
        glovars.message_display("vs.", 341, 229, glovars.teamSelectFont, glovars.white)
        
    elif selected_menu == 1:
        pygame.draw.rect(glovars.screen,glovars.white,(394,76,234,58),0) #selected

         #fill in outline borders for team options
        pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,156,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,156,261,194),0)

        #team options
        glovars.message_display("roster",110,308,glovars.teamFont30,glovars.white)
        glovars.message_display("coach",375,308,glovars.teamFont30,glovars.white)
        glovars.message_display("trade",110,506,glovars.teamFont30,glovars.white)
        glovars.message_display("free agents",375,506,glovars.teamFont30,glovars.white)

    elif selected_menu == 2:
        pygame.draw.rect(glovars.screen,glovars.white,(694,76,234,58),0) #selected

        #fill in outline borders for league options
        pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,156,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,156,261,194),0)

        #league options
        glovars.message_display("standings",110,308,glovars.teamFont30,glovars.white)
        glovars.message_display("stats",375,308,glovars.teamFont30,glovars.white)
        glovars.message_display("history",110,506,glovars.teamFont30,glovars.white)
        glovars.message_display("prestige",375,506,glovars.teamFont30,glovars.white)



    #fill menu options
    menuplay = pygame.draw.rect(glovars.screen,tintmenus[0],(98,80,226,50),0)
    menuteam = pygame.draw.rect(glovars.screen,tintmenus[1],(398,80,226,50),0)
    menuleague = pygame.draw.rect(glovars.screen,tintmenus[2],(698,80,226,50),0)

    #text on menu options
    glovars.message_display("next  game",132,88,glovars.EASmall30,glovars.white)
    glovars.message_display("team",473,88,glovars.EASmall30,glovars.white)
    glovars.message_display("league",763,88,glovars.EASmall30,glovars.white)


def runMenu(f, menu):
    global franchise_name, franchise_team, franchise_season, tintmenus, allmenus, selected_menu, team_info
    
    #play, team, league
    selected_menu = menu

    #get franchise info
    franchise_info = f["info"][0]
    franchise_name = str(franchise_info["name"])
    franchise_team = str(franchise_info["userteam"])
    franchise_season = str(franchise_info["season"])

    #get team info
    team_info = f["teamdata"][0]

    exitLoop = False
    allmenus = False
    appPressed = False
    
    loops = 315

    tintmenus = [glovars.black, glovars.black, glovars.black]

    loopImages()

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
                if menuplay.collidepoint(pygame.mouse.get_pos()):
                    selected_menu = 0
                if menuteam.collidepoint(pygame.mouse.get_pos()):
                    selected_menu = 1
                if menuleague.collidepoint(pygame.mouse.get_pos()):
                    selected_menu = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    appPressed = not appPressed
                    loops = 0
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

        if appPressed:
            phone.drawApp(loops)
        else:
            phone.closeApp(loops)
        if loops < 315:
            loops += 20
        if loops > 315:
            loops = 315

        pygame.display.flip()