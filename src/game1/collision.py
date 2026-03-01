"""
Game 1: Collision detection and physics.
"""


def platform(man, x, y, width, height, grav):
    """Detect and resolve platform collisions."""
    # Left collision
    if (man.y + man.height > y and man.y < y + height and
        man.x + man.width > x and man.x + man.width < x + 2 * man.vel):
        man.x = x - man.width
    # Right collision
    elif (man.y + man.height > y and man.y < y + height and
          man.x < x + width and man.x > x + width - man.vel * 2):
        man.x = x + width
    # Top collision (landing on platform)
    if (man.y + man.height > y and man.y + man.height < y + grav * 3 and
        man.x + man.width > x and man.x < x + width):
        man.y = y - man.height
        man.is_jump = False
        man.jump_count = 10
    # Bottom collision
    elif (man.y < y + height and man.y > y + height - man.vel * 4 and
          man.x + man.width > x and man.x < x + width):
        man.y = y + height
        man.is_jump = False
        man.jump_count = 10


def check_hitbox(bullet, room, obstacles, hindring3, hindring7, hindring7_2, plat7_flags):
    """Check bullet collisions with obstacles.
    
    Returns: True if bullet should be removed
    """
    if room == 3:
        if (bullet.x + bullet.width > hindring3.x and
            bullet.x < hindring3.x + hindring3.width and
            bullet.y + bullet.height > hindring3.y and
            bullet.y < hindring3.y + hindring3.height and
            hindring3.health > 0):
            hindring3.health -= 1
            return True
    
    elif room == 7:
        # Bouncing platforms
        if bullet.x + bullet.width > 0 and bullet.x < 70:  # plat7_2
            bullet.x = 1200 * 0.98
            bullet.y = 50
            return False
        
        # Destructible hindring7
        if (bullet.x + bullet.width > hindring7.x and
            bullet.x < hindring7.x + hindring7.width and
            bullet.y + bullet.height > hindring7.y and
            bullet.y < hindring7.y + hindring7.height and
            hindring7.health > 0):
            hindring7.health -= 1
            return True
        
        # More bouncing platforms
        if bullet.x + bullet.width > 0 and bullet.x < 20:
            bullet.x = 1200 * 0.98
            bullet.y -= 100
            return False
        
        if bullet.x + bullet.width > 1180 and bullet.x > 1160:
            bullet.x = 1200 * 0.98
            bullet.y -= 100
            return False
        
        # Destructible plat7_10
        if bullet.x + bullet.width > 570 and bullet.x < 600:
            return True
        
        # Destructible hindring7_2
        if (bullet.x + bullet.width > hindring7_2.x and
            bullet.x < hindring7_2.x + hindring7_2.width and
            bullet.y + bullet.height > hindring7_2.y and
            bullet.y < hindring7_2.y + hindring7_2.height and
            hindring7_2.health > 0):
            hindring7_2.health -= 1
            return True
    
    elif room == 10:
        # Enemy left side
        if (bullet.x + bullet.width > 350 + 50 and
            bullet.x < 350 + 50 and
            bullet.y + bullet.height > 460):
            return True
        # Enemy right side
        if (bullet.x + bullet.width > 350 + 200 and
            bullet.x < 350 + 200 and
            bullet.y + bullet.height > 460):
            return True
    
    return False
