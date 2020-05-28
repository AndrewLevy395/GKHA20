import pygame

def init(thisScreen):

    #colors
    global black, white
    black = 0, 0, 0
    white = 255, 255, 255

    #screen
    global screen
    screen = thisScreen

    #fonts
    global ESPNSmall, EALarge, teamFont, teamSelectFont, EASmall
    ESPNSmall = pygame.font.Font("assets/fonts/esp_ital.ttf", 25)
    EALarge = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 100)
    EASmall = pygame.font.Font("assets/fonts/EASPORTS15.ttf", 30)
    teamFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 40)
    teamSelectFont = pygame.font.Font("assets/fonts/Panton-LightCaps.otf", 35)

def message_display(text,x,y,font,color):
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.topleft = (x,y)
    screen.blit(TextSurf, TextRect)
    return TextRect.width

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()