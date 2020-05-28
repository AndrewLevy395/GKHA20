import pygame

import defaultTeam

def init(thisScreen):

    #colors
    global black, white, grey
    black = 0, 0, 0
    white = 255, 255, 255
    grey = 175,175,175

    #screen
    global screen
    screen = thisScreen

    #fonts
    global ESPNSmall, EALarge, teamFont, teamSelectFont, EASmall30
    ESPNSmall = pygame.font.Font("assets/fonts/esp_ital.ttf", 25)
    EALarge = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 100)
    EASmall30 = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 30)
    teamFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 40)
    teamSelectFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 35)

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