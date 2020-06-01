import pygame
import math


#sprite class
class Player(pygame.sprite.Sprite):
    def __init__ (self,width1,height1,x,y,speed,shotSpeed,reaction,image,job,name,captain,forScore,goalScore,sizeRank,speedRank,powerRank,reactionRank):
        pygame.sprite.Sprite.__init__(self)
        self.width1 = width1
        self.height1 = height1
        self.radius = max(width1,height1)/2
        self.shootradius = 115
        self.x = x+self.radius
        self.y = y+self.radius
        self.initX = x+self.radius
        self.initY = y+self.radius
        
        #used for movement to past spots
        self.oldx = self.initX
        self.oldy = self.initY
        self.goldx = self.initX
        self.goldy = self.initY
        self.groldx = self.initX
        self.groldy = self.initY
        
        self.speed = speed
        self.shotSpeed = shotSpeed

        #limited for different positions
        self.goalSpeed = 150/2.3
        self.forwardSpeed = speed/1.05
        self.reaction = reaction
        
        self.image = image
        
        #job: goalie = 0, player = 1, forward = 2
        self.job = job
        
        self.angle = 0
        self.mass = 2000
        self.rect = self.image.get_rect(topleft = (self.x-self.radius,self.y-self.radius))
        self.mask  = pygame.mask.from_surface(self.image)

        #statistics
        self.name = name
        self.captain = captain
        self.forScore = forScore
        self.goalScore = goalScore
        self.sizeRank = sizeRank
        self.speedRank = speedRank
        self.powerRank = powerRank
        self.reactionRank = reactionRank

        #player movement, varied for different jobs/locations
    def move(self,up,down,left,right,time_delta):
        dx, dy = self.x, self.y
        self.groldx = self.goldx
        self.groldy = self.goldy
        self.goldx = self.oldx
        self.goldy = self.oldy
        self.oldx = self.x
        self.oldy = self.y
        if self.job == 1:
            self.x += (right - left)*self.speed*time_delta
            self.y += (down - up)*self.speed*time_delta
        if self.job == 0:
            self.x += (right - left)*self.goalSpeed*time_delta
            self.y += (down - up)*self.goalSpeed*time_delta
        if self.job == 2:
            self.x += (right - left)*self.forwardSpeed*time_delta
            self.y += (down - up)*self.forwardSpeed*time_delta
        dx = self.x-dx
        dy = self.y-dy
        self.angle = math.atan2(dy, dx)
        

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
playerRock = Player(204,138,461,250,150,400,1,rock,1," ",False,1,1,1,1,1,1)
#andyLevyFF = Player(124,156,455,265,200,390,4,andyL,1,"Andy Levy",True,7,4,5,10,5,6)

andyLevyFF = Player(124,175,455,265,200,390,4,andyL,1,"Andy Levy",True,7,4,5,10,5,6)

chrisPapaFF = Player(146,172,455,265,175,450,5,chrisP,1,"Chris Papa",True,10,4,8,6,10,7)
salDeluciaFF = Player(132,164,455,265,175,380,3,salD,1,"Sal Delucia",False,5,5,6,6,4,4)
mikeyPapaFF = Player(124,164,455,265,185,420,6,mikeyP,1,"Mikey Papa",False,9,7,6,8,8,8)
austinIngarraFF = Player(148,168,455,265,170,410,4,austinI,1,"Austin Ingarra",True,7,6,8,5,7,6)
chrisHorowitzFF = Player(140,170,455,265,170,390,4,chrisH,1,"Chris Horowitz",False,6,4,8,5,5,6)
#forwards
andyLevyOF = Player(124,156,344,154,200,390,4,andyL,2,"Andy Levy",True,7,4,5,10,5,6)
chrisPapaOF = Player(146,172,344,154,175,450,5,chrisP,2,"Chris Papa",True,10,4,8,6,10,7)
salDeluciaOF = Player(132,164,344,154,175,380,3,salD,2,"Sal Delucia",False,5,5,6,6,4,4)
mikeyPapaOF = Player(124,164,344,154,185,420,6,mikeyP,2,"Mikey Papa",False,9,7,6,8,8,8)
austinIngarraOF = Player(148,168,344,154,170,410,4,austinI,2,"Austin Ingarra",True,7,6,8,5,7,6)
chrisHorowitzOF = Player(140,170,344,154,170,390,4,chrisH,2,"Chris Horowitz",False,6,4,8,5,5,6)
#goalieOpposing
mikeMarottaOG = Player(136,156,130,220,180,440,6,mikeM,0,"Mike Marotta",True,6,9,7,7,9,9)
tomBishopOG = Player(136,156,130,220,170,390,7,tomB,0,"Tom Bishop",True,7,9,6,5,5,10)
alecFowlerOG = Player(140,170,130,220,190,400,5,alecF,0,"Alec Fowler",False,5,7,8,9,6,7)
collinSalattoOG = Player(156,174,130,220,150,410,3,collinS,0,"Collin Salatto",True,2,9,10,2,7,4)
mattPalmaOG = Player(150,160,130,220,155,400,4,mattP,0,"Matt Palma",False,4,6,9,3,6,6)
rickyNoviaOG = Player(124,156,130,220,190,380,4,rickyN,0,"Ricky Novia",False,5,5,5,9,4,6)
#goalieFor
tomBishopFG = Player(136,156,664,220,170,390,7,tomB,0,"Tom Bishop",True,7,9,6,5,5,10)
mikeMarottaFG = Player(136,156,664,220,180,440,6,mikeM,0,"Mike Marotta",True,6,9,7,7,9,9)
alecFowlerFG = Player(140,170,664,220,190,400,5,alecF,0,"Alec Fowler",False,5,7,8,9,6,7)
collinSalattoFG = Player(156,174,664,220,150,410,3,collinS,0,"Collin Salatto",True,2,9,10,2,7,4)
mattPalmaFG = Player(150,160,664,220,155,400,4,mattP,0,"Matt Palma",False,4,6,9,3,6,6)
rickyNoviaFG = Player(124,156,664,220,190,380,4,rickyN,0,"Ricky Novia",False,5,5,5,9,4,6)