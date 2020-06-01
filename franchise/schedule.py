import pygame
import random

import glovars


def getRegseason(length):
    fullseason = []
    for i in range(int(length / 10)):
        fullseason.append([[1,0],[4,2],[5,3]])
        fullseason.append([[2,0],[1,3],[4,5]])
        fullseason.append([[3,0],[1,2],[5,4]])
        fullseason.append([[4,0],[1,5],[3,2]])
        fullseason.append([[5,0],[4,1],[2,3]])
        fullseason.append([[0,1],[5,2],[4,3]])
        fullseason.append([[0,2],[5,1],[3,4]])
        fullseason.append([[0,3],[1,4],[2,5]])
        fullseason.append([[0,4],[2,1],[3,5]])
        fullseason.append([[0,5],[3,1],[2,4]])
    for i in range(len(fullseason)):
        random.shuffle(fullseason[i])
    random.shuffle(fullseason)
    return fullseason


def getPreseason():

    teams = [0,1,2,3,4,5]
    random.shuffle(teams)

    match1 = [teams[0], teams[1]]
    match2 = [teams[2], teams[3]]
    match3 = [teams[4], teams[5]]

    return[match1, match2, match3]


def createSchedule(length):

    season = [None] * (1 + length)

    preseason = getPreseason()
    regseason = getRegseason(length)

    season[0] = preseason

    for i in range(length):
        season[i+1] = regseason[i]
    
    return season