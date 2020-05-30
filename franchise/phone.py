import pygame

import glovars

def drawApp(loops):
    pygame.draw.rect(glovars.screen,glovars.white,(715,505-loops,190,loops),0)


def closeApp(loops):
    pygame.draw.rect(glovars.screen,glovars.white,(715,190+loops,190,315-loops),0)