"""
Game 2: Action RPG
Entity definitions for the action RPG game.
"""
import pygame
from utils.entities import Entity


class ManGame2(Entity):
    """Player character for Game 2 - 4-directional movement."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.vel = 5
        self.facing = 1  # 1=up, 2=right, 3=down, 4=left
        self.sword = False
        self.health = 5
        self.damagecooldown = 0
        self.colour = (255, 0, 255)
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))


class Sword(Entity):
    """Melee weapon for Game 2."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.is_sword = False
        self.cooldown = 0
        self.damage = 1
    
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))


class Opponent1(Entity):
    """Enemy NPC for Game 2 rooms."""
    
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.vel = 2
        self.health = health
        self.count = 0
        self.walk = 240
        self.facing = True
    
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))


class Key4(Entity):
    """Key collectible for Game 2."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.key = False
    
    def draw(self, win):
        pygame.draw.rect(win, (80, 80, 80), (self.x, self.y, self.width, self.height))
