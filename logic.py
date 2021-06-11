import pygame

import glovars

def sortFunc(e):
    return e["points"]

#logic to calculate which team is top of the rankings and then sorts them accordingly
def calculateRankings(f):

    teampoints = [{"mascot": "Thunder", "name": "Alaskan Thunder", "points": 0},
    {"mascot": "Revolution", "name": "American Revolution", "points": 0},
    {"mascot": "Whales", "name": "Boondock Beluga Whales", "points": 0},
    {"mascot": "Tropics", "name": "Florida Tropics", "points": 0},
    {"mascot": "Chippewas", "name": "Smashville Chippewas", "points": 0},
    {"mascot": "Spartans", "name": "Southside Spartans", "points": 0}]

    teamdata = f["teamdata"][0]
    for i in range(len(teamdata)):
        teampoints[i]["points"] = (teamdata[glovars.defaultTeams[i].name][0]["wins"] * 2) + (teamdata[glovars.defaultTeams[i].name][0]["overtimelosses"])

    teampoints.sort(reverse=True, key=sortFunc)

    return teampoints

    
