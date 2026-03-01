"""
Game 2: Enemy AI and behavior.
"""


def update_enemy_ai(enemies, man, sword):
    """Update enemy AI - walking and collision with sword.
    
    Returns: (enemies_killed, knockback_info)
    """
    enemies_killed = 0
    knockback_info = None
    
    for enemy in enemies:
        if enemy.health > 0:
            # Enemy movement on 2 axes
            if enemy.facing:  # Horizontal movement
                if enemy.count > 0:
                    enemy.count -= 1
                    enemy.x += enemy.vel
                elif enemy.count > -enemy.walk:
                    enemy.count -= 1
                    enemy.x -= enemy.vel
                else:
                    enemy.count = enemy.walk
            else:  # Vertical movement
                if enemy.count > 0:
                    enemy.count -= 1
                    enemy.y += enemy.vel
                elif enemy.count > -enemy.walk:
                    enemy.count -= 1
                    enemy.y -= enemy.vel
                else:
                    enemy.count = enemy.walk
    
    return enemies_killed, knockback_info


def check_sword_enemy_collision(sword, enemies, man):
    """Check if sword hits enemy and apply damage/knockback.
    
    Returns: (enemy_to_remove, knockback_direction)
    """
    if not sword.is_sword:
        return None, None
    
    for enemy in enemies:
        if (sword.x + sword.width > enemy.x and sword.x < enemy.x + enemy.width and
            sword.y + sword.height > enemy.y and sword.y < enemy.y + enemy.height):
            enemy.health -= 1
            knockback_dir = man.facing
            return enemy if enemy.health <= 0 else None, knockback_dir
    
    return None, None
