import pygame

import defaultTeam

def init(thisScreen):

    #colors
    global black, white, grey, red, googusGreen, lightGrey, darkGrey, darkerGrey, blackTint
    black = 0, 0, 0
    white = 255, 255, 255
    darkGrey = 100, 100, 100
    grey = 175, 175, 175
    lightGrey = 225, 225, 225
    red = 234, 0, 0
    googusGreen = 33, 239, 22
    blackTint = 35, 35, 35
    

    #screen
    global screen
    screen = thisScreen

    #fonts
    global ESPNSmall, EALarge, teamFont20, teamFont30, teamFont40, teamSelectFont, EASmall30, EASmall50, periodFont, periodFontSmall, scoreFont, ESPN, timeFont
    ESPNSmall = pygame.font.Font("assets/fonts/esp_ital.ttf", 25)
    ESPN = pygame.font.Font("assets/fonts/esp_ital.ttf", 40)
    EALarge = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 100)
    EASmall30 = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 30)
    EASmall50 = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 50)
    teamFont40 = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 40)
    teamFont20 = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 20)
    teamFont30 = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 30)
    teamSelectFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 35)
    periodFont = pygame.font.Font("assets/fonts/Klavika_Regular_Plain.otf", 48)
    periodFontSmall = pygame.font.Font("assets/fonts/Klavika_Regular_Plain.otf", 24)
    scoreFont = pygame.font.Font("assets/fonts/Panton-BlackCaps.otf", 40)
    timeFont = pygame.font.Font("assets/fonts/CursedTimerULiL.ttf", 40)

    #teams
    global defaultTeams
    defaultTeams = defaultTeam.createAll()

    #clock
    global clock
    clock = pygame.time.Clock()

    #default team data for starting a franchise
    global franchiseTeamData, franchisePlayerData

    teamData = [None] * 6

    playerData = []

    for i in range(len(defaultTeams)):
        #default team data
        teamData[i] = [{"overall":str(defaultTeams[i].overall), "wins": 0, "losses": 0, "overtimelosses": 0, "scoredgoals": 0, "allowedgoals": 0}]

        #default offender data
        playerData.append({"name": defaultTeams[i].offense.name, "image": defaultTeams[i].offense.sprite, 
        "stamina": defaultTeams[i].offense.stamina, "shotAccuracy": defaultTeams[i].offense.shotAccuracy, "shotSpeed": defaultTeams[i].offense.shotSpeed, 
        "speed": defaultTeams[i].offense.speed, "reaction": defaultTeams[i].offense.reaction, "goalsScored": 0})

        #default defender data
        playerData.append({"name": defaultTeams[i].defense.name, "image": defaultTeams[i].defense.sprite, 
        "stamina": defaultTeams[i].defense.stamina, "shotAccuracy": defaultTeams[i].defense.shotAccuracy, "shotSpeed": defaultTeams[i].defense.shotSpeed, 
        "speed": defaultTeams[i].defense.speed, "reaction": defaultTeams[i].defense.reaction, "goalsScored": 0})

        #default goalie data
        playerData.append({"name": defaultTeams[i].goalie.name, "image": defaultTeams[i].goalie.sprite, 
        "stamina": defaultTeams[i].goalie.stamina, "shotAccuracy": defaultTeams[i].goalie.shotAccuracy, "shotSpeed": defaultTeams[i].goalie.shotSpeed, 
        "speed": defaultTeams[i].goalie.speed, "reaction": defaultTeams[i].goalie.reaction, "goalsScored": 0})

    franchisePlayerData = playerData

    franchiseTeamData = [{ "Alaskan Thunder": teamData[0], "American Revolution": teamData[1], 
    "Boondock Beluga Whales": teamData[2], "Florida Tropics": teamData[3], "Smashville Chippewas": teamData[4],
    "Southside Spartans": teamData[5]}]

def message_display(text,x,y,font,color):
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.topleft = (x,y)
    screen.blit(TextSurf, TextRect)
    return TextRect.width

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()