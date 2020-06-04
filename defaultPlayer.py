import pygame
import math


#sprite class
class Player(pygame.sprite.Sprite):

    def __init__(self, name, sprite, stamina, shotAccuracy, shotSpeed, speed, reaction):
        pygame.sprite.Sprite.__init__(self)

        #create image
        self.image = pygame.image.load(sprite)
        self.sprite = sprite

        #size
        self.size = self.image.get_rect().size
        self.w = self.size[0] * 2
        self.h = self.size[1] * 2
        self.radius = max(self.w,self.h)/2
        self.shootradius = 115

        #location
        self.x = 0
        self.y = 0
        self.initX = 0
        self.initY = 0
        
        #used for movement to past spots
        self.oldx = self.initX
        self.oldy = self.initY
        self.goldx = self.initX
        self.goldy = self.initY
        self.groldx = self.initX
        self.groldy = self.initY
        
        #attributes
        self.speed = 175 #speed
        self.shotSpeed = 450 #shotSpeed
        self.shotAccuracy = shotAccuracy
        self.stamina = stamina
        self.reaction = reaction

        #limited for different positions
        self.goalSpeed = 150/2.3
        self.forwardSpeed = self.speed/1.05
        
        #info
        self.position = None
        self.name = name
        self.controlled = False
        
        #for physics
        self.angle = 0
        self.mass = 2000

        #for sprite
        self.rect = self.image.get_rect(topleft = (self.x-self.radius,self.y-self.radius))
        self.mask  = pygame.mask.from_surface(self.image)

        #player movement, varied for different position/locations
    def move(self,up,down,left,right,time_delta):
        dx, dy = self.x, self.y
        self.groldx = self.goldx
        self.groldy = self.goldy
        self.goldx = self.oldx
        self.goldy = self.oldy
        self.oldx = self.x
        self.oldy = self.y
        if self.position == "player":
            self.x += (right - left) * self.speed*time_delta
            self.y += (down - up) * self.speed*time_delta
        if self.position == "goalie":
            self.x += (right - left) * self.goalSpeed*time_delta
            self.y += (down - up) * self.goalSpeed*time_delta
        if self.position == "offense" or self.position == "defense":
            self.x += (right - left) * self.forwardSpeed * time_delta
            self.y += (down - up) * self.forwardSpeed * time_delta
        dx = self.x-dx
        dy = self.y-dy
        self.angle = math.atan2(dy, dx)

    def setInitLocation(self, x,y):
        self.x = x + self.radius
        self.y = y + self.radius
        self.initX = x + self.radius
        self.initY = y + self.radius
        
# CREATE ALL PLAYERS

#player sprites
rock = "assets/images/playersprites/rock.png"
chrisP = "assets/images/playersprites/chris.png"
mikeM = "assets/images/playersprites/mikem.png"
andyL = "assets/images/playersprites/andyl.png"
tomB = "assets/images/playersprites/tomb.png"
salD = "assets/images/playersprites/sald.png"
mikeyP = "assets/images/playersprites/mikeyp.png"
collinS = "assets/images/playersprites/collins.png"
alecF = "assets/images/playersprites/alecF.png"
austinI = "assets/images/playersprites/austini.png"
mattP = "assets/images/playersprites/mattp.png"
rickyN = "assets/images/playersprites/rickyN.png"
chrisH = "assets/images/playersprites/chrisH.png"

#player objects for play now
rockOffense = Player("Rock O", rock, 7, 5, 3, 5, 5)
rockDefense = Player("Rock D", rock, 7, 5, 3, 5, 5)

andyLevy = Player("Andy Levy", andyL, 7, 5, 3, 5, 5)
chrisPapa = Player("Chris Papa", chrisP,  8, 9, 9, 5, 5)
salDelucia = Player("Sal Delucia", salD, 3, 3, 3, 5, 5)
mikeyPapa = Player("Mikey Papa", mikeyP, 4, 10, 5, 5, 5)
austinIngarra = Player("Austin Ingarra", austinI, 6, 6, 8, 5, 5)
chrisHorowitz = Player("Chris Horowitz", chrisH, 5, 7, 6, 5, 5)

owenBrown = Player("Owen Brown", rock, 7, 5, 3, 5, 5)
aidanMurray = Player("Aidan Murray", rock, 7, 5, 3, 5, 5)
darrenBarille = Player("Darren Barille", rock, 7, 5, 3, 5, 5)
mattRobidoux = Player("Matt Robidoux", rock, 7, 5, 3, 5, 5)
vinnyCleary = Player("Vinny Cleary", rock, 7, 5, 3, 5, 5)
erikGaluska = Player("Erik Galuska", rock, 7, 5, 3, 5, 5)

mikeMarotta = Player("Mike Marotta", mikeM, 7, 5, 3, 5, 5)
thomBishop = Player("Thom Bishop", tomB, 7, 7, 7, 5, 5)
alecFowler = Player("Alec Fowler", alecF, 7, 5, 3, 5, 5)
collinSalatto = Player("Collin Salatto", collinS, 7, 5, 3, 5, 5)
mattPalma = Player("Matt Palma", mattP, 7, 5, 3, 5, 5)
rickyNovia = Player("Ricky Novia", rickyN, 7, 5, 3, 5, 5)

bradRobidoux = Player("Brad Robidoux", rock, 7, 5, 3, 5, 5)
shemPrudhomme = Player("Shem Prudhomme", rock, 7, 5, 3, 5, 5)
ianBeling = Player("Ian Beling", rock, 7, 5, 3, 5, 5)
jarrettHissick = Player("Jarrett Hissick", rock, 7, 5, 3, 5, 5)
erikLevenduski = Player("Erik Levenduski", rock, 7, 5, 3, 5, 5)
georgeBonadies = Player("George Bonadies", rock, 7, 5, 3, 5, 5)
kyleKulthau = Player("Kyle Kulthau", rock, 7, 5, 3, 5, 5)
kevinCarnale = Player("Kevin Carnale", rock, 7, 5, 3, 5, 5)

franchiseFreeAgents = [bradRobidoux, shemPrudhomme, ianBeling, jarrettHissick, erikLevenduski, georgeBonadies, kyleKulthau, kevinCarnale]