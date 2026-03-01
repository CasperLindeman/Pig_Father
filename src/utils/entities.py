"""
Base entity classes for both games.
"""
import pygame


class Entity:
    """Base class for all drawable game entities."""
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        """Draw the entity. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement draw()")


class Platform(Entity):
    """Base platform class."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


class Obstacle(Entity):
    """Base obstacle class with health."""
    
    def __init__(self, x, y, width, height, health):
        super().__init__(x, y, width, height)
        self.health = health


class Collectible(Entity):
    """Base collectible class."""
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.collected = False
