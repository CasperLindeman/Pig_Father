"""
Game 2: Collision detection and physics for action RPG.
"""


def platform(man, x, y, width, height, enemies, vel):
    """Detect and resolve platform collisions for player and enemies."""
    # Player collisions
    if man.y + man.height > y and man.y < y + height and man.x + man.width > x and man.x + man.width < x + 2 * vel:
        man.x = x - man.width
    elif man.y + man.height > y and man.y < y + height and man.x < x + width and man.x > x + width - vel * 2:
        man.x = x + width
    if man.y + man.height > y and man.y + man.height < y + 2 * vel and man.x + man.width > x and man.x < x + width:
        man.y = y - man.height
    elif man.y < y + height and man.y > y + height - vel * 2 and man.x + man.width > x and man.x < x + width:
        man.y = y + height
    
    # Enemy collisions
    for enemy in enemies:
        if enemy.y + enemy.height > y and enemy.y < y + height and enemy.x + enemy.width > x and enemy.x + enemy.width < x + 2 * vel:
            enemy.x = x - enemy.width
        elif enemy.y + enemy.height > y and enemy.y < y + height and enemy.x < x + width and enemy.x > x + width - vel * 2:
            enemy.x = x + width
        if enemy.y + enemy.height > y and enemy.y + enemy.height < y + 2 * vel and enemy.x + man.width > x and enemy.x < x + width:
            enemy.y = y - enemy.height
        elif enemy.y < y + height and enemy.y > y + height - vel * 2 and enemy.x + enemy.width > x and enemy.x < x + width:
            enemy.y = y + height


def check_sword_hitbox(sword, enemies):
    """Check if sword hits any enemies."""
    for enemy in enemies:
        if (sword.x + sword.width > enemy.x and sword.x < enemy.x + enemy.width and
            sword.y + sword.height > enemy.y and sword.y < enemy.y + enemy.height):
            return enemy
    return None


def check_enemy_damage(man, enemies, damagecooldown):
    """Check if enemies hit the player.
    
    Returns: (new_damagecooldown, player_damaged)
    """
    if damagecooldown > 0:
        return damagecooldown - 1, False
    
    for enemy in enemies:
        if (man.x + man.width > enemy.x and man.x < enemy.x + enemy.width and
            man.y + man.height > enemy.y and man.y < enemy.y + enemy.height):
            return 60, True
    
    return damagecooldown, False
