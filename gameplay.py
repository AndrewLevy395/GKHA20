import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import time
import random
import math


import glovars
import defaultPlayer
import ball

clock = pygame.time.Clock()
keys = [0, 0, 0, 0]

goalScored = pygame.image.load("assets/images/goalScored.png")
periodScreen = pygame.image.load("assets/images/period.png")
gameOver = pygame.image.load("assets/images/gameover.png")
yellowTeam = pygame.image.load("assets/images/yellowTeam.png")
carpet = pygame.image.load("assets/images/carpet.png")
orangeBall = pygame.image.load("assets/images/orangeBall.png")#.convert_alpha()
scorebug1 = pygame.image.load("assets/images/scorebug1.png")
scorebug2 = pygame.image.load("assets/images/scorebug2.png")
alaSB = pygame.image.load("assets/images/alaSB.png")
ameSB = pygame.image.load("assets/images/ameSB.png")
sssSB = pygame.image.load("assets/images/sssSB.png")
floSB = pygame.image.load("assets/images/floSB.png")
bbwSB = pygame.image.load("assets/images/bbwSB.png")
smcSB = pygame.image.load("assets/images/smcSB.png")
alaPN = pygame.image.load("assets/images/alaPN.png")
amePN = pygame.image.load("assets/images/amePN.png")
sssPN = pygame.image.load("assets/images/sssPN.png")
floPN = pygame.image.load("assets/images/floPN.png")
bbwPN = pygame.image.load("assets/images/bbwPN.png")
smcPN = pygame.image.load("assets/images/smcPN.png")
bbwDesc = pygame.image.load("assets/images/BBWdesc.png")
smcDesc = pygame.image.load("assets/images/SMCdesc.png")
alaDesc = pygame.image.load("assets/images/ALAdesc.png")
ameDesc = pygame.image.load("assets/images/AMEdesc.png")
floDesc = pygame.image.load("assets/images/FLOdesc.png")
sssDesc = pygame.image.load("assets/images/SSSdesc.png")



#draw goals                                   LR   UD  S L
goal10 = pygame.draw.rect(carpet,glovars.red,(120,209,76,7),0) #left top
goal11 = pygame.draw.rect(carpet,glovars.red,(120,209,7,125),0) #left side
goal12 = pygame.draw.rect(carpet,glovars.red,(120,327,76,7),0) #left bottom

goal13 = pygame.draw.rect(carpet,glovars.red,(830,208,75,7),0) #right top
goal14 = pygame.draw.rect(carpet,glovars.red,(898,209,7,125),0) #right side
goal15 = pygame.draw.rect(carpet,glovars.red,(830,327,75,7),0) #right bottom

goalLineLeft = pygame.draw.rect(carpet,glovars.white,(194,216,2,111),0)
goalLineRight = pygame.draw.rect(carpet,glovars.white,(830,215,2,112),0)
centerLine = pygame.draw.rect(carpet,glovars.white,(510,11,4,554),0)

        
ball1=ball.Ball(487,303,0,orangeBall)


#ball collision with goal
def goalCollide(height,width,velX,velY):
    if ball1.rect.collidepoint(120,210.5):
        ball1.x = ball1.x-5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(120,383-7.5):
        ball1.x = ball1.x-5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(205,210.5):
        ball1.x = ball1.x+5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(205,383-7.5):
        ball1.x = ball1.x+5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(819,210.5):
        ball1.x = ball1.x-5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(819,383-7.5):
        ball1.x = ball1.x-5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(904,210.5):
        ball1.x = ball1.x+5
        ball1.angle = -ball1.angle
    elif ball1.rect.collidepoint(904,383-7.5):
        ball1.x = ball1.x+5
        ball1.angle = -ball1.angle
    else:
        if height > width:
            ball1.angle = -ball1.angle
            if velX:
                ball1.x = ball1.x-5
            else:
                ball1.x = ball1.x+5
        else:
            ball1.angle = math.pi-ball1.angle
            if velY:
                ball1.y = ball1.y-5
            else:
                ball1.y = ball1.y+5
    ball1.speed=220
    ball1.friction = .975
    return 0


#resets the rink and player after every goal or period
def resetRink(playerOffense,computerOffense,playerDefense,computerDefense,playerGoalie,computerGoalie):
    ball1.x = 502
    ball1.y = 318
    ball1.speed = 0
    playerOffense.x = playerOffense.initX
    playerOffense.y = playerOffense.initY
    computerOffense.x = computerOffense.initX
    computerOffense.y = computerOffense.initY
    playerDefense.x = playerDefense.initX
    playerDefense.y = playerDefense.initY
    computerDefense.x = computerDefense.initX
    computerDefense.y = computerDefense.initY
    playerGoalie.x = playerGoalie.initX
    playerGoalie.y = playerGoalie.initY
    computerGoalie.x = computerGoalie.initX
    computerGoalie.y = computerGoalie.initY


#movement for goalie in coordination with where the ball is 
def goalieMove(player,time_delta,team1,team2):
    if ball1.y-30 < player.y and player.y>228:
        player.move(1,0,0,0,time_delta)
    if ball1.y-30 > player.y and player.y<348:
        player.move(0,1,0,0,time_delta)
    if team1 and ball1.x>662 and player.x<player.initX+100:
        player.move(0,0,0,1,time_delta)
    if team2 and ball1.x<362 and player.x>player.initX-100:
        player.move(0,0,1,0,time_delta)
    if team1 and ball1.x<662 and player.x>player.initX:
        player.move(0,0,1,0,time_delta)
    if team2 and ball1.x>362 and player.x<player.initX:
        player.move(0,0,0,1,time_delta)


#AI forward movement 
def forwardAIMove(player,time_delta,holding):
    aimovement = [0, 0, 0, 0]
    normal = 0
    up = 0
    down = 0
    dx = ball1.x - player.x
    dy = ball1.y - player.y
    distance = math.hypot(dx, dy)
    if distance < 60:
        normal = 1
    randomMove = random.randint(0,5)
    if ball1.x <= 210:
        if ball1.y < 200:
            if player.y < 175:
                if player.x < 205:
                    normal = 1
                elif player.x > ball1.x:
                    aimovement[2] = 1
                    if randomMove == 1:
                         aimovement[0] = 1
                    if randomMove == 3:
                         aimovement[1] = 1
                else:
                    aimovement[3] = 1
                    if randomMove == 1:
                         aimovement[0] = 1
                    if randomMove == 3:
                         aimovement[1] = 1
            elif player.y > 425:
                if player.x > 412:
                    aimovement[0] = 1
                    aimovement[2] = 1
                elif player.x > 205:
                    aimovement[0] = 1
                    if randomMove == 2:
                       aimovement[2] = 1 
                elif player.x > 40:
                    aimovement[2] = 1
                    if randomMove == 1:
                        aimovement[0] = 1
                else:
                    aimovement[0] = 1
            else:
                aimovement[0] = 1
                if randomMove == 3:
                         aimovement[1] = 1
        elif ball1.y > 373:
            if player.y > 425:
                if player.x < 205:
                    normal = 1
                elif player.x > ball1.x:
                    aimovement[2] = 1
                    if randomMove == 1:
                         aimovement[1] = 1
                    if randomMove == 3:
                         aimovement[0] = 1
                else:
                    aimovement[3] = 1
                    if randomMove == 1:
                         aimovement[1] = 1
                    if randomMove == 3:
                         aimovement[0] = 1
            elif player.y <175:
                if player.x > 412:
                    aimovement[1] = 1
                    aimovement[2] = 1
                elif player.x > 205:
                    aimovement[1] = 1
                elif player.x > 40:
                    aimovement[2] = 1
                else:
                    aimovement[1] = 1
            else:
                aimovement[1] = 1
        else:
            if player.x > 350:
                aimovement[2] = 1
            elif player.x > 205:
                if player.y <175 or player.y > 425:
                    aimovement[2] = 1
                else:
                    if player.y > ball1.y:
                        aimovement[0] = 1
                    else:
                        aimovement[1] = 1
            elif player.x > 30:
                aimovement[2] = 1
                if randomMove == 3:
                         aimovement[1] = 1
            else:
                if player.y > ball1.y:
                    aimovement[0] = 1
                    if randomMove == 2:
                        aimovement[0] = 0
                        aimovement[1] = 1
                else:
                    aimovement[1] = 1
                    if randomMove == 2:
                        aimovement[1] = 0
                        aimovement[0] = 1
                    
                    
    elif ball1.x <= 780:
        if player.x <= 780 and player.x >= 205:
            if player.y <= 155 and ball1.y <= 205 and ball1.x > player.x:
                normal = 1
                up = 1
            elif player.y >= 450 and ball1.y >= 450 and ball1.x > player.x:
                normal = 1
                down = 1
            else:
                normal = 1
        elif player.x < 205:
            if player.y < 120:
                aimovement[3] = 1
            elif player.y < 300:
                aimovement[0] = 1
            elif player.y < 440:
                aimovement[1] = 1
            else:
                aimovement[3] = 1
        else:
            if player.y < 205 or player.y > 373:
                aimovement[2] = 1
    else:
        if holding == 0:
            if player.x < 610:
                aimovement[3] = 1
            elif player.x < 720:
                if ball1.y < 210 and player.y < 175:
                    aimovement[0] = 1
                elif ball1.y > 373 and player.y > 425:
                    aimovement[1] = 1
                elif ball1.y > player.y:
                    aimovement[1] = 1
                elif ball1.y < player.y:
                    aimovement[0] = 1
            if player.x > 620:
                aimovement[2] = 1
                
                
    if player.x > 780:
        normal = 0
    if normal:
        aimovement = [0, 0, 0, 0]
        if ball1.x-30 < player.x:
            aimovement[2] = 1
        if ball1.x-30 > player.x:
            aimovement[3] = 1
        if ball1.y-30 > player.y:
            aimovement[1] = 1
        if ball1.y-30 < player.y:
            aimovement[0] = 1
    if up:
        aimovement[0] = 1
        aimovement[1] = 0
    if down:
        aimovement[1] = 1
        aimovement[0] = 0
        
    player.move(aimovement[0],aimovement[1],aimovement[2],aimovement[3],time_delta)

#collision between player and AI forwards
def playersCollide(playerOffense,computerOffense):
    if pygame.sprite.collide_mask(computerOffense,playerOffense) != None:
        playerOffense.x = playerOffense.groldx
        playerOffense.y = playerOffense.groldy
        computerOffense.x = computerOffense.groldx
        computerOffense.y = computerOffense.groldy
        if playerOffense.x > 512:
            playerOffense.x = playerOffense.x - 10
        else:
            playerOffense.x = playerOffense.x + 10
        if playerOffense.y > computerOffense.y:
            playerOffense.y = playerOffense.y + 7
        else:
            playerOffense.y = playerOffense.y - 7
        return 1
    else:
        return 0

def knockeyGame(yourTeam,oppTeam):

    #set all players
    playerOffense = yourTeam.offense
    playerDefense = yourTeam.defense
    playerGoalie = oppTeam.goalie
    computerOffense = oppTeam.offense
    computerDefense = oppTeam.defense
    computerGoalie = yourTeam.goalie

    playerOffense.controlled = True

    #set all start locations
    playerOffense.setInitLocation(455,265)
    playerDefense.setInitLocation(550,300)
    playerGoalie.setInitLocation(664,220)
    computerOffense.setInitLocation(344,154)
    computerDefense.setInitLocation(250,300)
    computerGoalie.setInitLocation(130,220)

    #list of all players
    allPlayers = [playerOffense, playerDefense, playerGoalie, computerOffense, computerDefense, computerGoalie]

    paused = 0
    pauser = 0
    gameLoop = 1
    endLoop = 1
        #ball contacting with sprites
    ballContact = 0
    goalBallContact = 0 
    shotOrNot = 0
    shotRadius = 0
    shootCooldown = 0
    shootCooldown2 = 0
    collider = 0
        #ball velocities
    velX = 0
    velY = 0
        #goal scoring and goal timing
    rightGoal = 0
    leftGoal = 0
    anyGoal = 0
    team1score = 0
    team2score = 0
    goalTotalTime = 0
    timeTracker = 0
    goalTime = 0
        #timer related
    total_secs = 120
    seconds = 0
    minutes = 0
    secs_remain = -1
    mins_remain = -1
    total_ticks = 0
        #period / end of game
    endOfPeriod = 0
    period = 1
    anyPeriod = 0
    periodTime = 0
    periodTotalTime = 0
    endOfGame = 0
    endTime = 0
    endTotalTime = 0
    anyGame = 0

    resetRink(playerOffense,computerOffense,playerDefense,computerDefense,playerGoalie,computerGoalie)
    
    while gameLoop == 1 and endLoop == 1:
        space = 0
        start_ticks=pygame.time.get_ticks()
        glovars.screen.fill(glovars.red)
        glovars.screen.blit(carpet,(0,50))
        glovars.screen.blit(scorebug1, (1024-145,0))
        glovars.screen.blit(scorebug1, (1024-240,0))
        glovars.screen.blit(oppTeam.scorebug, (180,0))
        glovars.screen.blit(yourTeam.scorebug, (479,0))
        glovars.screen.blit(scorebug2, (703,0))
        glovars.screen.blit(scorebug2, (404,0))

        glovars.screen.blit(orangeBall, [ball1.x,ball1.y])

        for i in allPlayers:
            glovars.screen.blit(i.image, [i.x, i.y])
            
        if anyPeriod:
            glovars.screen.blit(periodScreen,(0,50))
        if anyGoal:
            glovars.screen.blit(goalScored,(-7,50))
        if anyGame:
            glovars.screen.blit(gameOver,(0,50))
        pos = pygame.mouse.get_pos()
        velX, velY = ball1.getVelocities()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endLoop = 0
                pygame.quit()
                exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=1
                elif event.key==K_a:
                    keys[1]=1
                elif event.key==K_s:
                    keys[2]=1
                elif event.key==K_d:
                    keys[3]=1
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=0
                elif event.key==pygame.K_a:
                    keys[1]=0
                elif event.key==pygame.K_s:
                    keys[2]=0
                elif event.key==pygame.K_d:
                    keys[3]=0
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
                    space = 1
            if event.type == pygame.KEYDOWN and paused == 0:
                if event.key==K_ESCAPE:
                    paused = 1
            if event.type == pygame.KEYUP and paused == 1:
                if event.key==K_ESCAPE:
                    pauser = 1
            if event.type == pygame.KEYDOWN and pauser == 1:
                if event.key==K_ESCAPE:
                    paused = 0
            if event.type == pygame.KEYUP and paused == 0:
                if event.key==K_ESCAPE:
                    pauser = 0
            if event.type == pygame.KEYDOWN and paused == 1:
                if event.key==K_i:
                    endLoop = mainMenuGo(0)
        if endLoop == 0:
            break
        time_delta = clock.get_time() / 1000.0
        if paused == 0:
            playerOffense.move(keys[0],keys[2],keys[1],keys[3],time_delta)

        for i in allPlayers:
            if i.x > (1024 - (10 + i.w / 2)):
                i.x = (1024 - (10 + i.w / 2))
            if i.x < 10:
                i.x = 10
            if i.y > 626 - (10 + i.h / 2):
                i.y = 626 - (10 + i.h / 2)
            if i.y < 60:
                i.y = 60

        if paused == 0:  
            ball1.move(time_delta)

        if paused == 0:
            for i in allPlayers:
                if i.position != "goalie" and i.controlled == False:
                    forwardAIMove(i,time_delta,0)

        moveChance = random.randint(0,playerGoalie.reaction)
        if moveChance != 1 and paused == 0:
            goalieMove(playerGoalie,time_delta,1,0)
        moveChance = random.randint(0,computerGoalie.reaction)
        if moveChance != 1 and paused == 0:
            goalieMove(computerGoalie,time_delta,0,1)

        if ball1.x > (1024-40):
            ball1.x = (1024-40)
            ball1.dx = -ball1.dx
            ball1.angle = -ball1.angle
        if ball1.x < 10:
            ball1.x = 10
            ball1.dx = -ball1.dx
            ball1.angle = -ball1.angle
        if ball1.y > (626-40):
            ball1.y = (626-40)
            ball1.dy = -ball1.dy
            ball1.angle = math.pi-ball1.angle
        if ball1.y < 60:
            ball1.y = 60
            ball1.dy = -ball1.dy
            ball1.angle = math.pi-ball1.angle

        ball1.rect = ball1.image.get_rect(topleft = (ball1.x,ball1.y-50))
        ball1.mask = pygame.mask.from_surface(ball1.image)
        playerOffense.rect = playerOffense.image.get_rect(topleft = (playerOffense.x,playerOffense.y-50))
        playerOffense.mask = pygame.mask.from_surface(playerOffense.image)
        computerOffense.rect = playerOffense.image.get_rect(topleft = (computerOffense.x,computerOffense.y-50))
        computerOffense.mask = pygame.mask.from_surface(computerOffense.image)
        playerGoalie.rect = playerGoalie.image.get_rect(topleft = (playerGoalie.x,playerGoalie.y-50))
        playerGoalie.mask = pygame.mask.from_surface(playerGoalie.image)
        computerGoalie.rect = computerGoalie.image.get_rect(topleft = (computerGoalie.x,computerGoalie.y-50))
        computerGoalie.mask = pygame.mask.from_surface(computerGoalie.image)

        playersCollide(computerOffense,computerGoalie)
        playersCollide(computerOffense,playerGoalie)
        playersCollide(playerOffense,computerGoalie)
        playersCollide(playerOffense,playerGoalie)

        if shootCooldown > 0:
            shootCooldown = shootCooldown + 1
            if shootCooldown == 20:
                shootCooldown = 0
        if shootCooldown2 > 0:
            shootCooldown2 = shootCooldown2 + 1
            if shootCooldown2 == 20:
                shootCooldown2 = 0
        if shootCooldown == 0:
            if space == 1:
                shotOrNot = ball1.shoot(playerOffense)
                shootCooldown = 1
        if pygame.sprite.collide_mask(ball1,playerOffense) != None:
            ballContact = 1
            collider = playerOffense
        elif pygame.sprite.collide_mask(ball1,computerOffense) != None:
            ballContact = 1
            collider = computerOffense
            forShot = random.randint(0,2)
            if shootCooldown == 0:
                if ball1.x > computerOffense.x and forShot != 1: 
                    shotOrNot = 1
                    shootCooldown2 = 1
        elif pygame.sprite.collide_mask(ball1,playerGoalie) != None:
            ballContact = 1
            collider = playerGoalie
        elif pygame.sprite.collide_mask(ball1,computerGoalie) != None:
            ballContact = 1
            collider = computerGoalie

        if ballContact == 1:
            ball1.collidePlayer(collider, shotOrNot)
        
        if ball1.rect.colliderect(goal11):
            allowOffset = goalCollide(85,15,velX,velY)
        elif ball1.rect.colliderect(goal10):
            allowOffset = goalCollide(15,85,velX,velY)
        elif ball1.rect.colliderect(goal12):
            allowOffset = goalCollide(15,85,velX,velY)
        elif ball1.rect.colliderect(goal14):
            allowOffset = goalCollide(85,15,velX,velY)
        elif ball1.rect.colliderect(goal13):
            allowOffset = goalCollide(15,85,velX,velY)
        elif ball1.rect.colliderect(goal15):
            allowOffset = goalCollide(15,85,velX,velY)
            
        if playerOffense.x>120-playerOffense.w/2 and playerOffense.x<205 and playerOffense.y>203-playerOffense.h/4.5 and playerOffense.y<373+playerOffense.h/2-playerOffense.h/4.5:
            playerOffense.x = playerOffense.groldx
            playerOffense.y = playerOffense.groldy
        if playerOffense.x>819-playerOffense.w/2 and playerOffense.x<904 and playerOffense.y>203-playerOffense.h/4.5 and playerOffense.y<373+playerOffense.h/2-playerOffense.h/4.5:
            playerOffense.x = playerOffense.groldx
            playerOffense.y = playerOffense.groldy

        if computerOffense.x>120-computerOffense.w/2 and computerOffense.x<205 and computerOffense.y>203-computerOffense.h/4.5 and computerOffense.y<373+computerOffense.h/2-computerOffense.h/4.5:

            computerOffense.x = computerOffense.groldx
            computerOffense.y = computerOffense.groldy
        if computerOffense.x>819-computerOffense.w/2 and computerOffense.x<904 and computerOffense.y>203-computerOffense.h/4.5 and computerOffense.y<373+computerOffense.h/2-computerOffense.h/4.5:
            computerOffense.x = computerOffense.groldx
            computerOffense.y = computerOffense.groldy

        if anyGoal == 0 and anyPeriod == 0 and anyGame == 0:
            if ball1.x-15>819 and ball1.x-15<904-40 and ball1.y-34>205 and ball1.y-15<375:
                if rightGoal == 0:
                    rightGoal = 1
                    anyGoal = 1
                
            if ball1.x+15>150 and ball1.x+15<202 and ball1.y-34>205 and ball1.y-15<375:
                if leftGoal == 0:
                    leftGoal = 1
                    anyGoal = 1

        if anyGoal == 0 and anyPeriod == 0 and anyGame == 0 and paused == 0:
            current_ticks = (pygame.time.get_ticks()-start_ticks)
            total_ticks = total_ticks+current_ticks
            seconds=math.trunc((total_ticks/1000)%60)
            minutes = math.trunc((total_ticks/1000)/60)
            secs_remain=(str("%02d" % (59-seconds)))
            mins_remain=(str(2-minutes))
            if int(secs_remain) <= 0 and int(mins_remain) <= 0:
                if period == 3:
                    if team1score != team2score:
                        endOfGame = 1
                        anyGame = 1
                elif period == 4:
                    endOfGame = 1
                    anyGame = 1
                else:
                    endOfPeriod = 1
                    anyPeriod = 1


        if leftGoal:
            goalTime = time.perf_counter()
            team2score = team2score + 1
            leftGoal = 0
        if rightGoal:
            goalTime = time.perf_counter()
            team1score = team1score + 1
            rightGoal = 0
        if anyGoal: 
            timeTracker = time.perf_counter()
            goalTotalTime = timeTracker - goalTime
        if goalTotalTime > 2:
            anyGoal = 0
            goalTotalTime = 0
            resetRink(playerOffense,computerOffense,playerDefense,computerDefense,playerGoalie,computerGoalie)

        if endOfPeriod:
            periodTime = time.perf_counter()
            endOfPeriod = 0
        if anyPeriod:
            timeTracker = time.perf_counter()
            periodTotalTime = timeTracker - periodTime
        if periodTotalTime > 2:
            total_ticks = 0
            anyPeriod = 0
            periodTotalTime = 0
            period = period + 1
            resetRink(playerOffense,computerOffense,playerDefense,computerDefense,playerGoalie,computerGoalie)

        if endOfGame:
            endTime = time.perf_counter()
            endOfGame = 0
        if anyGame:
            timeTracker = time.perf_counter()
            endTotalTime = timeTracker - endTime
        if endTotalTime > 2:
            anyGame = 0
            endTotalTime = 0
            gameLoop = 0

        if period == 1:
            periodForSB = "st"
            glovars.message_display(str(period),1024-210,5,glovars.periodFont, glovars.black)
            glovars.message_display(periodForSB,1024-195,6,glovars.periodFontSmall, glovars.black)
        elif period == 2:
            periodForSB = "nd"
            glovars.message_display(str(period),1024-215,5,glovars.periodFont, glovars.black)
            glovars.message_display(periodForSB,1024-193,9,glovars.periodFontSmall, glovars.black)
        elif period == 3:
            periodForSB = "rd"
            glovars.message_display(str(period),1024-210,5,glovars.periodFont, glovars.black)
            glovars.message_display(periodForSB,1024-188,9,glovars.periodFontSmall, glovars.black)
        elif period == 4:
            periodForSB = "OT"
            glovars.message_display(periodForSB,1024-218,5,glovars.periodFont, glovars.black)
            
        pygame.draw.rect(glovars.screen,glovars.black,(0,0,175,50),0)
##        pygame.draw.rect(glovars.screen,glovars.lightGrey,(1024-145,0,145,50),0)
        pygame.draw.rect(glovars.screen,glovars.lightGrey,(170,0,10,50),0)
        
        
        pygame.draw.rect(glovars.screen,glovars.lightGrey,(1024-148,0,6,50),0)
        pygame.draw.rect(glovars.screen,glovars.lightGrey,(1024-246,0,11,50),0)
        glovars.message_display("GKHA",20,9,glovars.ESPN,glovars.white)
        glovars.message_display("G",20,9,glovars.ESPN,glovars.googusGreen)
        
        glovars.message_display(mins_remain + ":" + secs_remain,1024-122,7, glovars.timeFont, glovars.black)

        if team1score > 19:
            glovars.message_display(str(team1score),717,1,glovars.scoreFont,glovars.white)
        elif team1score > 9:
            glovars.message_display(str(team1score),420,1,glovars.scoreFont,glovars.white)
        else:
            glovars.message_display(str(team1score),428,1,glovars.scoreFont,glovars.white)
        if team2score > 19:
            glovars.message_display(str(team2score),717,1,glovars.scoreFont,glovars.white)
        elif team2score > 9:
            glovars.message_display(str(team2score),720,1,glovars.scoreFont,glovars.white)
        else:
            glovars.message_display(str(team2score),728,1,glovars.scoreFont,glovars.white)


        pygame.draw.rect(glovars.screen,glovars.black,(0,0,1024,1),0)
        pygame.draw.rect(glovars.screen,glovars.black,(0,49,1024,1),0)
        pygame.draw.rect(glovars.screen,glovars.black,(1023,0,1,50),0)
        pygame.draw.rect(glovars.screen,glovars.black,(1024-236,0,1,50),0)
        pygame.draw.rect(glovars.screen,glovars.black,(180,0,1,50),0)
        
        shotOrNot = 0
        goalBallContact = 0
        ballContact = 0
        clock.tick(120)
        pygame.display.flip()

    while endLoop == 1:
        glovars.screen.fill(glovars.black)
        paused = 1
        top = pygame.draw.rect(glovars.screen,glovars.white,(0,0,1024,313),0)
        bottom = pygame.draw.rect(glovars.screen,yellow,(0,313,1024,313),0)
        glovars.message_display(oppTeam.name + " " + str(team1score),47,53,EA,glovars.black)
        glovars.message_display(yourTeam.name + " " + str(team2score),47,366,EA,glovars.black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endLoop = 0
                break
        if event.type == pygame.KEYDOWN and paused == 1:
                if event.key==K_i:
                    endLoop = mainMenuGo(0)
        if endLoop == 0:
            break
        clock.tick(120)
        pygame.display.flip()

