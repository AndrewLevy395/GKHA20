import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import glovars


#initialize pygame module, screen, and global game variables
def init():
    global width, height
    pygame.init()
    pygame.display.set_caption('GKHA 20')
    width, height = 1024, 626
    screen = pygame.display.set_mode((width, height))
    glovars.init(screen)
    initImages()


#initialize intro screen images (probably will be deleted)
def initImages():
    global introScreen, introScreenStart
    introScreen = pygame.image.load("assets/images/gkhaMain.png")
    introScreenStart = pygame.image.load("assets/images/gkhaMainClick.png")


#run intro sequence (needs be redone)
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
            glovars.screen.blit(introScreenStart,(0,25)) #this can be removed to save a small amount of space if need be
        else:
            glovars.screen.fill(glovars.black)
            glovars.screen.blit(introScreen,(0,25))       
        glovars.clock.tick(30)
        pygame.display.flip()
        loopTimeTracker = time.perf_counter()
        loopTotalTime = loopTimeTracker - loopStart
    return exitLoop


#run the game (ooo so powerful)
def game():
    mainmenu.runMenu()


#call game functions
init()
import mainmenu #have to import mainmenu after global variables are initialized
#intro()
game()
pygame.quit()
