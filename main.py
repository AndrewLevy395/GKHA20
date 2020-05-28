import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import mainmenu
import glovars

from pygame.locals import *


def init():
    global clock, width, height
    pygame.init()
    pygame.display.set_caption('GKHA 20')
    width, height = 1024, 626
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    glovars.init(screen)
    initImages()

def initImages():
    global introScreen, introScreenStart
    introScreen = pygame.image.load("assets/images/gkhaMain.png")
    introScreenStart = pygame.image.load("assets/images/gkhaMainClick.png")

def intro():
    intro = True
    exitLoop = False
    loopTotalTime = 0
    loopTimeTracker = 0
    loopStart = time.perf_counter()
    while intro and (not exitLoop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitLoop = True
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN and loopTotalTime > 6:
                intro = False
        if exitLoop:
            break
        glovars.screen.fill(glovars.white)
        if loopTotalTime < 5.7:
            glovars.screen.fill(glovars.black)
        elif loopTotalTime >13:
            glovars.screen.fill(glovars.black)
            glovars.screen.blit(introScreenStart,(0,25)) #this can be changed to save a small amount of space if need be
        else:
            glovars.screen.fill(glovars.black)
            glovars.screen.blit(introScreen,(0,25))       
        clock.tick(30)
        pygame.display.flip()
        loopTimeTracker = time.perf_counter()
        loopTotalTime = loopTimeTracker - loopStart
    return exitLoop

def game():
    mainmenu.runMenu()


if __name__ == "__main__":
    init()
    #intro()
    game()
    pygame.quit()
