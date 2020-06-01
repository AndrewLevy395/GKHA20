import pygame
import math


#sprite class
class Player(pygame.sprite.Sprite):

    def __init__(self, name, image, position, stamina, shotAccuracy, shotSpeed, speed, reaction):
        pygame.sprite.Sprite.__init__(self)

        #size
        self.size = image.get_rect().size
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
        self.image = image
        self.position = position
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
        

rock = pygame.image.load("assets/images/rock.png")
chrisP = pygame.image.load("assets/images/chris.png")
mikeM = pygame.image.load("assets/images/mikem.png")
andyL = pygame.image.load("assets/images/andyl.png")
tomB = pygame.image.load("assets/images/tomb.png")
salD = pygame.image.load("assets/images/sald.png")
mikeyP = pygame.image.load("assets/images/mikeyp.png")
collinS = pygame.image.load("assets/images/collins.png")
alecF = pygame.image.load("assets/images/alecF.png")
austinI = pygame.image.load("assets/images/austini.png")
mattP = pygame.image.load("assets/images/mattp.png")
rickyN = pygame.image.load("assets/images/rickyN.png")
chrisH = pygame.image.load("assets/images/chrisH.png")


#playerControlled
playerRock = Player("Rock", rock, "defense", 7, 5, 3, 5, 5)
#andyLevyFF = Player(124,156,455,265,200,390,4,andyL,1,"Andy Levy",True,7,4,5,10,5,6)

andyLevy = Player("Andy Levy", andyL, "defense", 7, 5, 3, 5, 5)
chrisPapa = Player("Chris Papa", chrisP, "offense", 8, 9, 9, 5, 5)
salDelucia = Player("Sal Delucia", salD, "offense", 3, 3, 3, 5, 5)
mikeyPapa = Player("Andy Levy", mikeyP, "offense", 4, 10, 5, 5, 5)
austinIngarra = Player("Andy Levy", austinI, "offense", 6, 6, 8, 5, 5)
chrisHorowitz = Player("Andy Levy", chrisH, "defense", 5, 7, 6, 5, 5)

mikeMarotta = Player("Mike Marotta", mikeM, "goalie", 7, 5, 3, 5, 5)
thomBishop = Player("Thom Bishop", tomB, "goalie", 7, 7, 7, 5, 5)
alecFowler = Player("Alec Fowler", alecF, "goalie", 7, 5, 3, 5, 5)
collinSalatto = Player("Collin Salatto", collinS, "goalie", 7, 5, 3, 5, 5)
mattPalma = Player("Matt Palma", mattP, "goalie", 7, 5, 3, 5, 5)
rickyNovia = Player("Ricky Novia", rickyN, "goalie", 7, 5, 3, 5, 5)