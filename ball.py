import pygame
import math



class Ball(pygame.sprite.Sprite):
    def __init__ (self,x,y,speed,image):
        pygame.sprite.Sprite.__init__(self)
        #only take height because its a circle
        self.height = 30
        self.x = x+self.height/2
        self.y = y+self.height/2
        self.dx = 0
        self.dy = 0
        self.oldx = 0
        self.oldy = 0
        self.speed = speed
        self.image = image
        self.angle = 0
        self.mass = 500
        self.friction = .994
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(487,313))

        #ball movement
    def move(self, time_delta):
        self.oldx = self.x
        self.oldy = self.y
        self.dx = math.sin(self.angle) * self.speed * time_delta
        self.dy = math.cos(self.angle) * self.speed * time_delta
        self.x += self.dx
        self.y -= self.dy
        self.speed *= self.friction
        
    def vector_addition(self, angle1, length1, angle2, length2):
        x = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y = math.cos(angle1) * length1 + math.cos(angle2) * length2

        length = math.hypot(x, y)
        angle = math.pi / 2 - math.atan2(y, x)
        return angle, length

        #collision between player and ball
    def collidePlayer(self, player, shot):
        self.friction = .994
        player.oldx = player.x
        player.oldy = player.y
        self.dx = self.x - player.x
        self.dy = self.y - player.y
        distance = math.hypot(self.dx, self.dy)
        tangent = math.atan2(self.dy, self.dx)
        temp_angle = math.pi / 2 + tangent
        total_mass = self.mass + player.mass
        vec_a = self.speed * (self.mass - player.mass) / total_mass
        vec_b = 2 * player.speed * player.mass / total_mass
        (self.angle, self.speed) = self.vector_addition(self.angle,vec_a,temp_angle,vec_b)
        self.speed =player.shotSpeed
        if shot == 1 or player.job == 0:
            if self.x < player.x:
                self.angle = self.angle + .5
        if shot == 1 or player.job == 0:
            if self.x > player.x:
                self.angle = self.angle - .2
        if self.speed > 500:
            self.speed = 500
        if shot == 0:
            self.speed = player.speed
        if shot == 1:
            if player.job == 1:
                #slapShot.set_volume(0.5)
                #slapShot.play(0,1300)
                #slapShot.set_volume(0.3)
                print("shot noise")
            else:
                #slapShot.play(0,1300)
                print("other shot noise")
        if player.x<150 and shot == 0:
            self.speed = 220
        if player.x>874 and shot == 0:
            self.speed = 220
        vec_speed_a = player.speed * (player.mass - self.mass) / total_mass
        vec_speed_b = 2 * self.speed * self.mass / total_mass
        temp_angle_a = temp_angle + math.pi
        temp_speed = player.speed
        (player.angle, player.speed) = self.vector_addition(player.angle,vec_speed_a,temp_angle_a,vec_speed_b)
        player.speed = temp_speed
        
        offset = 0.05 * (self.height/2 + player.radius - distance + 1)
        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset
        if player.job != 0:
            player.x -= math.sin(temp_angle) * offset
            player.y += math.cos(temp_angle) * offset
        return 
    
    def getVelocities(self):
        x=0
        y=0
        if(self.x-self.oldx > 0):
            x=1
        if(self.y-self.oldy > 0):
            y=1
        return x,y
        
    def shoot(self, player):
        dx = self.x-42 - player.x 
        dy = self.y-30 - player.y 
        distance = math.hypot(dx, dy)
        if distance < self.height/2 + player.shootradius:
            self.collidePlayer(player,1)
        return 1





