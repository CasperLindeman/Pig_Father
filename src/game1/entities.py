"""
Game 1: Platformer
Entity definitions for the platformer game.
"""
import pygame
from utils.entities import Entity, Platform, Obstacle, Collectible
from utils.constants import BLACK, PINK, DARK_RED


class Man(Entity):
    """Player character for Game 1."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.vel = 6 * 0.75
        self.is_jump = False
        self.jump = False
        self.jump_count = 10
        self.right = False
        self.left = False
        self.colour = PINK
        self.djevel = False
        self.health = 5
        self.damagecooldown = 0
        self.hit = False
        self.bounce = False
        self.bouncetime = 0
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))


class Enemy(Entity):
    """Final boss enemy (Satan) for Game 1."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.walk = 450
        self.count = 300
        self.vel = 2
        self.feet = 0
        self.health1 = 8
        self.health2 = 8
        self.health3 = 8
    
    def draw(self, win):
        """Draw the multi-part boss enemy."""
        if self.health3 > 0:
            # Body
            pygame.draw.rect(win, (225, 0, 225), (self.x, self.y, 200, 200))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 50, self.y + 50, 100, 100))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 30, self.y + 60, 20, 20))
            pygame.draw.rect(win, (255, 0, 255), (self.x + 150, self.y + 60, 20, 20))
            pygame.draw.rect(win, (255, 255, 255), (self.x + 65, self.y + 65, 20, 30))
            pygame.draw.rect(win, (255, 255, 255), (self.x + 115, self.y + 65, 20, 30))
            pygame.draw.rect(win, BLACK, (self.x + 70, self.y + 75, 10, 10))
            pygame.draw.rect(win, BLACK, (self.x + 120, self.y + 75, 10, 10))
            pygame.draw.rect(win, BLACK, (self.x + 48, self.y + 48, 104, 104), 2)
            pygame.draw.rect(win, BLACK, (self.x + 29, self.y + 60, 20, 20), 2)
            pygame.draw.rect(win, BLACK, (self.x + 151, self.y + 60, 20, 20), 2)
            pygame.draw.rect(win, BLACK, (self.x + 65, self.y + 65, 20, 30), 2)
            pygame.draw.rect(win, BLACK, (self.x + 115, self.y + 65, 20, 30), 2)
            pygame.draw.rect(win, BLACK, (self.x + 84, self.y + 100, 32, 32), 2)
            pygame.draw.rect(win, BLACK, (self.x + 90, self.y + 109, 7, 15))
            pygame.draw.rect(win, BLACK, (self.x + 103, self.y + 109, 7, 15))
            pygame.draw.rect(win, BLACK, (self.x + 83, self.y + 137, 36, 5))
            
            # Animation
            if self.walk % 2 == 0:
                if self.feet != 20:
                    self.feet += 1
                elif self.feet == 20:
                    self.feet = 0
            
            # Legs
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
            
            # Health indicators and damage
            self._draw_health_left(win)
            self._draw_health_right(win)
            self._draw_head(win)
        else:
            # Dead state - draw corpse
            if hasattr(self, '_grisdead_image'):
                win.blit(self._grisdead_image, (self.x, self.y + 35))
    
    def _draw_health_left(self, win):
        """Draw left side health/damage."""
        if self.health1 < 8:
            if self.health1 < 1:
                pygame.draw.rect(win, (100, 0, 0), (self.x + 20, self.y + 160, 80, 37))
                pygame.draw.rect(win, BLACK, (self.x + 114, self.y + 137, 5, 12))
                pygame.draw.rect(win, BLACK, (self.x + 111, self.y + 137, 8, 8))
                pygame.draw.rect(win, BLACK, (self.x + 83, self.y + 137, 5, 12))
                pygame.draw.rect(win, BLACK, (self.x + 83, self.y + 137, 8, 8))
                pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 100, 5, 10))
                pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 115, 5, 10))
                pygame.draw.rect(win, (0, 0, 200), (self.x + 75, self.y + 130, 5, 10))
            pygame.draw.rect(win, (100, 0, 0), (self.x, self.y + 100, 10, 10))
            if self.health1 < 7:
                pygame.draw.rect(win, (255, 0, 0), (self.x + 3, self.y + 20, 5, 15))
                if self.health1 < 6:
                    pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y + 60, 10, 30))
                    if self.health1 < 5:
                        pygame.draw.rect(win, (220, 0, 0), (self.x + 5, self.y + 115, 40, 50))
                        if self.health1 < 4:
                            pygame.draw.rect(win, (170, 0, 0), (self.x, self.y + 175, 70, 20))
                            if self.health1 < 3:
                                pygame.draw.rect(win, (70, 0, 0), (self.x + 40, self.y + 80, 5, 30))
                                if self.health1 < 2:
                                    pygame.draw.rect(win, (100, 0, 0), (self.x + 10, self.y + 120, 30, 40))
    
    def _draw_health_right(self, win):
        """Draw right side health/damage."""
        if self.health2 < 8:
            pygame.draw.rect(win, (100, 0, 0), (self.x + self.width - 20, self.y + 120, 20, 10))
            if self.health2 < 7:
                pygame.draw.rect(win, (240, 0, 0), (self.x + self.width - 45, self.y + 100, 10, 10))
                if self.health2 < 6:
                    pygame.draw.rect(win, (70, 0, 0), (self.x + self.width - 30, self.y + 60, 30, 18))
                    if self.health2 < 5:
                        pygame.draw.rect(win, (250, 0, 0), (self.x + self.width - 100, self.y + 155, 95, 40))
                        if self.health2 < 4:
                            pygame.draw.rect(win, (167, 0, 0), (self.x + self.width - 20, self.y + 137, 15, 17))
                            if self.health2 < 3:
                                pygame.draw.rect(win, (200, 0, 0), (self.x + self.width - 35, self.y + 115, 10, 5))
                                if self.health2 < 2:
                                    pygame.draw.rect(win, (100, 0, 0), (self.x + self.width - 90, self.y + 160, 65, 30))
                                    if self.health2 < 1:
                                        pygame.draw.rect(win, (40, 0, 0), (self.x + self.width - 80, self.y + 165, 45, 20))
                                        pygame.draw.rect(win, (0, 0, 200), (self.x + 120, self.y + 100, 5, 10))
                                        pygame.draw.rect(win, (0, 0, 200), (self.x + 120, self.y + 115, 5, 10))
                                        pygame.draw.rect(win, (0, 0, 200), (self.x + 120, self.y + 130, 5, 10))
    
    def _draw_head(self, win):
        """Draw head with health indicators."""
        if self.health1 > 0 or self.health2 > 0:
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
            if self.health1 > 0 and self.health2 > 0:
                pygame.draw.rect(win, (85, 85, 85), (self.x + 15, self.y - 10, 5, 10))
                pygame.draw.rect(win, (85, 85, 85), (self.x + 45, self.y - 10, 5, 10))
                pygame.draw.rect(win, (85, 85, 85), (self.x + 75, self.y - 10, 5, 10))
                pygame.draw.rect(win, (85, 85, 85), (self.x + 180, self.y - 10, 5, 10))
                pygame.draw.rect(win, (85, 85, 85), (self.x + 150, self.y - 10, 5, 10))
                pygame.draw.rect(win, (85, 85, 85), (self.x + 120, self.y - 10, 5, 10))
                pygame.draw.rect(win, (140, 140, 140), (self.x + 97, self.y - 20, 8, 10))
                pygame.draw.rect(win, (140, 140, 140), (self.x + 100, self.y - 30, 2, 10))
        
        if self.health3 < 8:
            pygame.draw.rect(win, (240, 0, 0), (self.x + 80, self.y, 20, 30))
            if self.health3 < 7:
                pygame.draw.rect(win, (140, 0, 0), (self.x + 83, self.y + 3, 14, 24))
                if self.health3 < 6:
                    pygame.draw.rect(win, (200, 0, 0), (self.x, self.y, 40, 50))
                    if self.health3 < 5:
                        pygame.draw.rect(win, (120, 0, 0), (self.x + 150, self.y + 20, 15, 10))
                        if self.health3 < 4:
                            pygame.draw.rect(win, (180, 0, 0), (self.x + 60, self.y + 35, 30, 10))
                            if self.health3 < 3:
                                pygame.draw.rect(win, (150, 0, 0), (self.x + 85, self.y + 55, 6, 10))
                                pygame.draw.rect(win, (150, 0, 0), (self.x + 100, self.y, 80, 40))
                                if self.health3 < 2:
                                    pygame.draw.rect(win, (200, 0, 0), (self.x + 55, self.y + 100, 20, 40))


class Krone(Collectible):
    """Crown collectible that grants shooting ability."""
    
    def __init__(self, x, y, width, height, image=None):
        super().__init__(x, y, width, height)
        self.is_krone = False
        self.image = image
    
    def draw(self, win):
        if self.image:
            win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 215, 0), (self.x, self.y, self.width, self.height))


class JumpAb(Entity):
    """Jump ability tutorial indicator."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
    
    def draw(self, win):
        pygame.draw.rect(win, (0, 200, 200), (self.x, self.y, self.width, self.height))


class Platform1(Entity):
    """Sprite-based platform."""
    
    def __init__(self, x, y, width, height, sprite):
        super().__init__(x, y, width, height)
        self.sprite = sprite
    
    def draw(self, win):
        if self.sprite:
            win.blit(self.sprite, (self.x, self.y))


class Platform2(Entity):
    """Colored rectangle platform."""
    
    def __init__(self, x, y, width, height, colour):
        super().__init__(x, y, width, height)
        self.colour = colour
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))


class Platform3(Entity):
    """Moving/oscillating platform."""
    
    def __init__(self, x, y, width, height, vel, facing, walk, count):
        super().__init__(x, y, width, height)
        self.vel = vel
        self.facing = facing
        self.count = count
        self.walk = walk
    
    def draw(self, win):
        if not self.facing:
            if self.walk > 0:
                self.y += self.vel
                self.walk -= 1
            elif self.walk > -self.count:
                self.y -= self.vel
                self.walk -= 1
            else:
                self.walk = self.count
        elif self.facing:
            if self.walk > 0:
                self.x += self.vel
                self.walk -= 1
            elif self.walk > -self.count:
                self.x -= self.vel
                self.walk -= 1
            else:
                self.walk = self.count
        pygame.draw.rect(win, (150, 0, 150), (self.x, self.y, self.width, self.height))


class Projectile(Entity):
    """Bullet projectile."""
    
    def __init__(self, x, y, width, height, facing, image=None):
        super().__init__(x, y, width, height)
        self.facing = facing
        self.vel = 10 * 0.75 * facing
        self.image = image
    
    def draw(self, win):
        if self.image:
            win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, self.width, self.height))


class Hindring(Obstacle):
    """Sprite-based destructible obstacle."""
    
    def __init__(self, x, y, width, height, health, image=None):
        super().__init__(x, y, width, height, health)
        self.image = image
    
    def draw(self, win):
        if self.image:
            win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(win, (100, 100, 100), (self.x, self.y, self.width, self.height))


class Hindring2(Obstacle):
    """Colored destructible obstacle."""
    
    def __init__(self, x, y, width, height, health, colour):
        super().__init__(x, y, width, height, health)
        self.colour = colour
    
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
