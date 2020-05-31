import pygame

import glovars
from franchise import franchiseload
from franchise import phone
import logic

def determineTeams(f):
    #determines the home and away teams of the next user game
    day = f["info"][0]["day"]
    daygames = f["schedule"][int(day)]
    for i in daygames:
        for j in i:
            if glovars.defaultTeams[j].name == f["info"][0]["userteam"]:
                return i

def loopImages(f):
    global menuplay, menuteam, menuleague, leagueOptionsButtons

    #background
    glovars.screen.blit(pygame.image.load("assets/images/franchiseBG.png"), (0,0))

    #franchise name
    glovars.message_display("coach " + str(f["info"][0]["name"]) + " of the " + str(f["info"][0]["userteam"]),40,20,glovars.teamSelectFont,glovars.black)

    #franchise season
    if int(str(f["info"][0]["season"])) >= 100:
        glovars.message_display("season " + str(f["info"][0]["season"]),800,575,glovars.teamSelectFont,glovars.black)
    elif int(str(f["info"][0]["season"])) >= 10:
        glovars.message_display("season " + str(f["info"][0]["season"]),820,575,glovars.teamSelectFont,glovars.black)
    else:
        glovars.message_display("season " + str(f["info"][0]["season"]),840,575,glovars.teamSelectFont,glovars.black)

    #back button
    pygame.draw.rect(glovars.screen,glovars.white,(0,572,204,4),0)
    pygame.draw.rect(glovars.screen,glovars.white,(200,576,4,50),0)

    #phone
    glovars.screen.blit(pygame.image.load("assets/images/phone.png"), (698,148))

    # PLAY MENU
    if selected_menu == 0:
        
        pygame.draw.rect(glovars.screen,glovars.white,(94,76,234,58),0) #selected

        #determine home and away team for next game
        hometeam = glovars.defaultTeams[determineTeams(f)[1]].name
        awayteam = glovars.defaultTeams[determineTeams(f)[0]].name

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
        glovars.message_display(str(f["teamdata"][0][hometeam][0]["overall"]),591,297,glovars.EASmall50,glovars.white)
        glovars.message_display(str(f["teamdata"][0][awayteam][0]["overall"]),259,297,glovars.EASmall50,glovars.white)

        #play and sim buttons
        pygame.draw.rect(glovars.screen,glovars.white,(94,350,534,202),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)

        #displays text based on week
        if f["info"][0]["day"] == 0:
            glovars.message_display("play",110,471,glovars.teamFont30,glovars.white)
            glovars.message_display("preseason",110,506,glovars.teamFont30,glovars.white)
            glovars.message_display("sim",375,471,glovars.teamFont30,glovars.white)
            glovars.message_display("preseason",375,506,glovars.teamFont30,glovars.white)
        else:
            glovars.message_display("play game " + str(f["info"][0]["day"]),110,506,glovars.teamFont30,glovars.white)
            glovars.message_display("sim game " + str(f["info"][0]["day"]),375,506,glovars.teamFont30,glovars.white)

        #vs box
        pygame.draw.rect(glovars.screen,glovars.white,(328,225,70,50),0)
        pygame.draw.rect(glovars.screen,glovars.black,(332,229,62,42),0)
        glovars.message_display("vs.", 341, 229, glovars.teamSelectFont, glovars.white)
        
    # TEAM MENU
    if selected_menu == 1:
        pygame.draw.rect(glovars.screen,glovars.white,(394,76,234,58),0) #selected

         #fill in outline borders for team options
        pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(98,156,261,194),0)
        pygame.draw.rect(glovars.screen,glovars.black,(363,156,261,194),0)

        #team options
        glovars.message_display("roster",110,308,glovars.teamFont30,glovars.white)
        glovars.message_display("schedule",375,308,glovars.teamFont30,glovars.white)
        glovars.message_display("trade",110,506,glovars.teamFont30,glovars.white)
        glovars.message_display("free agents",375,506,glovars.teamFont30,glovars.white)

    #default all leagueOptions and league buttons to false
    leagueOptionsButtons = [False] * 4

    # LEAGUE MENU
    if selected_menu == 2:
        pygame.draw.rect(glovars.screen,glovars.white,(694,76,234,58),0) #selected

        if leagueOptions == "menu":
            #fill in outline borders for league options
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            leagueOptionsButtons[2] = pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
            leagueOptionsButtons[3] = pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)
            leagueOptionsButtons[0] = pygame.draw.rect(glovars.screen,glovars.black,(98,156,261,194),0)
            leagueOptionsButtons[1] = pygame.draw.rect(glovars.screen,glovars.black,(363,156,261,194),0)

            #league options
            glovars.message_display("standings",110,308,glovars.teamFont30,glovars.white)
            glovars.message_display("stats",375,308,glovars.teamFont30,glovars.white)
            glovars.message_display("history",110,506,glovars.teamFont30,glovars.white)
            glovars.message_display("prestige",375,506,glovars.teamFont30,glovars.white)

        # STANDINGS
        elif leagueOptions == "standings":
            
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)
            glovars.message_display("standings",116,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("w",375,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("l",446,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("ol",503,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("p",575,180,glovars.teamFont30,glovars.googusGreen)
 
            order = logic.calculateRankings(f)
            for i in range(len(order)):
                glovars.message_display(order[i]["mascot"],116,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(order[i]["points"]),575,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(f["teamdata"][0][order[i]["name"]][0]["wins"]),375,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(f["teamdata"][0][order[i]["name"]][0]["losses"]),446,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(f["teamdata"][0][order[i]["name"]][0]["overtimelosses"]),512,240 + (i * 50),glovars.teamFont30,glovars.white)

        # STATS
        elif leagueOptions == "stats":
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
        # HISTORY
        elif leagueOptions == "history":
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
        # PRESTIGE
        elif leagueOptions == "prestige":
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)


    #fill menu options
    menuplay = pygame.draw.rect(glovars.screen,tintmenus[0],(98,80,226,50),0)
    menuteam = pygame.draw.rect(glovars.screen,tintmenus[1],(398,80,226,50),0)
    menuleague = pygame.draw.rect(glovars.screen,tintmenus[2],(698,80,226,50),0)

    #text on menu options
    glovars.message_display("next  game",132,88,glovars.EASmall30,glovars.white)
    glovars.message_display("team",473,88,glovars.EASmall30,glovars.white)
    glovars.message_display("league",763,88,glovars.EASmall30,glovars.white)


def runMenu(f, menu):
    global tintmenus, allmenus, selected_menu, leagueOptions

    #play, team, league
    selected_menu = menu

    exitLoop = False #exit game

    allmenus = False #all top level menus (play, team, league)- defaults to false
    tintmenus = [glovars.black, glovars.black, glovars.black] #tint color for all menus

    appPressed = False #if an app is pressed on phone 
    loops = 315 #number of loops - defaults to maximun when no app is pressed

    loopImages(f)

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
                    leagueOptions = "menu"
                for i in range(len(leagueOptionsButtons)):
                    if leagueOptionsButtons[i] != False:
                        if leagueOptionsButtons[0].collidepoint(pygame.mouse.get_pos()):
                            leagueOptions = "standings"
                        if leagueOptionsButtons[1].collidepoint(pygame.mouse.get_pos()):
                            leagueOptions = "stats"
                        if leagueOptionsButtons[2].collidepoint(pygame.mouse.get_pos()):
                            leagueOptions = "history"
                        if leagueOptionsButtons[3].collidepoint(pygame.mouse.get_pos()):
                            leagueOptions = "prestige"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    appPressed = not appPressed
                    loops = 0
            #check for allmenus tint
            if allmenus:
                for i in range(3):
                    if allmenus[i].collidepoint(pygame.mouse.get_pos()):
                        tintmenus[i] = glovars.blackTint
                    else: 
                        tintmenus[i] = glovars.black
        loopImages(f)
        allmenus = [menuplay, menuteam, menuleague]
        if backButtonClickCheck.collidepoint(pygame.mouse.get_pos()):
                backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButtonHover.png"), (0,576))
        else:
            backButtonClickCheck = glovars.screen.blit(pygame.image.load("assets/images/backButton.png"), (0,576))

        #phone open and close apps
        if appPressed:
            phone.drawApp(loops)
        else:
            phone.closeApp(loops)

        #adjust loops when phone opens or closes apps
        if loops < 315:
            loops += 20
        if loops > 315:
            loops = 315

        pygame.display.flip()