# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:31:06 2022

@author: linde
"""

import pygame
pygame.init()

winHeight = int(750 * 1)
winWidth = int(winHeight * 1.6)

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Sug meg")

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
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.isJump = False
        self.jump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        
    def draw(self, win):
        pygame.draw.rect(win, (255,0,255), (man.x , man.y, man.width, man.height))
        
class krone(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isKrone = False
        
    def draw(self, win):
        win.blit(krone_png, (krone.x, krone.y, krone.width, krone.height))
    
class jumpAb(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,200,200), (jumpAb.x, jumpAb.y, jumpAb.width, jumpAb.height))

class plat1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        win.blit(room3_1, (self.x, self.y))

class plat2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        win.blit(room3_1, (self.x, self.y))
        
class plat3(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        win.blit(room3_1, (self.x, self.y))

class plat4(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        win.blit(room3_1, (self.x, self.y))

class portal1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        win.blit(portal, (self.x, self.y))

class etgRoom2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        win.blit(floorRoom2, (self.x, self.y))

class plat5_1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_1.x, plat5_1.y, plat5_1.width, plat5_1.height))

class plat5_2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_2.x, plat5_2.y, plat5_2.width, plat5_2.height))

class plat5_3(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_3.x, plat5_3.y, plat5_3.width, plat5_3.height))

class plat5_4(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_4.x, plat5_4.y, plat5_4.width, plat5_4.height))

class plat5_5(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_5.x, plat5_5.y, plat5_5.width, plat5_5.height))

class plat5_6(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_6.x, plat5_6.y, plat5_6.width, plat5_6.height))

class plat5_7(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
    def draw(self, win):
        pygame.draw.rect(win, (0,0,0), (plat5_7.x, plat5_7.y, plat5_7.width, plat5_7.height))
        
class projectile(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 10 * facing
    
    def draw(self, win):
        win.blit(bullet_png, (self.x, self.y))
    
class hindring3(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health 
        
    def draw(self, win):
        win.blit(hindring3_1, (self.x, self.y))



kode1 = False
kode2 = False
kode3 = False
kode4 = False
kode5 = False
koden = False

bullets = []

grav = 10  
room = 1
gudCount = 1
dialogsleep = 0
room6count = 100

man = man(winWidth * 0.375, winHeight * 0.815, winWidth * 0.05 / 1.6, winHeight * 0.05)
krone = krone(man.x, man.y - winHeight * 0.05, winWidth * 0.05 / 1.6, winHeight * 0.05)

jumpAb = jumpAb(winWidth * 0.07625, winHeight * 0.790, winWidth * 0.02 / 1.6, winHeight * 0.02)

plat1 = plat1(winWidth * 0.625, winHeight * 0.765, winWidth * 0.4375, winHeight * 0.1)
plat2 = plat2(winWidth * 0.84375, winHeight * 0.765 - plat1.height, winWidth * 0.4375, winHeight * 0.104)
plat3 = plat3(winWidth * 0.3125, winHeight * 0.765 - plat1.height * 2, winWidth * 0.4375, winHeight * 0.104)
plat4 = plat4(winWidth * -0.125, winHeight * 0.765 - plat1.height * 2, winWidth * 0.4375, winHeight * 0.104)
portal1 = portal1(0, winHeight * 0.165, winWidth * 0.125, winHeight * 0.4)
etg2Room2 = etgRoom2(0, winHeight * 0.565, winWidth, winHeight * 0.05)
plat5_1 = plat5_1(0, winHeight * 0.550, winWidth * 0.1875, winHeight * 0.02)
plat5_2 = plat5_2(winWidth * 0.8125, winHeight * 0.55, winWidth * 0.187500, winHeight * 0.02)
plat5_3 = plat5_3(winWidth * 0.1875, winHeight * 0.425, winWidth * 0.09375, winHeight * 0.04)
plat5_4 = plat5_4(winWidth * 0.3125, winHeight * 0.3, winWidth * 0.09375, winHeight * 0.04)
plat5_5 = plat5_5(winWidth * 0.5, winHeight * 0.175, winWidth * 0.09375, winHeight * 0.04)
plat5_6 = plat5_6(winWidth * 0.78125, winHeight * 0.3, winWidth * 0.125, winHeight * 0.04)
plat5_7 = plat5_7(winWidth * 0.90625, winHeight * 0.175, winWidth * 0.125, winHeight * 0.04)

hindring3 = hindring3(winWidth * 0.25, winHeight * 0.165, winWidth * 0.046875, winHeight * 0.4, 5)


# Alt av sprites kommer her
def redrawGameWindow():
    global room    
    global hindring3_1
    global hindring1_png
    global hindring2_png
    global hindring3_png
    global room6count
    
    if room == 1:
        win.blit(bg, (0,0))
        win.blit(gulv1, (0, 815+ man.height))
        pygame.draw.rect(win, (5,5,0), (winWidth * 0.70625 , winHeight * 0.865, winWidth * 0.18125, winHeight * 0.2))
        win.blit(bro, (winWidth * 0.81875, winHeight * 0.865))
        win.blit(darkRoomEnt, (0, winHeight * 0.22))
            
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
        portal1.draw(win)
        etg2Room2.draw(win)
        win.blit(levitasjon, (winWidth * 0.71875, winHeight * 0.08))
        if not(man.jump):
            jumpAb.draw(win)
    
    elif room == 3:
        win.blit(bg3, (0, 0))
        plat1.draw(win)
        plat2.draw(win)
        plat3.draw(win)
        plat4.draw(win)
        portal1.draw(win)
        
        if hindring3.health > 0:
            if hindring3.health == 5:
                hindring3_1 = hindring1_png
            elif 2 < hindring3.health < 5:
                hindring3_1 = hindring2_png
            else:
                hindring3_1 = hindring3_png
            hindring3.draw(win)
            
        
    elif room == 4:
       win.blit(bg4, (0,0))
       win.blit(floor4, (0, winHeight * 0.665))
       if man.y == winHeight * 0.615:
           if winWidth * 0.4875 - man.width < man.x < winWidth * 0.55:
               win.blit(w, (winWidth * 0.4875, winHeight * 0.22))
            
            
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
        
    krone.x = man.x - winWidth * 0.00625
    krone.y = man.y - winHeight * 0.05
        
 
    if krone.isKrone:
        krone.draw(win)
        
    for bullet in bullets:
        bullet.draw(win)
    
    
    man.draw(win)
    pygame.display.update()

#Teleporterefunksjon + annet
def teleport():
    global room
    global room6count
    
    if room == 1:
        if man.x < winWidth * 0.00625 and man.y == winHeight * 0.815:
            room = 2
            man.x = winWidth - man.width - winWidth * 0.03125
        elif man.x > winWidth - man.width - 10 and man.y == winHeight * 0.815:
            room = 3
            man.x = winWidth * 0.031250
            man.y = winHeight * 0.815
            
    elif room == 2:
        if man.x < winWidth * 0.075:
            man.jump = True
                
        if man.x > winWidth - man.width - winWidth * 0.006250 and man.y == winHeight * 0.815:
            room = 1
            man.x = winWidth * 0.03125
        elif man.x < winWidth * 0.05 and man.y < winHeight * 0.6:
            room = 3
            man.x += winWidth * 0.09375
        elif man.y < 0:
            room = 7
            man.y = winHeight * 0.9
    
    elif room == 3:
        if man.x < winWidth * 0.00625 and man.y == winHeight * 0.815:
            room = 1
            man.x = winWidth - man.width - winWidth * 0.03125
            man.y = winHeight * 0.815
        elif man.x > winWidth - man.width - winWidth * 0.00625:
            man.x = winWidth * 0.0625
            man.y = winHeight * 0.815 - plat1.height * 2
            room = 4
        elif man.x < winWidth * 0.05 and man.y < winHeight * 0.6:
            room = 2
            man.x += winWidth * 0.09375
    
    elif room == 4:
        if man.x < 20 and man.y < 800:
            man.x = winWidth * 0.9375
            man.y = winHeight * 0.815 - plat1.height * 2
            room = 3

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
        pass


def platformer():
    if room == 3:
        platform(plat1.x, plat1.y, plat1.width, plat1.height)
        platform(plat2.x, plat2.y, plat2.width, plat2.height)
        platform(plat3.x, plat3.y, plat3.width, plat3.height)
        platform(plat4.x, plat4.y, plat4.width, plat4.height) 
        if hindring3.health > 0:
            platform(hindring3.x, hindring3.y, hindring3.width, hindring3.height)
            
    elif room == 4:
        platform(0, winHeight * 0.665, winWidth * 0.9375, winHeight * 0.1)
        
    elif room == 5:
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
    
#Gravitasjon
def gravity():
    if room == 1:
        if not(man.isJump):
            man.y += grav
            if man.x > 0 and man.x < winWidth * 0.70625:
                man.y -= grav
            elif man.x > winWidth * 0.78125:
                man.y -= grav
    
    if room == 2:
        if man.y < winHeight * 0.35:
            man.y -= 8
        elif man.x > winWidth * 0.78125 and man.y < winHeight * 0.6:
            man.y -= 8
    
    elif room == 3:
        if not(man.isJump):
            man.y += grav
            if man.y == winHeight * 0.815:
                man.y -= grav
            elif man.y > winHeight * 0.815 - man.height:
                 man.y = winHeight * 0.815
    
    elif room == 4:        
        if not(man.isJump):
                man.y += grav
                if man.y == winHeight * 0.815:
                    man.y -= grav
                elif man.y > winHeight * 0.815 - man.height:
                     man.y = winHeight * 0.815
        
    elif room == 5:
        if not(man.isJump):
            man.y += grav
            if man.y == winHeight * 0.815:
                man.y -= grav
            elif man.y > winHeight * 0.615 - man.height:
                 man.y = winHeight * 0.615



# bullet hitbox funksjon
def hitbox():
      if room == 3:
            if bullet.x + bullet.width > hindring3.x and bullet.x < hindring3.x + hindring3.width and bullet.y + bullet.height > hindring3.y and bullet.y < hindring3.y + hindring3.height and hindring3.health > 0:
                hindring3.health -= 1
                print("hit")
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
            
            

delay = 0
run = True
while run:
    clock.tick(60)
    
    if delay > 0:
        delay -= 1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if man.y > winHeight:
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
        if man.jump:
            if keys[pygame.K_w]:
                man.isJump = True
        
    if man.isJump:
        if man.jumpCount >= -10:
            man.y -= man.jumpCount * abs(man.jumpCount) * 0.2
            man.jumpCount -= 0.5
        else:
            man.isJump = False
            man.jumpCount = 10       
    

#Inputs fra spessielle rom
    if room == 4:
        if keys[pygame.K_w] and man.x > winWidth * 0.4875 - man.width and man.x < winWidth * 0.55:
            room = 5
          
    if room == 6:
        if dialogsleep > 0:
            dialogsleep -= 1
        elif keys[pygame.K_e] and dialogsleep < 1:
            dialogsleep = 20
            gudCount += 1

    gravity()            
    teleport()
    platformer()        
    redrawGameWindow()
    
    
pygame.quit()