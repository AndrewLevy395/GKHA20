import pygame

import defaultTeam

def init(thisScreen):

    #colors
    global black, white, grey, red, googusGreen, lightGrey, darkGrey, blackTint
    black = 0, 0, 0
    white = 255, 255, 255
    darkGrey = 100, 100, 100
    grey = 175, 175, 175
    lightGrey = 225, 225, 225
    red = 234, 0, 0
    googusGreen = 33, 239, 22
    blackTint = 20, 20, 20

    #screen
    global screen
    screen = thisScreen

    #fonts
    global ESPNSmall, EALarge, teamFont, teamSelectFont, EASmall30, periodFont, periodFontSmall, scoreFont, ESPN, timeFont
    ESPNSmall = pygame.font.Font("assets/fonts/esp_ital.ttf", 25)
    ESPN = pygame.font.Font("assets/fonts/esp_ital.ttf", 40)
    EALarge = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 100)
    EASmall30 = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 30)
    teamFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 40)
    teamSelectFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 35)
    periodFont = pygame.font.Font("assets/fonts/Klavika_Regular_Plain.otf", 48)
    periodFontSmall = pygame.font.Font("assets/fonts/Klavika_Regular_Plain.otf", 24)
    scoreFont = pygame.font.Font("assets/fonts/Panton-BlackCaps.otf", 40)
    timeFont = pygame.font.Font("assets/fonts/CursedTimerULiL.ttf", 40)



    #teams
    global defaultTeams
    defaultTeams = defaultTeam.createAll()

def message_display(text,x,y,font,color):
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.topleft = (x,y)
    screen.blit(TextSurf, TextRect)
    return TextRect.width

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()