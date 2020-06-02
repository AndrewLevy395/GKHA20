import pygame
import defaultPlayer


class DefaultTeam:
    def __init__ (self, name, offense, defense, goalie, scorebug, selectImage, franchiseImage, overall):
        self.name = name

        self.offense = offense
        self.offense.position = "offense"
        self.defense = defense
        self.defense.position = "defense"
        self.goalie = goalie
        self.goalie.position = "goalie"

        self.scorebug = scorebug
        self.selectImage = selectImage
        self.franchiseImage = franchiseImage
        self.overall = overall #will be calculated by players later

def createAll():
    ala = DefaultTeam("Alaskan Thunder", defaultPlayer.rockOffense, defaultPlayer.andyLevy, defaultPlayer.rickyNovia, 
    pygame.image.load("assets/images/alaSB.png"), pygame.image.load("assets/images/alaPN.png"), pygame.image.load("assets/images/alaFP.png"), 6)
    ame = DefaultTeam("American Revolution", defaultPlayer.mikeyPapa, defaultPlayer.rockDefense, defaultPlayer.mikeMarotta, 
    pygame.image.load("assets/images/ameSB.png"), pygame.image.load("assets/images/amePN.png"), pygame.image.load("assets/images/ameFP.png"), 7)
    bbw = DefaultTeam("Boondock Beluga Whales", defaultPlayer.austinIngarra, defaultPlayer.rockDefense, defaultPlayer.alecFowler,
    pygame.image.load("assets/images/bbwSB.png"), pygame.image.load("assets/images/bbwPN.png"), pygame.image.load("assets/images/bbwFP.png"), 6)
    flo = DefaultTeam("Florida Tropics", defaultPlayer.rockOffense, defaultPlayer.chrisHorowitz, defaultPlayer.collinSalatto,
    pygame.image.load("assets/images/floSB.png"), pygame.image.load("assets/images/floPN.png"), pygame.image.load("assets/images/floFP.png"), 7)
    smc = DefaultTeam("Smashville Chippewas", defaultPlayer.salDelucia, defaultPlayer.rockDefense, defaultPlayer.thomBishop,
    pygame.image.load("assets/images/smcSB.png"), pygame.image.load("assets/images/smcPN.png"), pygame.image.load("assets/images/smcFP.png"), 7)
    sss = DefaultTeam("Southside Spartans", defaultPlayer.chrisPapa, defaultPlayer.rockDefense, defaultPlayer.mattPalma,
    pygame.image.load("assets/images/sssSB.png"), pygame.image.load("assets/images/sssPN.png"), pygame.image.load("assets/images/sssFP.png"), 7)
    teams = [ala, ame, bbw, flo, smc, sss]
    return teams


bcp = DefaultTeam("Bamar Crab People", defaultPlayer.austinIngarra, defaultPlayer.andyLevy, defaultPlayer.mikeMarotta,
pygame.image.load("assets/images/bcpSB.png"), pygame.image.load("assets/images/bcpPN.png"), pygame.image.load("assets/images/sssFP.png"), "P")