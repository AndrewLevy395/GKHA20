import pygame
import json

import glovars
from franchise import franchiseload
from franchise import phone
import logic

def determineTeams(f):
    #determines the home and away teams of the next user game
    daygames = f["schedule"][int(day)]
    for i in daygames:
        for j in i:
            if glovars.defaultTeams[j].name == f["info"][0]["userteam"]:
                return i

def loopImages(data):
    global menuplay, menuteam, menuleague, leagueOptionsButtons, teamOptionsButtons, left_observe, right_observe, moveButtons

    #this franchise
    f = data["franchises"][fnum]

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

    # NEXT GAME MENU
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
        
    #default all teamOptions and team buttons to false
    teamOptionsButtons = [False] * 6
    
    #create moveButtons
    moveButtons = [False, False, False]

    #default no schedule being observed
    left_observe = False
    right_observe = False
    
    # TEAM MENU
    if selected_menu == 1:
        pygame.draw.rect(glovars.screen,glovars.white,(394,76,234,58),0) #selected

        # QUAD BOX MENU
        if teamOptions == "menu":
            #fill in outline borders for team options
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            teamOptionsButtons[2] = pygame.draw.rect(glovars.screen,glovars.black,(98,354,261,194),0)
            teamOptionsButtons[3] = pygame.draw.rect(glovars.screen,glovars.black,(363,354,261,194),0)
            teamOptionsButtons[0] = pygame.draw.rect(glovars.screen,glovars.black,(98,156,261,194),0)
            teamOptionsButtons[1] = pygame.draw.rect(glovars.screen,glovars.black,(363,156,261,194),0)

            #team options
            glovars.message_display("roster",110,308,glovars.teamFont30,glovars.white)
            glovars.message_display("schedule",375,308,glovars.teamFont30,glovars.white)
            glovars.message_display("trade",110,506,glovars.teamFont30,glovars.white)
            glovars.message_display("free agents",375,506,glovars.teamFont30,glovars.white)

        # ROSTER 
        elif teamOptions == "roster":

            #background
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)

            switchColor = [glovars.black, glovars.black, glovars.black]

            #display roster
            glovars.message_display("roster - " + glovars.defaultTeams[playerTeam].name.split(' ', 1)[1],116,180,glovars.teamFont30,glovars.googusGreen)

            #display names and position inside boxes of correct color
            offPlayer = f["teamdata"][0][glovars.defaultTeams[playerTeam].name][0]["offense"]
            defPlayer = f["teamdata"][0][glovars.defaultTeams[playerTeam].name][0]["defense"]
            goalPlayer = f["teamdata"][0][glovars.defaultTeams[playerTeam].name][0]["goalie"]
            players = [offPlayer, defPlayer, goalPlayer]
            positions = ["off", "def", "goa"]
            for i in range(3):
                if selected_move == i:
                    for j in range(3):
                        if j != i:
                            switchColor[j] = glovars.red
                    moveColor = glovars.googusGreen
                else:
                    moveColor = glovars.black
                pygame.draw.rect(glovars.screen,glovars.white,(120,254 + (100 * i),354,58),0)
                pygame.draw.rect(glovars.screen,moveColor,(124,258 + (100 * i),346,50),0)
                pygame.draw.rect(glovars.screen,glovars.white,(470,254 + (100 * i),130,58),0)
                glovars.message_display(positions[i] + ": " + players[i],130,264 + (100 * i),glovars.teamFont30,glovars.white)

            #define the message in roster and print it with the correct color
            if selected_move != None:
                moveMessage = "here"
            else:
                moveMessage = "move"
            for i in range(3):
                moveButtons[i] = pygame.draw.rect(glovars.screen,switchColor[i],(474,258 + (100 * i),122,50),0)
                glovars.message_display(moveMessage,495,264 + (100 * i),glovars.teamFont30,glovars.white)

        # SCHEDULE
        elif teamOptions == "schedule":

            #set the matchup observed
            matchup = page_observe

            #background
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)

            #rotate through matchup being observed
            pygame.draw.rect(glovars.screen,glovars.white,(294,548,334,50),0)
            pygame.draw.rect(glovars.screen,glovars.black,(298,552,326,42),0)
            pygame.draw.rect(glovars.screen,glovars.white,(516,548,112,50),0)
            left_observe = pygame.draw.rect(glovars.screen,glovars.black,(520,552,50,42),0)
            right_observe = pygame.draw.rect(glovars.screen,glovars.black,(574,552,50,42),0)
            if matchup == 0:
                weektype = "Preseason"
            else:
                weektype = "matchup " + str(matchup)
            glovars.message_display(weektype,306,555,glovars.teamFont30,glovars.white)

            #display the schedule for the week
            for i in range(3):

                #offsets for match on right side
                xdist = 117
                goalfilloffset = 0
                goalsoffset = 0
                borderoffset = 0
                if i == 1:
                    xdist = 379
                    borderoffset = -54
                    goalfilloffset = -284
                    goalsoffset = -22

                #determine home and away teams, add outline, and blit to screen
                awayschedule = f["schedule"][page_observe][i][0]
                homeschedule = f["schedule"][page_observe][i][1]
                pygame.draw.rect(glovars.screen,glovars.white,(xdist - 4 + borderoffset, 171 + (125 * i), 288, 112),0)
                glovars.screen.blit(glovars.defaultTeams[homeschedule].scorebug, (xdist,229 + (125 * i)))
                glovars.screen.blit(glovars.defaultTeams[awayschedule].scorebug, (xdist,175 + (125 * i)))

                #determine scores, add fill, and blit to screen
                pygame.draw.rect(glovars.screen,glovars.black,(xdist + 230 + goalfilloffset, 175 + (125 * i), 50, 50),0)
                pygame.draw.rect(glovars.screen,glovars.black,(xdist + 230 + goalfilloffset, 229 + (125 * i), 50, 50),0)
                if page_observe < day:
                    texthome = glovars.EASmall50.render(str((f["results"][page_observe][i][0]["Goals"])), True, glovars.white)
                    texthome_rect = texthome.get_rect(center = (372 + goalsoffset, 254 + (125 * i)))
                    textaway = glovars.EASmall50.render(str((f["results"][page_observe][i][1]["Goals"])), True, glovars.white)
                    textaway_rect = textaway.get_rect(center = (372 + goalsoffset, 200 + (125 * i)))
                    glovars.screen.blit(texthome, texthome_rect)
                    glovars.screen.blit(textaway, textaway_rect)


        elif teamOptions == "trade":
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)

        # FREE AGENTS
        elif teamOptions == "free agents":
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)

            #display moves left
            glovars.message_display("free agents - moves left: " + str(f["info"][0]["freeAgentMoves"]),116,180,glovars.teamFont30,glovars.googusGreen)

            #rotate through pages of free agents
            pygame.draw.rect(glovars.screen,glovars.white,(294,548,334,50),0)
            pygame.draw.rect(glovars.screen,glovars.black,(298,552,326,42),0)
            pygame.draw.rect(glovars.screen,glovars.white,(516,548,112,50),0)
            left_observe = pygame.draw.rect(glovars.screen,glovars.black,(520,552,50,42),0)
            right_observe = pygame.draw.rect(glovars.screen,glovars.black,(574,552,50,42),0)
            glovars.message_display("page " + str(page_observe),306,555,glovars.teamFont30,glovars.white)

            finalPageMax = int(len(f["freeagents"])%3)

            for i in range(3):
                pygame.draw.rect(glovars.screen,glovars.white,(120,254 + (100 * i),334,58),0)
                pygame.draw.rect(glovars.screen,glovars.black,(124,258 + (100 * i),326,50),0)
                pygame.draw.rect(glovars.screen,glovars.white,(450,254 + (100 * i),150,58),0)
                #freeAgentButtons[i] = 
                pygame.draw.rect(glovars.screen,glovars.black,(454,258 + (100 * i),142,50),0)
                if(page_observe != int(len(f["freeagents"])/3)):
                    glovars.message_display(f["freeagents"][(page_observe * 3) + i],130,264 + (100 * i),glovars.teamFont30,glovars.white)
                elif finalPageMax == 2:
                    if i != 2:
                        glovars.message_display(f["freeagents"][(page_observe * 3) + i],130,264 + (100 * i),glovars.teamFont30,glovars.white)
                else:
                    if i == 0:
                        glovars.message_display(f["freeagents"][(page_observe * 3) + i],130,264 + (100 * i),glovars.teamFont30,glovars.white)


    #default all leagueOptions and league buttons to false
    leagueOptionsButtons = [False] * 6

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
 
            #order teams by points
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
            leagueOptionsButtons[4] = pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,194),0)
            leagueOptionsButtons[5] = pygame.draw.rect(glovars.screen,glovars.black,(98,354,526,194),0)
            glovars.message_display("player stats",110,308,glovars.teamFont30,glovars.white)
            glovars.message_display("team stats",110,506,glovars.teamFont30,glovars.white)

        # TEAM STATS
        elif leagueOptions == "team stats":
            #fill background
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)

            #display stats
            glovars.message_display("team stats",116,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("gs",375,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("ga",442,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("e",517,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("e",575,180,glovars.teamFont30,glovars.googusGreen)

            for i in range(6):
                glovars.message_display(glovars.defaultTeams[i].name.split(' ', 1)[1],116,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display("a",575,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(f["teamdata"][0][glovars.defaultTeams[i].name][0]["scoredgoals"]),380,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display(str(f["teamdata"][0][glovars.defaultTeams[i].name][0]["allowedgoals"]),446,240 + (i * 50),glovars.teamFont30,glovars.white)
                glovars.message_display("s",513,240 + (i * 50),glovars.teamFont30,glovars.white)

        # PLAYER STATS
        elif leagueOptions == "player stats": 

            #fill background
            pygame.draw.rect(glovars.screen,glovars.white,(94,152,534,400),0)
            pygame.draw.rect(glovars.screen,glovars.black,(98,156,526,392),0)

            #rotate through teams
            pygame.draw.rect(glovars.screen,glovars.white,(294,548,334,50),0)
            pygame.draw.rect(glovars.screen,glovars.black,(298,552,326,42),0)
            pygame.draw.rect(glovars.screen,glovars.white,(516,548,112,50),0)
            left_observe = pygame.draw.rect(glovars.screen,glovars.black,(520,552,50,42),0)
            right_observe = pygame.draw.rect(glovars.screen,glovars.black,(574,552,50,42),0)
            statTeam = glovars.defaultTeams[page_observe].name
            statTeam = statTeam.split(' ', 1)[0]
            glovars.message_display(statTeam,306,555,glovars.teamFont30,glovars.white)

            #display stats
            glovars.message_display("player stats",116,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("gs",375,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("ga",442,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("sog",503,180,glovars.teamFont30,glovars.googusGreen)
            glovars.message_display("a",583,180,glovars.teamFont30,glovars.googusGreen)

            offPlayer = f["teamdata"][0][glovars.defaultTeams[page_observe].name][0]["offense"]
            defPlayer = f["teamdata"][0][glovars.defaultTeams[page_observe].name][0]["defense"]
            goalPlayer = f["teamdata"][0][glovars.defaultTeams[page_observe].name][0]["goalie"]
            players = [offPlayer, defPlayer, goalPlayer]
            for i in range(3):
                glovars.message_display(players[i],116,265 + (100 * i),glovars.teamFont30,glovars.white)
                for j in range(len(f["playerdata"])):
                    if players[i] == f["playerdata"][j]["name"]:
                        glovars.message_display(str(f["playerdata"][j]["goalsScored"]),383,265 + (100 * i),glovars.teamFont30,glovars.white)
                        glovars.message_display(f["playerdata"][j]["goalsAllowed"],450,265 + (100 * i),glovars.teamFont30,glovars.white)

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


def optionsCheck(teamOptions, leagueOptions, opage, f):
    global page_observe

    page_observe = opage
    moveColorsCheck = False

    #TEAM OPTIONS
    if teamOptionsButtons[0] != False: #check for click on team options tab
        if teamOptionsButtons[0].collidepoint(pygame.mouse.get_pos()):
            teamOptions = "roster"
        if teamOptionsButtons[1].collidepoint(pygame.mouse.get_pos()):
            teamOptions = "schedule"
            page_observe = day
        else:
            page_observe = f["info"][0]["day"]
        if teamOptionsButtons[2].collidepoint(pygame.mouse.get_pos()):
            teamOptions = "trade"
        if teamOptionsButtons[3].collidepoint(pygame.mouse.get_pos()):
            teamOptions = "free agents"
            page_observe = 0
    if left_observe and teamOptions == "schedule": #check for click on schedule tab
        if left_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe -= 1
            if page_observe < 0:
                page_observe = len(f["schedule"]) - 1
        if right_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe += 1
            if page_observe > len(f["schedule"]) - 1:
                page_observe = 0
    if left_observe and teamOptions == "free agents": #check for click on schedule tab
        if left_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe -= 1
            if page_observe < 0:
                page_observe = int((len(f["freeagents"])-1)/3)
        if right_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe += 1
            if page_observe > int((len(f["freeagents"])-1)/3):
                page_observe = 0

    #LEAGUE OPTIONS
    if leagueOptionsButtons[0] != False:
        if leagueOptionsButtons[0].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "standings"
        if leagueOptionsButtons[1].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "stats"
        if leagueOptionsButtons[2].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "history"
        if leagueOptionsButtons[3].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "prestige"
    if leagueOptionsButtons[4] != False:
        if leagueOptionsButtons[4].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "player stats"
            page_observe = playerTeam
        if leagueOptionsButtons[5].collidepoint(pygame.mouse.get_pos()):
            leagueOptions = "team stats"
            page_observe = playerTeam
    if left_observe and leagueOptions == "player stats":
        if left_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe -= 1
            if page_observe < 0:
                page_observe = 5
        if right_observe.collidepoint(pygame.mouse.get_pos()):
            page_observe += 1
            if page_observe > 5:
                page_observe = 0

    return teamOptions, leagueOptions, page_observe


def rosterSwitch(i, f, data):
    for j in range(len(f["teamdata"][0])):
        if f["info"][0]["userteam"] == glovars.defaultTeams[j].name:
            if (i == 0 or selected_move == 0) and (i == 1 or selected_move == 1):
                newOffense = f["teamdata"][0][f["info"][0]["userteam"]][0]["defense"]
                newDefense = f["teamdata"][0][f["info"][0]["userteam"]][0]["offense"]
                newGoalie = f["teamdata"][0][f["info"][0]["userteam"]][0]["goalie"]
            elif (i == 0 or selected_move == 0) and (i == 2 or selected_move == 2):
                newOffense = f["teamdata"][0][f["info"][0]["userteam"]][0]["goalie"]
                newDefense = f["teamdata"][0][f["info"][0]["userteam"]][0]["defense"]
                newGoalie = f["teamdata"][0][f["info"][0]["userteam"]][0]["offense"]
            elif (i == 1 or selected_move == 1) and (i == 2 or selected_move == 2):
                newOffense = f["teamdata"][0][f["info"][0]["userteam"]][0]["offense"]
                newDefense = f["teamdata"][0][f["info"][0]["userteam"]][0]["goalie"]
                newGoalie = f["teamdata"][0][f["info"][0]["userteam"]][0]["defense"]
    data["franchises"][fnum]["teamdata"][0][f["info"][0]["userteam"]][0]["offense"] = newOffense
    data["franchises"][fnum]["teamdata"][0][f["info"][0]["userteam"]][0]["defense"] = newDefense
    data["franchises"][fnum]["teamdata"][0][f["info"][0]["userteam"]][0]["goalie"] = newGoalie
    wfile = open("savedata.json", "w")
    json.dump(data, wfile)
    wfile.close()


def runMenu(menu, ffran):
    global tintmenus, allmenus, selected_menu, leagueOptions, teamOptions, day, playerTeam, selected_move, fnum

    #set the fnum of this franchise
    fnum = ffran

    #all game data
    rfile = open("savedata.json", "r")
    data = json.load(rfile)
    rfile.close()

    #data for this franchise
    f = data["franchises"][fnum]

    #play, team, league
    selected_menu = menu
    
    #change color for roster moves
    selected_move = None 

    #default options to the menu
    teamOptions = "menu"
    leagueOptions = "menu"

    exitLoop = False #exit game

    allmenus = False #all top level menus (play, team, league)- defaults to false
    tintmenus = [glovars.black, glovars.black, glovars.black] #tint color for all menus

    appPressed = False #if an app is pressed on phone 
    loops = 315 #number of loops - defaults to maximun when no app is pressed

    #current matchup day
    day = f["info"][0]["day"]
    #current player team
    for i in range(6):
        if f["info"][0]["userteam"] == glovars.defaultTeams[i].name:
            playerTeam = i
    #defaults opage (operating page) to None
    opage = None

    loopImages(data)

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
                    teamOptions = "menu"
                if menuleague.collidepoint(pygame.mouse.get_pos()):
                    selected_menu = 2
                    leagueOptions = "menu"
                
                for i in range(3):
                    if moveButtons[i] != False: #check for click on roster tab - move buttons
                        if moveButtons[i].collidepoint(pygame.mouse.get_pos()):
                            if selected_move == i:
                                selected_move = None
                            elif selected_move == None:
                                selected_move = i
                            elif selected_move != i:
                                rosterSwitch(i, f, data)
                                selected_move = None
                                

                #check if team and league options have been selected
                teamOptions, leagueOptions, opage = optionsCheck(teamOptions, leagueOptions, opage, f)

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
        loopImages(data)
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