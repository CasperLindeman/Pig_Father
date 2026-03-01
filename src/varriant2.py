"""
Created on Sat Dec  7 13:13:38 2019
@author: Casper
Nåvernende verdensrekord: 88 sekunder / 1 min og 28 sekunder. Holdes av: Casper Lindeman
"""
import os
os.chdir(r"C:\VScode\metroidvania")

import pygame
pygame.init()

winHeight = int(1000 * 0.75)
winWidth = int(winHeight * 1.6)
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Pig Father")

djeveldør = pygame.image.load('djeveldør.png')
grisdead = pygame.image.load('gris.png')


krone_png = pygame.image.load('krone_2.png')
bullet_R = pygame.image.load('bullet_R_2.png')
bullet_L = pygame.image.load('bullet_L_2.png')

darkRoomEnt = pygame.image.load('darkroom_2.png')
bro = pygame.image.load('bro_1_2.png')
bg = pygame.image.load('bg_1_2.png')
gulv1 = pygame.image.load('gulv_1_2.png')


room3_1 = pygame.image.load('room3_1_2.png')
bg3 = pygame.image.load('bgs_2.jpg')
portal = pygame.image.load('portal_2.png')
hindring1_png = pygame.image.load('hindring1_2.png')
hindring2_png = pygame.image.load('hindring2_2.png')
hindring3_png = pygame.image.load('hindring3_2.png')
hindring3_1 = hindring1_png

DRGulv = pygame.image.load('gulv_2_2.png')
jumpBord = pygame.image.load('jumpbord_2.png')
floorRoom2 = pygame.image.load('gulv_2_2_2.png')
levitasjon = pygame.image.load('levitasjon_2.png')


bg4 = pygame.image.load('bg4_2.png')
w = pygame.image.load('w_2.png')
floor4 = pygame.image.load('floor4_2.png')

fakkel = pygame.image.load('fakkel_2.png')

bg6 = pygame.image.load('bg6_2.png')
gud1 = pygame.image.load('gud1_2.png')
gud2 = pygame.image.load('gud2_2.png')
gud3 = pygame.image.load('gud3_2.png')

clock = pygame.time.Clock()

class man(object):
    def __init__(self, x, y, width, height, colour, health, damagecooldown, hit, bounce, bouncetime):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6 * 0.75
        self.isJump = False
        self.jump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.colour = colour
        self.djevel = False
        self.health = health
        self.damagecooldown = damagecooldown
        self.hit = hit
        self.bounce = bounce
        self.bouncetime = bouncetime
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (man.x , man.y, man.width, man.height))
         

class enemy(object):
    def __init__(self, x, y, width, height, count, feet, health1, health2, health3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk = 450
        self.count = count
        self.vel = 2
        self.feet = feet
        self.health1 = health1
        self.health2 = health2
        self.health3 = health3
    
    def draw(self, win):
        if self.health3 > 0:
            pygame.draw.rect(win, (225, 0, 225), (self.x , self.y, 200, 200))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 50, self.y + 50, 100, 100))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 30, self.y + 60, 20, 20))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 150, self.y + 60, 20, 20))
            pygame.draw.rect(win, white, (self.x + 65, self.y + 65, 20, 30))
            pygame.draw.rect(win, white, (self.x + 115, self.y + 65, 20, 30))
            pygame.draw.rect(win, black, (self.x + 70, self.y + 75, 10, 10))
            pygame.draw.rect(win, black, (self.x + 120, self.y + 75, 10, 10))
            pygame.draw.rect(win, black, (self.x + 48, self.y + 48, 104, 104), 2)
            pygame.draw.rect(win, black, (self.x + 29, self.y + 60, 20, 20), 2)
            pygame.draw.rect(win, black, (self.x + 151, self.y + 60, 20, 20), 2)
            pygame.draw.rect(win, black, (self.x + 65, self.y + 65, 20, 30), 2)
            pygame.draw.rect(win, black, (self.x + 115, self.y + 65, 20, 30), 2)
            pygame.draw.rect(win, black, (self.x + 84, self.y + 100, 32, 32), 2)
            pygame.draw.rect(win, black, (self.x + 90, self.y + 109, 7, 15))
            pygame.draw.rect(win, black, (self.x + 103, self.y + 109, 7, 15))
            pygame.draw.rect(win, black, (self.x + 83, self.y + 137, 36, 5))
            if enemy.health3 > 0:
                if self.walk % 2 == 0:
                    if self.feet != 20:
                        self.feet += 1
                    elif self.feet == 20:
                        self.feet = 0
            if self.feet < 11:
                pygame.draw.rect(win, (100, 0, 100), (self.x + 20, self.y + 200 + self.feet, 50, 28))
                pygame.draw.rect(win, (100, 0, 100), (self.x + 130, self.y + 210 - self.feet, 50, 28))
                pygame.draw.rect(win, (255, 0, 255), (self.x + 10, self.y + 200 + self.feet, 50, 30))
                pygame.draw.rect(win, (255, 0, 255), (self.x + 140, self.y + 210 - self.feet, 50, 30))   
            elif self.feet > 10:
                pygame.draw.rect(win, (100, 0, 100), (self.x + 20, self.y + 220 - self.feet, 50, 28))
                pygame.draw.rect(win, (100, 0, 100), (self.x + 130, self.y + 190 + self.feet, 50, 28))
                pygame.draw.rect(win, (255, 0, 255), (self.x + 10, self.y + 220 - self.feet, 50, 30))
                pygame.draw.rect(win, (255, 0, 255), (self.x + 140, self.y + 190 + self.feet, 50, 30))
            if enemy.health1 < 8:
                if enemy.health1 < 1:
                    pygame.draw.rect(win, (100, 0, 0), (self.x + 20, self.y + 160, 80, 37))
                    pygame.draw.rect(win, black, (self.x + 114, self.y + 137, 5, 12))
                    pygame.draw.rect(win, black, (self.x + 111, self.y + 137, 8, 8))
                    pygame.draw.rect(win, black, (self.x + 83, self.y + 137, 5, 12))
                    pygame.draw.rect(win, black, (self.x + 83, self.y + 137, 8, 8)) 
                    pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 100, 5, 10))
                    pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 115, 5, 10))
                    pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 130, 5, 10))
                pygame.draw.rect(win, (100, 0, 0), (self.x, self.y + 100, 10, 10))
                if enemy.health1 < 7:
                    pygame.draw.rect(win, (255, 0, 0), (enemy.x + 3, enemy.y + 20, 5, 15))
                    if enemy.health1 < 6:
                        pygame.draw.rect(win, (255, 0, 0), (enemy.x + 15, enemy.y + 60, 10, 30))
                        if enemy.health1 < 5:
                            pygame.draw.rect(win, (220, 0, 0), (enemy.x + 5, enemy.y + 115, 40, 50))
                            if enemy.health1 < 4:
                                pygame.draw.rect(win, (170, 0, 0), (enemy.x, enemy.y + 175, 70, 20))                      
                                if enemy.health1 < 3:
                                    pygame.draw.rect(win, (70, 0, 0), (enemy.x + 40, enemy.y + 80, 5, 30))
                                    if enemy.health1 < 2:
                                        pygame.draw.rect(win, (100, 0, 0), (enemy.x + 10, enemy.y + 120, 30, 40))
            if enemy.health2 < 8:
                pygame.draw.rect(win, (100, 0, 0),(enemy.x + enemy.width - 20, enemy.y + 120, 20, 10))
                if enemy.health2 < 7:
                    pygame.draw.rect(win, (240, 0, 0),(enemy.x + enemy.width - 45, enemy.y + 100, 10, 10))
                    if enemy.health2 < 6:
                        pygame.draw.rect(win, (70, 0, 0),(enemy.x + enemy.width - 30, enemy.y + 60, 30, 18))
                        if enemy.health2 < 5:
                            pygame.draw.rect(win, (250, 0, 0),(enemy.x + enemy.width - 100, enemy.y + 155, 95, 40))
                            if enemy.health2 < 4:
                                pygame.draw.rect(win, (167, 0, 0),(enemy.x + enemy.width - 20,enemy.y + 137, 15, 17))
                                if enemy.health2 < 3:
                                    pygame.draw.rect(win, (200, 0, 0),(enemy.x + enemy.width - 35, enemy.y + 115, 10, 5))
                                    if enemy.health2 < 2:
                                        pygame.draw.rect(win, (100, 0, 0),(enemy.x + enemy.width - 90, enemy.y + 160, 65, 30))
                                        if enemy.health2 < 1:
                                            pygame.draw.rect(win, (40, 0, 0),(enemy.x + enemy.width - 80, enemy.y + 165, 45, 20))
                                            pygame.draw.rect(win, (0, 0, 200), (enemy.x + 120, enemy.y + 100, 5, 10))
                                            pygame.draw.rect(win, (0, 0, 200), (enemy.x + 120, enemy.y + 115, 5, 10))
                                            pygame.draw.rect(win, (0, 0, 200), (enemy.x + 120, enemy.y + 130, 5, 10))
            if enemy.health1 > 0 or enemy.health2 > 0:
                pygame.draw.rect(win, (100, 100, 100), (self.x, self.y, 200, 25))
                pygame.draw.rect(win, (140, 140, 140), (self.x + 93, self.y - 10, 16, 10))
                pygame.draw.rect(win, (70, 70, 70), (self.x, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 30, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 60, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 195, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 165, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 135, self.y - 5, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x - 5, self.y + 10, 5, 5))
                pygame.draw.rect(win, (70, 70, 70), (self.x + 200, self.y + 10, 5, 5))
                if enemy.health1 > 0 and enemy.health2 > 0:
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 15, self.y - 10, 5, 10))
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 45, self.y - 10, 5, 10))
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 75, self.y - 10, 5, 10))
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 180, self.y - 10, 5, 10))
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 150, self.y - 10, 5, 10))
                    pygame.draw.rect(win, (85, 85, 85), (self.x + 120, self.y - 10, 5, 10)) 
                    pygame.draw.rect(win, (140, 140, 140), (self.x + 97, self.y - 20, 8, 10))
                    pygame.draw.rect(win, (140, 140, 140), (self.x + 100, self.y - 30, 2, 10))
            if enemy.health3 < 8:
                pygame.draw.rect(win, (240, 0, 0),(self.x + 80, self.y, 20, 30))
                if enemy.health3 < 7:
                    pygame.draw.rect(win, (140, 0, 0),(self.x + 83, self.y + 3, 14, 24))
                    if enemy.health3 < 6:
                        pygame.draw.rect(win, (200, 0, 0),(self.x, self.y, 40, 50))
                        if enemy.health3 < 5:
                            pygame.draw.rect(win, (120, 0, 0),(self.x + 150, self.y + 20, 15, 10))
                            if enemy.health3 < 4:
                                pygame.draw.rect(win, (180, 0, 0),(self.x + 60, self.y + 35, 30, 10))
                                if enemy.health3 < 3:
                                    pygame.draw.rect(win, (150, 0, 0),(self.x + 85, self.y + 55, 6, 10))
                                    pygame.draw.rect(win, (150, 0, 0),(self.x + 100, self.y, 80, 40))
                                    if enemy.health3 < 2:
                                        pygame.draw.rect(win, (200, 0, 0),(self.x + 55, self. y + 100, 20, 40))
        if enemy.health3 <= 0:
            win.blit(grisdead,(self.x, self.y + 35))
            
class krone(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isKrone = False
        
    def draw(self, win):
        win.blit(krone_png, (krone.x, krone.y))
    
class jumpAb(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,200,200), (jumpAb.x, jumpAb.y, jumpAb.width, jumpAb.height))

class plat1(object):
    def __init__(self, x, y, width, height, sprite):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite = sprite
        
    def draw(self, win):
        win.blit(self.sprite, (self.x, self.y))

class plat2(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
        
class plat3(object):
    def __init__(self, x ,y, width, height, vel, facing, walk, count):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.facing = facing
        self.count = count
        self.walk = walk
    
    def draw(self, win):
        if not(self.facing):
            if self.walk > 0:
                self.y += self.vel
                self.walk -= 1
            elif self.walk > - self.count:
                self.y -= self.vel
                self.walk -= 1
            else: self.walk = self.count
        elif self.facing:
            if self.walk > 0:
                self.x += self.vel
                self.walk -= 1
            elif self.walk > - self.count:
                self.x -= self.vel
                self.walk -= 1
            else: self.walk = self.count
        pygame.draw.rect(win, (150, 0, 150), (self.x, self.y, self.width, self.height))
        
        
class projectile(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 10 * 0.75 * facing
    
    def draw(self, win):
        win.blit(bullet_png, (self.x, self.y))
    
class hindring(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health 
        
    def draw(self, win):
        win.blit(hindring3_1, (self.x, self.y))

class hindring2(object):
    def __init__(self, x, y, width, height, health, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health 
        self.colour = colour
        
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))

kode1 = False
kode2 = False
kode3 = False
kode4 = False
kode5 = False
koden = False
bullets = []
game2 = False
damagecooldown = 30
grav = 10 * 0.75
room = 1
gudCount = 1
dialogsleep = 0
room6count = 100
black = (0, 0, 0)
darkRed = (100, 0, 0)
darkYellow = (0,100, 100)
white = (255, 255, 255)
pink = (255, 0, 255)
colour = pink
secret = False
man = man(winWidth * 0.375, winHeight * 0.815, winWidth * 0.05 / 1.6, winHeight * 0.05, pink, 5, 0, False, False, 0)
krone = krone(man.x, man.y - winHeight * 0.05, winWidth * 0.05 / 1.6, winHeight * 0.05)
enemy = enemy(350, 460, 200 ,300, 300, 0, 8, 8, 8)
jumpAb = jumpAb(winWidth * 0.07625, winHeight * 0.790, winWidth * 0.02 / 1.6, winHeight * 0.02)
plat2_1 = plat2(0, 400, 30, 250, (100, 100, 100))
plat3_1 = plat1(winWidth * 0.625, winHeight * 0.765, winWidth * 0.4375, winHeight * 0.1, room3_1)
plat3_2 = plat1(winWidth * 0.84375, winHeight * 0.765 - plat3_1.height, winWidth * 0.4375, winHeight * 0.104, room3_1)
plat3_3 = plat1(winWidth * 0.3125, winHeight * 0.765 - plat3_1.height * 2, winWidth * 0.4375, winHeight * 0.104, room3_1)
plat3_4 = plat1(winWidth * -0.125, winHeight * 0.765 - plat3_1.height * 2, winWidth * 0.4375, winHeight * 0.104, room3_1)
portal1 = plat1(0, winHeight * 0.165, winWidth * 0.125, winHeight * 0.4, portal)
etg2Room2 = plat1(0, winHeight * 0.565, winWidth, winHeight * 0.05, floorRoom2)
plat5_1 = plat2(0, winHeight * 0.550, winWidth * 0.1875, winHeight * 0.02, black)
plat5_2 = plat2(winWidth * 0.8125, winHeight * 0.55, winWidth * 0.187500, winHeight * 0.02, black)
plat5_3 = plat2(winWidth * 0.1875, winHeight * 0.425, winWidth * 0.09375, winHeight * 0.04, black)
plat5_4 = plat2(winWidth * 0.3125, winHeight * 0.3, winWidth * 0.09375, winHeight * 0.04, black)
plat5_5 = plat2(winWidth * 0.5, winHeight * 0.175, winWidth * 0.09375, winHeight * 0.04, black)
plat5_6 = plat2(winWidth * 0.78125, winHeight * 0.3, winWidth * 0.125, winHeight * 0.04, black)
plat5_7 = plat2(winWidth * 0.90625, winHeight * 0.175, winWidth * 0.125, winHeight * 0.04, black)
hindring3 = hindring(winWidth * 0.25, winHeight * 0.165, winWidth * 0.046875, winHeight * 0.4, 5)
hindring7 = hindring2(winWidth * 0.75, 0, 10, 200, 3, darkRed)
plat7_1 = plat2(0, winHeight * 0.95, winWidth, 100, darkRed)
plat7_2 = plat2(0, winHeight * 0.95 - 200, 20, 200, darkYellow)
plat7_3 = plat2(1180, 0, 20, 200, darkYellow)
plat7_4 = plat2(winWidth * 0.75 - 40, hindring7.height, 100, 100, white)
plat7_5 = plat2(0, winHeight * 0.95 - 230, winWidth * 0.5, 30, darkRed)
plat7_6 = plat2(0, plat7_5.y - 100, 20, 100, (0, 255, 0))
plat7_7 = plat2(1180, plat7_5.y - 200, 20, 100, (0, 255, 0))
plat7_8 = plat2(0, plat7_5.y - 200, 20, 100, (255, 255, 0 ))
plat7_9 = plat2(1180, plat7_5.y - 300, 20, 100, (255, 255, 0))
plat7_10 = plat2(570, 0, 30, 200, darkRed)
plat7_11 = plat2(0, plat7_5.y - 220, 300, 30, darkRed)
plat7_12 = plat2(400, 0, 10, 100, darkRed)
plat7_13 = plat2(385, 100, 40, 40,(150, 0, 150))
hindring7_2 = hindring2(100, 0, 10, 270, 3, darkRed)
plat8_2 = plat2(1170, 0, 30, winHeight, darkRed)
plat10_1 = plat3(50, 350, 150, 50, 1, False, 300, 450)
plat10_2 = plat3(1000, 500, 150, 50, 1, False, -150, 450)
plat10_3 = plat3(300, 350, 150, 50, 1, True, 450, 450)
plat10_4 = plat3(700, 200, 150, 50, 3, True, 0, 150)

# Alt av sprites kommer her
def sprites():
    global room    
    global hindring3_1
    global hindring1_png
    global hindring2_png
    global hindring3_png
    global room6count
    global secret
    global runtime
    if room == 1:
        win.blit(bg, (0,0))
        win.blit(gulv1, (0, winHeight * 0.815 + man.height))
        pygame.draw.rect(win, (5,5,0), (winWidth * 0.70625 , winHeight * 0.865, winWidth * 0.18125, winHeight * 0.2))
        win.blit(bro, (winWidth * 0.81875, winHeight * 0.865))
        win.blit(darkRoomEnt, (0, winHeight * 0.22))
        if not(man.jump):
            if 350 < man.x < 500 and man.y > 600:
                pygame.draw.rect(win, white, (380, 280, 300, 200))
                message("A and D", black, 400, 300, font)
                message("to move", black, 400, 400, font)
                pygame.draw.rect(win, white, (300, 150, 550, 50))
                message("Top left corner is your health", black, 310, 160, font2)  
         
    elif room == 2:
        win.fill((0, 0, 0))
        win.blit(jumpBord, (winWidth * 0.059375, winHeight * 0.83))
        win.blit(DRGulv, (winWidth * -0.05, winHeight * 0.865))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285, winHeight * 0.865))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285 * 2, winHeight * 0.865))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285 * 3, winHeight * 0.865))
        win.blit(DRGulv, (winWidth * -0.05, winHeight * 0.938))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285, winHeight * 0.938))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285 * 2, winHeight * 0.938))
        win.blit(DRGulv, (winWidth * -0.05 + winWidth * 0.285 * 3, winHeight * 0.938))
        plat2_1.draw(win)
        portal1.draw(win)
        etg2Room2.draw(win)
        win.blit(levitasjon, (winWidth * 0.71875, winHeight * 0.08))
        if not(man.jump):
            jumpAb.draw(win)
        if man.x < winWidth * 0.075:
            if not(krone.isKrone):
                pygame.draw.rect(win, white, (380, 280, 300, 200))
                message("W", black, 480, 300, font)
                message("to jump", black, 400, 400, font)
            
    elif room == 3:
        win.blit(bg3, (0, 0))
        plat3_1.draw(win)
        plat3_2.draw(win)
        plat3_3.draw(win)
        plat3_4.draw(win)
        portal1.draw(win)
        if hindring3.health > 0:
            if hindring3.health == 5:
                hindring3_1 = hindring1_png
            elif 2 < hindring3.health < 5:
                hindring3_1 = hindring2_png
            else:
                hindring3_1 = hindring3_png
            hindring3.draw(win)
        if not(man.djevel):
            if krone.isKrone:
                if man.x > 1050:
                    pygame.draw.rect(win, white, (380, 280, 300, 200))
                    message("SPACE", black, 420, 300, font)
                    message("to shoot", black, 400, 400, font)
        
    elif room == 4:
        win.blit(bg4, (0,0))
        win.blit(floor4, (0, winHeight * 0.665))
        pygame.draw.rect(win, black, (1100, 150, 150, 30))
        if man.y == winHeight * 0.615:
            if winWidth * 0.4875 - man.width < man.x < winWidth * 0.55:
                win.blit(w, (winWidth * 0.4875, winHeight * 0.22))
                pygame.draw.rect(win, white, (winWidth * 0.5, winHeight * 0.245, 40, 30))
                message("E", black, winWidth * 0.51, winHeight * 0.25, font2) 
        if man.x > 990 - man.width or man.y > winHeight * 0.665:
            pygame.draw.rect(win, black, (0, winHeight * 0.765, 1200, winHeight * 0.95 - winHeight * 0.765))
            pygame.draw.rect(win, black, (winWidth * 0.9375, winHeight * 0.665, 100, winHeight * 0.285))
            pygame.draw.rect(win, black, (winWidth * 0.3, winHeight * 0.94, winWidth * 0.1, 200))
            
    elif room == 5:
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (211, 211, 211), (0, winHeight * 0.665, winWidth, winHeight * 0.35))
        plat5_1.draw(win)
        plat5_2.draw(win)
        if koden:
            win.blit(fakkel, (winWidth * 0.21875, winHeight * 0.8))
            win.blit(fakkel, (winWidth * 0.34375, winHeight * 0.8))
            win.blit(fakkel, (winWidth * 0.46875, winHeight * 0.8))
            win.blit(fakkel, (winWidth * 0.59375, winHeight * 0.8))
            win.blit(fakkel, (winWidth * 0.71875, winHeight * 0.8))
            plat5_3.draw(win)
            plat5_4.draw(win)
            plat5_5.draw(win)
            plat5_6.draw(win)
            plat5_7.draw(win)
        else:
            if kode1:
                win.blit(fakkel, (winWidth * 0.218750, winHeight * 0.8))
            if kode2:
                win.blit(fakkel, (winWidth * 0.34375, winHeight * 0.8))
            if kode3:
                win.blit(fakkel, (winWidth * 0.46875, winHeight * 0.8))
            if kode4:
                win.blit(fakkel, (winWidth * 0.59375, winHeight * 0.8))      
            
    if room == 6:
        win.blit(bg6, (0, 0))
        if gudCount == 1:
            win.blit(gud1, (0, 0))
        if gudCount == 2:
            win.blit(gud2, (0, 0))
        if gudCount == 3:
            win.blit(gud3, (0, 0))
    
    if room == 7:
        win.fill((0, 0, 0))
        plat7_1.draw(win)
        plat7_2.draw(win)
        plat7_3.draw(win)
        plat7_5.draw(win)
        plat7_6.draw(win)
        plat7_7.draw(win)
        plat7_8.draw(win)
        plat7_9.draw(win)
        plat7_10.draw(win)
        plat7_11.draw(win)
        if hindring7.health > 0:
            hindring7.draw(win)
        elif plat7_4.y < 600:
            plat7_4.y += 10
        else:
            plat7_4.y = plat7_1.y - 100
        plat7_4.draw(win)
        if 0 < hindring7.health < 3:
            pygame.draw.rect(win, (255, 255, 255), (winWidth * 0.75, 50, 10, 3))
            pygame.draw.rect(win, (255, 255, 255), (winWidth * 0.75, 120, 10, 3))  
        if hindring7_2.health > 0:
            hindring7_2.draw(win)
            plat7_12.draw(win)
            plat7_13.draw(win)
            if 0 < hindring7_2.health < 3:
                pygame.draw.rect(win, (255, 255, 255), (100, 30, 10, 2))
                pygame.draw.rect(win, (255, 255, 255), (100, 90, 10, 2))
                pygame.draw.rect(win, (255, 255, 255), (100, 200, 10, 2)) 
                pygame.draw.rect(win, (255, 255, 255), (400, 70, 10, 2))
        elif plat7_13.y < plat7_5.y - 40:
            plat7_13.y += 10
            plat7_13.draw(win)
        else:
            man.colour = darkRed
            man.djevel = True
        if man.djevel:
            pygame.draw.rect(win, white, (490, 240, 350, 150))
            message("You can now enter", black, 500, 250, font2)
            message("where only devils", black, 500, 300, font2)
            message("are meant to be", black, 500, 350, font2)
        
        
            
            
    if room == 8:
        win.fill((0, 0, 0))
        plat7_1.draw(win)
        plat8_2.draw(win)
        win.blit(djeveldør, (500, 500))
        pygame.draw.rect(win, (255, 155, 0), (500, 500, 10, 210))
        pygame.draw.rect(win, (255, 155, 0), (780, 500, 10, 210))
        pygame.draw.rect(win, (255, 155, 0), (500, 500, 280, 10))
        if man.x > 500 - man.width and man.x < 790:
            pygame.draw.rect(win, (0, 0, 255), (600, 710, 100, 100))
    
    if room == 9:
        win.fill(black)
        pygame.draw.rect(win, (150, 0, 150), (0, 0, 50, 750))
        pygame.draw.rect(win, (150, 0, 150), (0, 700, 1200, 100))
        message("Healing room", white, 400, 200, font)
    
    if room == 10:
        win.fill(black)
        pygame.draw.rect(win, (150, 0, 150), (0, 700, 1200, 100))
        pygame.draw.rect(win, (150, 0, 150), (0,0, 30, 500))
        pygame.draw.rect(win, (150, 0, 150), (1170, 0, 30, 700))
        enemy.draw(win)
        plat10_1.draw(win)
        plat10_2.draw(win)
        plat10_3.draw(win)
        plat10_4.draw(win)
    
    if room == 11:
        secret = True
        win.fill(black)
        message("Created by: Casper Lindeman", white, 200, 250, font)
        
        
    if man.health > 0:
        pygame.draw.rect(win, (255,0,0), (50 + 25 , 50, 20, 20))
    if man.health > 1:
        pygame.draw.rect(win, (255,0,0), (50 * 2 + 25 , 50, 20, 20))
    if man.health > 2:
        pygame.draw.rect(win, (255,0,0), (50 * 3 + 25, 50, 20, 20))
    if man.health > 3:
        pygame.draw.rect(win, (255,0,0), (50 * 4 + 25 , 50, 20, 20))
    if man.health > 4:
        pygame.draw.rect(win,(255, 0, 0), (50 * 5 + 25, 50, 20, 20))
    

    pygame.draw.rect(win, (0,0,0), (50 + 25 , 50, 20, 20), 2)
    pygame.draw.rect(win, (0,0,0), (50 * 2 + 25 , 50, 20, 20), 2)
    pygame.draw.rect(win, (0,0,0), (50 * 3 + 25, 50, 20, 20), 2)
    pygame.draw.rect(win, (0,0,0), (50 * 4 + 25 , 50, 20, 20), 2)
    pygame.draw.rect(win,(0, 0, 0), (50 * 5 + 25, 50, 20, 20), 2)
             
    krone.x = man.x - winWidth * 0.00625
    krone.y = man.y - winHeight * 0.05
    if krone.isKrone:
        krone.draw(win)
        
    for bullet in bullets:
        bullet.draw(win)
    
    if enemy.health3 < 1:
        message("You KILLED Satan", (255, 0, 0), 300, 100, font)
        message("Time:", white, 400, 200, font)
        finaltime = str(runtime)
        message(finaltime, white, 600, 200, font)
        if man.djevel:
            message("Completionist", white, 400, 300, font)
        if runtime < 150:
            message("Speedrunner", white, 400, 400, font)
        if runtime <= 90:
            message("True Master", darkYellow, 500, 400, font)
        if secret:
            message("!!!You found the Secret room!!!", white, 110, 500, font)
            
    man.draw(win)
    pygame.display.update()

#Teleporterefunksjon + annet
def teleport():
    global game2
    global room
    global room6count
    if room == 1:
        if man.x < winWidth * 0.00625:
            room = 2
            man.x = winWidth - man.width - winWidth * 0.03125
        elif man.x > winWidth - man.width - 10:
            room = 3
            man.x = winWidth * 0.031250
            man.y = winHeight * 0.815
            
    elif room == 2:
        if man.x < winWidth * 0.075:
            man.jump = True
        if man.x > winWidth - man.width - winWidth * 0.006250 and man.y > winHeight * 0.6:
            room = 1
            man.x = winWidth * 0.03125
        elif man.x < winWidth * 0.05 and man.y < winHeight * 0.6:
            room = 3
            man.x += winWidth * 0.09375
        elif man.y < 0:
            room = 7
            man.y = winHeight * 0.9
    
    elif room == 3:
        if man.x < winWidth * 0.00625 and man.y > winHeight * 0.6:
            room = 1
            man.x = winWidth - man.width - winWidth * 0.03125
            man.y = winHeight * 0.815
        elif man.x > winWidth - man.width - winWidth * 0.00625:
            man.x = winWidth * 0.0625
            room = 4
        elif man.x < winWidth * 0.05 and man.y < winHeight * 0.6:
            room = 2
            man.x += winWidth * 0.09375
    
    elif room == 4:
        if man.x < 20:
            man.x = winWidth * 0.9375
            #man.y = winHeight * 0.815 - plat3_1.height * 2
            room = 3
        if man.y > winHeight - man.height - 10:
            room = 9
            man.y = 0
        if man.x > 1190 - man.width and man.y < 150:
            game2 = True

    elif room == 5:
        if man.x > winWidth * 0.9875 - man.width and man.y < winHeight * 0.15:
            room = 6
            man.y = winHeight * 0.7
            man.x = winWidth * 0.5   
            
    elif room == 6:
        if gudCount > 3 and room6count > 0:
            room6count -= 1
        if room6count == 0:
            krone.isKrone = True
            room = 4
            man.y = winHeight * 0.615
    
    elif room == 7:
        if man.x > 1140:
            room = 8
            man.x = 50
        if man.x < 20 and man.y < 450:
            room = 11
            man.x = 1100
    
    elif room == 8:
        if man.x < 20:
            room = 7
            man.x = 1110
        elif man.y > 735:
            room = 1
            man.y = 0
    
    elif room == 9:
        if man.x > 1180 - man.width:
            room = 10
            man.x = 50
    
    elif room == 10:
        if enemy.health3 > 0:
            if man.x < 20:
                room = 9
                man.x = 1100
    
    elif room == 11:
        if man.x > 1150:
            room = 7
            man.x = 50


def platformer():
    if room == 1:
        platform(0, winHeight * 0.865, 850, 150)
        platform(winWidth * 0.81875, winHeight * 0.865, 300, 150)
        
    if room == 2:
        platform(plat2_1.x, plat2_1.y, plat2_1.width, plat2_1.height)
        platform(0, winHeight * 0.865, winWidth, 150)
        platform(0, winHeight * 0.565, winWidth, winHeight * 0.05)
        
    if room == 3:
        platform(0, winHeight * 0.865, winWidth, 150)
        platform(plat3_1.x, plat3_1.y, plat3_1.width, plat3_1.height)
        platform(plat3_2.x, plat3_2.y, plat3_2.width, plat3_2.height)
        platform(plat3_3.x, plat3_3.y, plat3_3.width, plat3_3.height)
        platform(plat3_4.x, plat3_4.y, plat3_4.width, plat3_4.height) 
        if hindring3.health > 0:
            platform(hindring3.x, hindring3.y, hindring3.width, hindring3.height)
            
    elif room == 4:
        platform(0, winHeight * 0.665, winWidth * 0.9375, winHeight * 0.1)
        platform(0, winHeight * 0.95, winWidth * 0.3, 100)
        platform(winWidth * 0.4, winHeight * 0.95, winWidth * 0.6, 100)
        platform(1100, 150, 150, 30)
        if not(man.djevel):
            platform(1000 - 10, 300, 400, 400)
        
    elif room == 5:
        platform(0, winHeight * 0.665, winWidth, winHeight * 0.3)
        platform(plat5_1.x, plat5_1.y, plat5_1.width, plat5_1.height)
        platform(plat5_2.x, plat5_2.y, plat5_2.width, plat5_2.height)
        if koden:
           platform(plat5_3.x, plat5_3.y, plat5_3.width, plat5_3.height)
           platform(plat5_4.x, plat5_4.y, plat5_4.width, plat5_4.height)
           platform(plat5_5.x, plat5_5.y, plat5_5.width, plat5_5.height)
           platform(plat5_6.x, plat5_6.y, plat5_6.width, plat5_6.height)
           platform(plat5_7.x, plat5_7.y, plat5_7.width, plat5_7.height)
        else:
            kode()
    
    elif room == 6:
        platform(0, winHeight * 0.8, winWidth, winHeight * 0.3)
    
    elif room == 7:
        platform(plat7_1.x, plat7_1.y, plat7_1.width, plat7_1.height)
        platform(plat7_4.x, plat7_4.y, plat7_4.width, plat7_4.height)
        platform(plat7_5.x, plat7_5.y, plat7_5.width, plat7_5.height)
    
    elif room == 8:
        platform(plat7_1.x, plat7_1.y, 600, plat7_1.height)
        platform(700, plat7_1.y, 600, plat7_1.height)
        platform(plat8_2.x, plat8_2.y, plat8_2.width, plat8_2.height)
        if not(man.djevel):
            platform(500, 400, 400, 400)
    
    elif room == 9:
        platform(0, 700, 1200, 100)
        platform(0, 0, 50, 750)

    elif room == 10:
        platform(0,0, 30, 500)
        platform(1170, 0, 30, 700)
        platform(0, 700, 1200, 100)
        platform(plat10_1.x, plat10_1.y, plat10_1.width, plat10_1.height)
        platform(plat10_2.x, plat10_2.y, plat10_2.width, plat10_2.height)
        platform(plat10_3.x, plat10_3.y, plat10_3.width, plat10_3.height)
        platform(plat10_4.x, plat10_4.y, plat10_4.width, plat10_4.height)
        if enemy.health3 > 0:
            platform(enemy.x, enemy.y, enemy.width, enemy.height)
        if enemy.health1 > 0 or enemy.health2 > 0:
            if man.x + man.width > enemy.x and man.x < enemy.x + enemy.width and man.y + man.height > enemy.y - 10 and man.y < enemy.y + 50:
                man.health -= 1
                man.bounce = True
                man.bouncetime = 20
                man.hit = True
        if man.bounce:
            if man.bouncetime > 0:
                man.y -= man.bouncetime
                man.bouncetime -= 1
            elif man.bouncetime == 0:
                man.bounce = False
        else:
            if man.x + man.width > enemy.x and man.x < enemy.x + enemy.width and man.y + man.height > enemy.y - 10 and man.y < enemy.y + 50:
                enemy.health3 -= 1
                man.bounce = True
                man.bouncetime = 40
            if man.bounce:
                if man.bouncetime > 0:
                    man.y -= man.bouncetime
                    man.bouncetime -= 1
                elif man.bouncetime == 0:
                    man.bounce = False     
    
    if room == 11:
        man.y -= grav
        
# bullet hitbox funksjon
def hitbox():
    if room == 3:
        if bullet.x + bullet.width > hindring3.x and bullet.x < hindring3.x + hindring3.width and bullet.y + bullet.height > hindring3.y and bullet.y < hindring3.y + hindring3.height and hindring3.health > 0:
            hindring3.health -= 1
            bullets.pop(bullets.index(bullet)) 
            
    if room == 7:
        if bullet.x + bullet.width > plat7_2.x and bullet.x < plat7_2.x + plat7_2.width and bullet.y + bullet.height > plat7_2.y and bullet.y < plat7_2.y + plat7_2.height:
            bullet.x = winWidth * 0.98
            bullet.y = 50
        if bullet.x + bullet.width > hindring7.x and bullet.x < hindring7.x + hindring7.width and bullet.y + bullet.height > hindring7.y and bullet.y < hindring7.y + hindring7.height and hindring7.health > 0:
            hindring7.health -= 1
            bullets.pop(bullets.index(bullet))  
        if bullet.x + bullet.width > plat7_6.x and bullet.x < plat7_6.x + plat7_6.width and bullet.y + bullet.height > plat7_6.y and bullet.y < plat7_6.y + plat7_6.height:
            bullet.x = winWidth * 0.98
            bullet.y -= 100  
        if bullet.x + bullet.width > plat7_8.x and bullet.x < plat7_8.x + plat7_8.width and bullet.y + bullet.height > plat7_8.y and bullet.y < plat7_8.y + plat7_8.height:
            bullet.x = winWidth * 0.98
            bullet.y -= 100
        if bullet.x + bullet.width > plat7_10.x and bullet.x < plat7_10.x + plat7_10.width and bullet.y + bullet.height > plat7_10.y and bullet.y < plat7_10.y + plat7_10.height:
            bullets.pop(bullets.index(bullet)) 
        if bullet.x + bullet.width > hindring7_2.x and bullet.x < hindring7_2.x + hindring7_2.width and bullet.y + bullet.height > hindring7_2.y and bullet.y < hindring7_2.y + hindring7_2.height and hindring7_2.health > 0:
            hindring7_2.health -= 1
            bullets.pop(bullets.index(bullet)) 
            
    if room == 10:
        if enemy.x + 50 > bullet.x + bullet.width > enemy.x  and bullet.y + bullet.height > enemy.y:
            enemy.health1 -= 1
            bullets.pop(bullets.index(bullet))
        if enemy.x + enemy.width > bullet.x > enemy.x + 100 and bullet.y + bullet.height > enemy.y:
            enemy.health2 -= 1
            bullets.pop(bullets.index(bullet))

# Plattformfunksjon
def platform(x, y, width, height):
    if man.y + man.height > y and man.y < y + height and man.x + man.width > x and man.x + man.width < x + 2 * man.vel:
        man.x = x - man.width #Venstre
    elif man.y + man.height > y and man.y < y + height and man.x < x + width and man.x > x + width - man.vel * 2:
        man.x = x + width #Høyre
    if man.y + man.height > y and man.y + man.height < y + grav * 3 and man.x + man.width > x and man.x < x + width:
        man.y = y - man.height #Over
        man.isJump = False
        man.jumpCount = 10
    elif man.y < y + height and man.y > y + height - man.vel * 4 and man.x + man.width > x and man.x < x + width:
        man.y = y + height #Under
        man.isJump = False
        man.jumpCount = 10

#rom 5 koden
def kode():
    global kode1
    global kode2
    global kode3
    global kode4
    global kode5
    global koden
    if man.x < winWidth * 0.0125 and man.y == plat5_1.y - man.height:
        man.x = winWidth * 0.98125 - man.width
        man.y = winHeight * 0.615
        if kode1 == True and kode2 == False and kode3 == False and kode4 == False and kode5 == False:
            kode2 = True
        else:
            kode1 = False
            kode2 = False
            kode3 = False
            kode4 = False
            kode5 = False     
    elif man.x < winWidth * 0.0125 and man.y == winHeight * 0.615:
        man.x = winWidth * 0.98125 - man.width
        man.y = plat5_1.y - man.height
        if kode1 == True and kode2 == True and kode3 == False and kode4 == False and kode5 == False:
            kode3 = True
        elif kode1 == True and kode2 == True and kode3 == True and kode4 == False and kode5 == False:
            kode4 = True
        else:
            kode1 = False
            kode2 = False
            kode3 = False
            kode4 = False
            kode5 = False
    elif man.x > winWidth * 0.9875 - man.width and man.y == plat5_1.y - man.height:
        man.x = winWidth * 0.01875
        man.y = winHeight * 0.615
        if kode1 == False and kode2 == False and kode3 == False and kode4 == False and kode5 == False:
            kode1 = True
        else:
            kode1 = True
            kode2 = False
            kode3 = False
            kode4 = False
            kode5 = False
    elif man.x > winWidth * 0.9875 - man.width and man.y == winHeight * 0.615:
        man.x = winWidth * 0.01875
        man.y = plat5_1.y - man.height
        if kode1 == True and kode2 == True and kode3 == True and kode4 == True and kode5 == False:
            kode5 = True
            koden = True
        else:
            kode1 = False
            kode2 = False
            kode3 = False
            kode4 = False
            kode5 = False

def gris():
    if room == 9:
        man.health = 5
        enemy.health1 = 8
        enemy.health2 = 8
        enemy.health3 = 8
    if room == 10:
        if enemy.health1 > 0 or enemy.health2 > 0 or enemy.health3 > 0:
            if enemy.count > 0:
                enemy.count -= 1
                enemy.x += enemy.vel
            elif enemy.count > - enemy.walk:
                enemy.count -= 1
                enemy.x -= enemy.vel
            else:
                enemy.count = enemy.walk
        if enemy.health3 > 0:
            if man.hit:
                pass
            elif man.x + man.width > enemy.x - 3 and man.x < enemy.x + enemy.width + 3 and man.y + man.height > enemy.y and man.y < enemy.y + enemy.height:
                man.health -= 1
                man.hit = True
                
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 50)
def message(msg, colour, x, y, font):
    text = font.render(msg, True, colour)
    win.blit(text, [x, y])

tid = 0
runtime = 0
delay = 0
run = True
while run:
    clock.tick(60)
    if enemy.health3 > 0:
        tid += 1
        if tid % 60 == 0:
            runtime += 1
        
    if delay > 0:
        delay -= 1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if man.djevel:
        man.colour = darkRed
    else:
        man.colour = pink
    if man.hit:
        if man.damagecooldown == 0:
            man.colour = white
            man.damagecooldown = 60
        elif man.damagecooldown > 1:
            man.colour = white
            man.damagecooldown -= 1
        elif man.damagecooldown == 1:
            man.hit = False
            man.damagecooldown -= 1
    
    if man.y > 750:
        man.health -= 1
        man.y = 400
        man.hit = True
        man.damagecooldown = 60
        
    if man.health < 1:
        run = False
    elif game2:
        run = False
        
    keys = pygame.key.get_pressed()
  
    for bullet in bullets:
        
        if bullet.x < winWidth and bullet.x > 0:
            bullet.x += bullet.vel
    
        else:
            bullets.pop(bullets.index(bullet))
        hitbox()
        #Definer om bulleten treffer ting den skal treffe
        
    
    if keys[pygame.K_SPACE] and delay < 1  and krone.isKrone:
        delay = 60
        if man.left:
            facing = -1
            bullet_png = bullet_L
        elif man.right:
            facing = 1
            bullet_png = bullet_R
        bullets.append(projectile(man.x + man.width * 0.5, man.y - krone.height, 20, 16, facing))
    
    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    
    if keys[pygame.K_d] and man.x < winWidth - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        
    if not(man.isJump):
        if room == 2 and man.x > winWidth * 0.78125 and man.y < winHeight * 0.6:
            man.y -= 8
        elif man.jump:
            if keys[pygame.K_w]:
                man.isJump = True
            else:
                man.y += grav
        if not(man.jump):
            man.y += grav
        
    if man.isJump:
        if man.jumpCount >= -10:
            man.y -= man.jumpCount * abs(man.jumpCount) * 0.2 * 0.75
            man.jumpCount -= 0.5
        else:
            man.isJump = False
            man.jumpCount = 10       
    
#Inputs fra spessielle rom
    if room == 4:
        if keys[pygame.K_e] and man.x > winWidth * 0.4875 - man.width and man.x < winWidth * 0.55:
            room = 5
          
    if room == 6:
        if dialogsleep > 0:
            dialogsleep -= 1
        elif keys[pygame.K_e] and dialogsleep < 1:
            dialogsleep = 20
            gudCount += 1
            
    teleport()
    platformer()  
    gris()      
    sprites()
    
if game2:
    winHeight = 800
    winWidth = 1200
    win = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption("Lets goooo")
    class man(object):
        def __init__(self, x, y, width, height, facing, health, colour):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.facing = facing
            self.sword = False
            self.health = health
            self.damagecooldown = damagecooldown
            self.colour = colour
            
        def draw(self, win):
            pygame.draw.rect(win, man.colour, (man.x , man.y, man.width, man.height))
    
    class sword(object):
        def __init__(self, x, y, width, height, cooldown):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.isSword = False
            self.cooldown = cooldown
            self.damage = 1
    
        def draw(self, win):
            pygame.draw.rect(win, (255, 0, 0), (sword.x, sword.y, sword.width, sword.height))
            
    class opponent1(object):
        def __init__(self, x, y, width, height, health, count, vel, walk, facing):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = vel
            self.health = health
            self.count = count
            self.walk = walk
            self.facing = facing
            
        def draw(self, win):
            pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))
    
    class key4(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.key = False
        
        def draw(self, win):
            pygame.draw.rect(win, gray, (key4.x, key4.y, key4.width, key4.height))
    
    damagecooldown = 30
    x = 50
    y = 50
    white = (255, 255, 255)
    gray = (80, 80, 80)
    gul = (255, 255, 0)
    rosa = (255,0,255)
    rød = (255, 0, 0)
    
    man = man(winWidth * 0.5, winHeight * 0.5, 40, 40, 1, 5, rosa)
    sword = sword(0, 0, 10, 30, 0)
    
    opponent3_1 = opponent1(x * 11, y * 13, 30, 30, 3, 240, 2, 240, True)
    opponent3_2 = opponent1(x * 11 + 25, y * 14, 30, 30, 3, 0, 0, 0, True)
    
    key4 = key4(21 * x, 2 * y, 20, 20)
    
    opponent4_1 = opponent1(21 * x, 4 * y, 40, 40, 3, 100, 3, 100, False)
    opponent4_2 = opponent1(22 * x, 4 * y, 40, 40, 3, 100, 3, 100, False)
    opponent4_3 = opponent1(20 * x, 4 * y, 40, 40, 3, 100, 3, 100, False)
    opponent4_4 = opponent1(19 * x, 4 * y, 40, 40, 3, 100, 3, 100, False)
    
    enemies_1 = []
    
    room = 1
    
    
    
    #Sprites incoming
    def sprites():
        
        win.fill((0, 0, 0))
        vegger()
            
        if room == 2:     
            if not(man.sword):
                pygame.draw.rect(win, (255, 0, 0), (x * 12, y * 11, 10, 30))
       
        if room == 3:
            if opponent3_1.health > 0:
                opponent3_1.draw(win)
            if opponent3_2.health > 0:
                opponent3_2.draw(win)
        
        if room == 4:
            if opponent4_1.health > 0:
                opponent4_1.draw(win)
            if opponent4_2.health > 0:
                opponent4_2.draw(win)
            if opponent4_3.health > 0:
                opponent4_3.draw(win)
            if opponent4_4.health > 0:
                opponent4_4.draw(win)
    
    
     
        if sword.isSword:
            if sword.cooldown > 15:
                sword.draw(win)
                
                
        if man.health > 0:
            pygame.draw.rect(win, (255,0,0), (x + 25 , 75, 20, 20))
        if man.health > 1:
            pygame.draw.rect(win, (255,0,0), (x * 2 + 25 , 75, 20, 20))
        if man.health > 2:
            pygame.draw.rect(win, (255,0,0), (x * 3 + 25, 75, 20, 20))
        if man.health > 3:
            pygame.draw.rect(win, (255,0,0), (x * 4 + 25 , 75, 20, 20))
        if man.health > 4:
            pygame.draw.rect(win,(255, 0, 0), (x * 5 + 25, 75, 20, 20))
                
        man.draw(win)
        
    
        pygame.display.update()
    
    
    def teleportering():
        global room
        
        enemies_1len = len(enemies_1)
        
        if enemies_1len == 0:
            pass
        else:
            if x * 11 < man.x < x * 13 - man.width and man.y < 20 or x * 11 < man.x < x * 13 - man.width and man.y > winHeight - 20 - man.height or man.x > 1180 - man.width and man.y > y * 7 and man.y < y * 9 - man.height or man.x < 20 and man.y > y * 7 and man.y < y * 9 - man.height:
                del enemies_1[0:]   
        
        if room == 1:
            if x * 11 < man.x < x * 13 - man.width and man.y > winHeight - 20 - man.height:
                man.y = y * 1
                room = 2 #ned
            if man.x < 20 and man.y > y * 7 and man.y < y * 9 - man.height:       
                man.x = x * 23 - 10
                room = 3 #venstre
                enemies_1.append(opponent3_1)
                enemies_1.append(opponent3_2)
                
            elif man.x > 1180 - man.width and man.y > y * 7 and man.y < y * 9 - man.height:
                man.x = x
                room = 8 #Høyre
                
        if room == 2:
            if x * 11 < man.x < x * 13 - man.width and man.y < 20:
                man.y = winHeight - 50 - man.height
                room = 1 #opp
        
        if room == 3:
            if x * 11 < man.x < x * 13 - man.width and man.y < 20:
                man.y = winHeight - 50 - man.height
                room = 7 #opp
    
            elif x * 11 < man.x < x * 13 - man.width and man.y > winHeight - 20 - man.height:
                man.y = y * 1
                room = 4 #ned
                enemies_1.append(opponent4_1)
                enemies_1.append(opponent4_2)
                enemies_1.append(opponent4_3)
                enemies_1.append(opponent4_4)
    
            elif man.x > 1180 - man.width and man.y > y * 7 and man.y < y * 9 - man.height:
                man.x = x
                room = 1 #Høyre
    
            elif man.x < 20 and man.y > y * 7 and man.y < y * 9 - man.height:       
                man.x = x * 23 - 10
                room = 6 #venstre
            
        if room == 4:
            if man.x < 20 and man.y > y * 7 and man.y < y * 9 - man.height:       
                man.x = y * 23 - 10
                room = 5 #venstre
            if x * 11 < man.x < x * 13 - man.width and man.y < 20:
                man.y = winHeight - 50 - man.height
                room = 3 #opp
                enemies_1.append(opponent3_1)
                enemies_1.append(opponent3_2)
        
        if room == 5:
            if x * 11 < man.x < x * 13 - man.width and man.y < 20:
                man.y = winHeight - 50 - man.height
                room = 6 #opp
            elif man.x > 1180 - man.width and man.y > y * 7 and man.y < y * 9 - man.height:
                man.x = x
                room = 4 #Høyre
        
        if room == 6:
            if man.x > 1180 - man.width and man.y > y * 7 and man.y < y * 9 - man.height:
                man.x = x
                room = 3 #Høyre
            elif x * 11 < man.x < x * 13 - man.width and man.y > winHeight - 20 - man.height:
                man.y = y * 1
                room = 5 #ned
        
        if room == 7:
            if x * 11 < man.x < x * 13 - man.width and man.y > winHeight - 20 - man.height:
                man.y = y * 1
                room = 3 #ned
        if room == 8:
            if man.x < 20 and man.y > y * 7 and man.y < y * 9 - man.height:       
                man.x = y * 23 - 10
                room = 1 #venstre
            
    
    
    
    
    def opponents():
        global damagecooldown
        
        if damagecooldown > 0:
            damagecooldown -= 1
    """
        else:
            if room == 3:
                oppHitbox(opponent3_1.x, opponent3_1.y, opponent3_1.width, opponent3_1.height, opponent3_1.health)
                oppHitbox(opponent3_2.x, opponent3_2.y, opponent3_2.width, opponent3_2.height, opponent3_2.health)
         
            if room == 4:
                oppHitbox(opponent4_1.x, opponent4_1.y, opponent4_1.width, opponent4_1.height, opponent4_1.health)
                oppHitbox(opponent4_2.x, opponent4_2.y, opponent4_2.width, opponent4_2.height, opponent4_2.health)
                oppHitbox(opponent4_3.x, opponent4_3.y, opponent4_3.width, opponent4_3.height, opponent4_3.health)
                oppHitbox(opponent4_4.x, opponent4_4.y, opponent4_4.width, opponent4_4.height, opponent4_4.health)
                    
    """        
            
        
        
        
        
                
    def hitboxer():
        
        sword.x = man.x
        sword.y = man.y
        
        if sword.isSword:
            if man.facing == 1:
                    sword.x += 15
                    sword.y -= sword.height
                    sword.width = 10
                    sword.height = 30
                    
            elif man.facing == 2:
                sword.x += man.width
                sword.y += 15
                sword.width = 30
                sword.height = 10
                    
            elif man.facing == 3:
                sword.x += 15
                sword.y += man.height
                sword.width = 10
                sword.height = 30
                    
            elif man.facing == 4:
                sword.x -= 30
                sword.y += 15
                sword.width = 30
                sword.height = 10
        
        if room == 1:
            if man.x > x * 10 and man.x + man.width < x * 14:
                if man.y > y * 6 and man.y + man.height < x * 10:
                    man.health = 5
                  
        if room == 4:
            if not(key4.key):
                if man.x + man.width > key4.x and man.x < key4.x + key4.width and man.y + man.height > key4.y and man.y < key4.y + key4.height:
                    key4.key = True
                                      
        if room == 2:
            if not(man.sword):
                if x * 11 < man.x < x * 13 - man.width:
                    if man.y > y * 10 and man.y + man.height < y * 13:
                        man.sword = True
        
    
        
        
    def vegger():
        pygame.draw.rect(win, white, (0, 0, 50, 350))
        pygame.draw.rect(win, white, (0, 450, 50, 350))
        pygame.draw.rect(win, white, (0,0, 550, 50))
        pygame.draw.rect(win, white, (0, 750, 550, 50))
        pygame.draw.rect(win, white, (650, 0, 550, 50))
        pygame.draw.rect(win, white, (650, 750, 550, 50))
        pygame.draw.rect(win, white, (1150, 0, 50, 350))
        pygame.draw.rect(win, white, (1150, 450, 50, 350))
        
        
        if room == 1:
            pygame.draw.rect(win, (gray), (550, 0, 100, 50))
            pygame.draw.rect(win, gul, (x * 10, y * 6, 4 * x, 4 * y))
            
            pygame.draw.rect(win, white, (x * 9, y * 5, 50, 50))
            pygame.draw.rect(win, white, (x * 9, y * 6, 50, 50))
            pygame.draw.rect(win, white, (x * 9, y * 7, 50, 50))
            pygame.draw.rect(win, white, (x * 9, y * 8, 50, 50))
            pygame.draw.rect(win, white, (x * 9, y * 9, 50, 50))
            pygame.draw.rect(win, white, (x * 9, y * 10, 50, 50))
            
            pygame.draw.rect(win, white, (x * 10, y * 10, 50, 50))
            #pygame.draw.rect(win, white, (x * 11, y * 9, 50, 50))
            #pygame.draw.rect(win, white, (x * 12, y * 9, 50, 50))
            pygame.draw.rect(win, white, (x * 13, y * 10, 50, 50))
            
            pygame.draw.rect(win, white, (x * 10, y * 5, 50, 50))
            pygame.draw.rect(win, white, (x * 11, y * 5, 50, 50))
            pygame.draw.rect(win, white, (x * 12, y * 5, 50, 50))
            pygame.draw.rect(win, white, (x * 13, y * 5, 50, 50))
            
            pygame.draw.rect(win, white, (x * 14, y * 5, 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 6, 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 7, 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 8, 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 9, 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 10, 50, 50))
            
        if room == 2:
            pygame.draw.rect(win, white, (x * 0, y * 7, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 15, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 23, y * 7, 50, 2 * 50))
            
            pygame.draw.rect(win, white, (x * 2, y * 2, 50, 8 * 50))
            pygame.draw.rect(win, white, (x * 3, y * 4, 3 * 50, 50))
            pygame.draw.rect(win, white, (x * 3, y * 8, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 4, y * 9, 2* 50, 50))
            pygame.draw.rect(win, white, (x * 6, y * 8, 50, 4 * 50))#5
            pygame.draw.rect(win, white, (x * 3, y * 11, 4 * 50, 50))
            pygame.draw.rect(win, white, (x * 2, y * 11, 50, 3 * 50))
            pygame.draw.rect(win, white, (x * 5, y * 12, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 4, y * 13, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 6, y * 13, 3 * 50, 50))#10
            pygame.draw.rect(win, white, (x * 8, y * 11, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 9, y * 11, 50, 50))
            pygame.draw.rect(win, white, (x * 10, y * 9, 50, 5 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 9, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 13, y * 9, 50, 5 * 50))#15
            pygame.draw.rect(win, white, (x * 14, y * 11, 2 * 50, 50))
            
            pygame.draw.rect(win, white, (x * 4, y * 2, 4 * 50, 50))
            pygame.draw.rect(win, white, (x * 7, y * 3, 50, 3 * 50))
            pygame.draw.rect(win, white, (x * 4, y * 6, 5 * 50, 50))
            pygame.draw.rect(win, white, (x * 8, y * 7, 12 * 50, 50))
            pygame.draw.rect(win, white, (x * 8, y * 8, 50, 2 * 50))#5
            pygame.draw.rect(win, white, (x * 10, y * 9, 50, 5 * 50))
            pygame.draw.rect(win, white, (x * 19, y * 4, 50, 3 * 50))
            pygame.draw.rect(win, white, (x * 9, y * 2, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 10, y * 3, 50, 3 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 5, 6 * 50, 50))#10
            pygame.draw.rect(win, white, (x * 16, y * 6, 50, 50))
            pygame.draw.rect(win, white, (x * 17, y * 8, 50, 50))
            pygame.draw.rect(win, white, (x * 15, y * 9, 7 * 50, 50))
            pygame.draw.rect(win, white, (x * 21, y * 10, 50, 4 * 50))
            pygame.draw.rect(win, white, (x * 17, y * 10, 50, 4 * 50))#15
            pygame.draw.rect(win, white, (x * 15, y * 13, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 16, y * 14, 50, 50))
            
            pygame.draw.rect(win, white, (x * 19, y * 11, 50, 4 * 50))
            
            pygame.draw.rect(win, white, (x * 21, y * 2, 50, 6 * 50))
            pygame.draw.rect(win, white, (x * 22, y * 7, 50, 50))
            
            pygame.draw.rect(win, white, (x * 13, y * 3, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 14, y * 2, 5 * 50, 50))
            pygame.draw.rect(win, white, (x * 16, y * 3, 50, 50))
            
            pygame.draw.rect(win, gul, (x * 11, y * 10, 2 * 50, 2 * 50))
            
            if not(man.sword):
                pygame.draw.rect(win, (255, 0, 0), (x * 12, y * 11, 10, 30))
                
        elif room == 3:
            pygame.draw.rect(win, white, (x * 10, y * 5, 50, 10 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 5, 7 * 50, 50))
            pygame.draw.rect(win, white, (x * 17, y * 1, 50, 4 * 50))
                
        elif room == 4:
            pygame.draw.rect(win, white, (x * 23, y * 7, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 15, 2 * 50, 50))
            
            pygame.draw.rect(win, white, (x * 10, y * 1, 50, 11 * 50))
            pygame.draw.rect(win, white, (x * 10, y * 11, 9 * 50, 50))
            pygame.draw.rect(win, white, (x * 5, y * 3, 50, 12 * 50))
            pygame.draw.rect(win, white, (x * 18, y, 50, 7 * 50))
            
            if not(key4.key):
                key4.draw(win)
                pygame.draw.rect(win, gray, (x * 10, y * 12, 50, 3 * 50)) #door
            
        elif room == 5:
            pygame.draw.rect(win, white, (x * 0, y * 7, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 15, 2 * 50, 50))
    
        elif room == 6:
            pygame.draw.rect(win, white, (x * 0, y * 7, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 0, 2 * 50, 50))
        
        elif room == 7:
            pygame.draw.rect(win, white, (x * 0, y * 7, 50, 2 * 50))
            pygame.draw.rect(win, white, (x * 11, y * 0, 2 * 50, 50))
            pygame.draw.rect(win, white, (x * 23, y * 7, 50, 2 * 50))
    
        elif room == 8:
            pygame.draw.rect(win, white, (x * 1, y * 0, 23 * 50, 7 * 50))
            pygame.draw.rect(win, white, (x * 1, y * 9, 23 * 50, 7 * 50))
            
            
        platform(0, 0, 50, 350)
        platform(0, 450, 50, 350)
        platform(0,0, 550, 50)
        platform(0, 750, 550, 50)
        platform(650, 0, 550, 50)
        platform(650, 750, 550, 50)
        platform(1150, 0, 50, 350)
        platform(1150, 450, 50, 350)
        
        if room == 1:
            platform(550, 0, 100, 50)
            platform(x * 9, y * 5, 50, 50 * 6)
            platform(x * 10, y * 5, 4 * 50, 50)
            platform(x * 10, y * 10, 50, 50)
            platform(x * 13, y * 10, 50, 50)
            platform(x * 14, y * 5, 50, 6 * 50)
        elif room == 2:
            platform(x * 0, y * 7, 50, 2 * 50) #venstre
            platform(x * 11, y * 15, 2 * 50, 50) #nede
            platform(x * 23, y * 7, 50, 2 * 50) #høyre
            
            platform(x * 2, y * 2, 50, 8 * 50)
            platform(x * 3, y * 4, 3 * 50, 50)
            platform(x * 3, y * 8, 2 * 50, 50)
            platform(x * 4, y * 9, 2* 50, 50)
            platform(x * 6, y * 8, 50, 4 * 50)#5
            platform(x * 3, y * 11, 4 * 50, 50)
            platform(x * 2, y * 11, 50, 3 * 50)
            platform(x * 5, y * 12, 50, 2 * 50)
            platform(x * 4, y * 13, 50, 2 * 50)
            platform(x * 6, y * 13, 3 * 50, 50)#10
            platform(x * 8, y * 11, 50, 2 * 50)
            platform(x * 9, y * 11, 50, 50)
            platform(x * 10, y * 9, 50, 5 * 50)
            platform(x * 11, y * 9, 2 * 50, 50)
            platform(x * 13, y * 9, 50, 5 * 50)#15
            platform(x * 14, y * 11, 2 * 50, 50)
            
            platform(x * 4, y * 2, 4 * 50, 50)
            platform(x * 7, y * 3, 50, 3 * 50)
            platform(x * 4, y * 6, 5 * 50, 50)
            platform(x * 8, y * 7, 12 * 50, 50)
            platform(x * 8, y * 8, 50, 2 * 50)#5
            platform(x * 10, y * 9, 50, 5 * 50)
            platform(x * 19, y * 4, 50, 3 * 50)
            platform(x * 9, y * 2, 50, 2 * 50)
            platform(x * 10, y * 3, 50, 3 * 50)
            platform(x * 11, y * 5, 6 * 50, 50)#10
            platform(x * 16, y * 6, 50, 50)
            platform(x * 17, y * 8, 50, 50)
            platform(x * 15, y * 9, 7 * 50, 50)
            platform(x * 21, y * 10, 50, 4 * 50)
            platform(x * 17, y * 10, 50, 4 * 50)#15
            platform(x * 15, y * 13, 2 * 50, 50)
            platform(x * 16, y * 14, 50, 50)
            
            platform(x * 19, y * 11, 50, 4 * 50)
            
            platform(x * 21, y * 2, 50, 6 * 50)
            platform(x * 22, y * 7, 50, 50)
            
            platform(x * 13, y * 3, 2 * 50, 50)
            platform(x * 14, y * 2, 5 * 50, 50)
            platform(x * 16, y * 3, 50, 50)
        
        elif room == 3:
            platform(x * 10, y * 5, 50, 10 * 50)
            platform(x * 11, y * 5, 7 * 50, 50)
            platform(x * 17, y * 1, 50, 4 * 50)
    
        elif room == 4:
            platform(x * 23, y * 7, 50, 2 * 50)
            platform(x * 11, y * 15, 2 * 50, 50)
            
            platform(x * 10, y * 1, 50, 11 * 50)
            platform(x * 10, y * 11, 9 * 50, 50)
            platform(x * 5, y * 3, 50, 12 * 50)
            platform(x * 18, y, 50, 7 * 50)
            
            if not(key4.key):
                platform(x * 10, y * 12, 50, 4 * 50)
            
    
        elif room == 5:
            platform(x * 0, y * 7, 50, 2 * 50)
            platform(x * 11, y * 15, 2 * 50, 50)
        
        elif room == 6:
            platform(x * 0, y * 7, 50, 2 * 50)
            platform(x * 11, y * 0, 2 * 50, 50)
        
        elif room == 7:
            platform(x * 0, y * 7, 50, 2 * 50)
            platform(x * 11, y * 0, 2 * 50, 50)
            platform(x * 23, y * 7, 50, 2 * 50)
        
        elif room == 8:
            platform(x * 1, y * 0, 23 * 50, 7 * 50)
            platform(x * 1, y * 9, 23 * 50, 7 * 50)
    
             
            
        
    def platform(x, y, width, height):
        if man.y + man.height > y and man.y < y + height and man.x + man.width > x and man.x + man.width < x + 2 * man.vel:
            man.x = x - man.width #Venstre
        elif man.y + man.height > y and man.y < y + height and man.x < x + width and man.x > x + width - man.vel * 2:
            man.x = x + width #Høyre
        if man.y + man.height > y and man.y + man.height < y + 2 * man.vel and man.x + man.width > x and man.x < x + width:
            man.y = y - man.height #Over
        elif man.y < y + height and man.y > y + height - man.vel * 2 and man.x + man.width > x and man.x < x + width:
            man.y = y + height #Under
        
        for enemy in enemies_1:
            if enemy.y + enemy.height > y and enemy.y < y + height and enemy.x + enemy.width > x and enemy.x + enemy.width < x + 2 * man.vel:
                enemy.x = x - enemy.width #Venstre
            elif enemy.y + enemy.height > y and enemy.y < y + height and enemy.x < x + width and enemy.x > x + width - man.vel * 2:
                enemy.x = x + width #Høyre
            if enemy.y + enemy.height > y and enemy.y + enemy.height < y + 2 * man.vel and enemy.x + man.width > x and enemy.x < x + width:
                enemy.y = y - enemy.height #Over
            elif enemy.y < y + height and enemy.y > y + height - man.vel * 2 and enemy.x + enemy.width > x and enemy.x < x + width:
                enemy.y = y + height #Under
            
    
    def opp1():
        global damagecooldown
    
        for enemy in enemies_1:
            if enemy.health > 0:
                if enemy.facing:
                    if enemy.count > 0:
                        enemy.count -= 1
                        enemy.x += enemy.vel
                    elif enemy.count > - enemy.walk:
                        enemy.count -= 1
                        enemy.x -= enemy.vel
                    else:
                        enemy.count = enemy.walk
                else:
                    if enemy.count > 0:
                        enemy.count -= 1
                        enemy.y += enemy.vel
                    elif enemy.count > - enemy.walk:
                        enemy.count -= 1
                        enemy.y -= enemy.vel
                    else:
                        enemy.count = enemy.walk
                
                if damagecooldown > 0:
                    damagecooldown -= 1
                    man.colour = rød
                else:
                    if man.colour == rød:
                        man.colour = rosa
                    if man.x + man.width > enemy.x and man.x < enemy.x + enemy.width and man.y + man.height > enemy.y and man.y < enemy.y + enemy.height:
                        man.health -= 1
                        damagecooldown = 60
                        platform(enemy.x, enemy.y, enemy.width, enemy.height)
                    elif sword.isSword:
                        if sword.x + sword.width > enemy.x and sword.x < enemy.x + enemy.width and sword.y + sword.height > enemy.y and sword.y < enemy.y + enemy.height:
                            print(enemy.health)
                            enemy.health -= 1
                            print(enemy.health)
                            damagecooldown = 15
                            if man.facing == 1:
                                man.y += 15
                                enemy.y -= 15
                            elif man.facing == 2:
                                man.x -= 15
                                enemy.x += 15
                            elif man.facing == 3:
                                man.y -= 15
                                enemy.y += 15
                            elif man.facing == 4:
                                man.x += 15
                                enemy.x -= 15
    
    run = True
    while run and man.health > 0:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
            
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.facing = 4
        
        if keys[pygame.K_RIGHT] and man.x < winWidth - man.width - man.vel:
            man.x += man.vel
            man.facing = 2
            
        if keys[pygame.K_UP] and man.y > man.vel:
            man.y -= man.vel
            man.facing = 1
            
        if keys[pygame.K_DOWN] and man.y < winHeight - man.height - man.vel:
            man.y += man.vel
            man.facing = 3
        
        if not(sword.isSword):
            if man.sword:
                if keys[pygame.K_x]:
                    sword.isSword = True
                    sword.cooldown = 30
        
        if sword.isSword:     
            if sword.cooldown > 0:
                sword.cooldown -= 1
                
            else:
                sword.isSword = False
                
                    
        teleportering()
        vegger()
        opponents()  
        opp1()
        hitboxer()
        sprites()
        #if keys[pygame.K_a] and man.x > man.vel:

pygame.quit()
