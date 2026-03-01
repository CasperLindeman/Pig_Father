"""
Game 2: Game state management for action RPG.
"""


class Game2State:
    """Manages the state for Game 2 (action RPG)."""
    
    def __init__(self):
        self.room = 1
        self.enemies = []
        self.damagecooldown = 30
    
    def add_enemy(self, enemy):
        """Add enemy to the active enemies list."""
        self.enemies.append(enemy)
    
    def remove_enemy(self, enemy):
        """Remove enemy from the active enemies list."""
        if enemy in self.enemies:
            self.enemies.remove(enemy)
    
    def clear_enemies(self):
        """Clear all enemies."""
        self.enemies.clear()
