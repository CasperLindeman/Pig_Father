"""
Game 1: Game state management.
"""


class Game1State:
    """Manages the state for Game 1 (platformer)."""
    
    def __init__(self):
        # Room management
        self.room = 1
        self.bullets = []
        
        # Room 5 code puzzle state
        self.kode1 = False
        self.kode2 = False
        self.kode3 = False
        self.kode4 = False
        self.kode5 = False
        self.koden = False  # Master flag
        
        # Room 6 dialog state
        self.gud_count = 1
        self.room6_count = 100
        self.dialog_sleep = 0
        
        # Special states
        self.secret = False
        self.game2_triggered = False
        
        # Timing
        self.runtime = 0
        self.tid = 0
        self.delay = 0
    
    def reset_room(self, room_num):
        """Reset state for a specific room."""
        self.room = room_num
        if room_num != 5:
            # Reset code puzzle if leaving room 5
            pass
    
    def reset_code_puzzle(self):
        """Reset code puzzle flags."""
        self.kode1 = False
        self.kode2 = False
        self.kode3 = False
        self.kode4 = False
        self.kode5 = False
        self.koden = False
    
    def add_bullet(self, bullet):
        """Add a bullet to the active bullets list."""
        self.bullets.append(bullet)
    
    def remove_bullet(self, bullet):
        """Remove a bullet from the active bullets list."""
        if bullet in self.bullets:
            self.bullets.remove(bullet)
    
    def update_runtime(self):
        """Update runtime counter."""
        self.tid += 1
        if self.tid % 60 == 0:
            self.runtime += 1
