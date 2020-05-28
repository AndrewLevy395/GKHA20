import pygame

class DefaultTeam:
    def __init__ (self, name, offense, defense, goalie, scorebug, selectImage, overall):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.goalie = goalie
        self.scorebug = scorebug
        self.selectImage = selectImage
        self.overall = overall #will be calculated by players later

def createAll():
    ala = DefaultTeam("Alaskan Thunder","bob","andy","ricky","alaSB", pygame.image.load("assets/images/alaPN.png"), 6)
    ame = DefaultTeam("American Revolution","bob","andy","ricky","alaSB", pygame.image.load("assets/images/amePN.png"), 7)
    bbw = DefaultTeam("Boondock Beluga Whales","bob","andy","ricky","alaSB", pygame.image.load("assets/images/bbwPN.png"), 6)
    flo = DefaultTeam("Florida Tropics","bob","andy","ricky","alaSB", pygame.image.load("assets/images/floPN.png"), 7)
    smc = DefaultTeam("Smashville Chippewas","bob","andy","ricky","alaSB", pygame.image.load("assets/images/smcPN.png"), 7)
    sss = DefaultTeam("Southside Spartans","bob","andy","ricky","alaSB", pygame.image.load("assets/images/sssPN.png"), 7)
    teams = [ala, ame, bbw, flo, smc, sss]
    return teams