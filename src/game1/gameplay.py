"""
Game 1: Game logic and mechanics (teleporting, platforming, enemy behavior).
"""
from utils.constants import WIN_WIDTH, WIN_HEIGHT


def teleport(man, state):
    """Handle room transitions based on player position."""
    if state.room == 1:
        if man.x < WIN_WIDTH * 0.00625:
            state.room = 2
            man.x = WIN_WIDTH - man.width - WIN_WIDTH * 0.03125
        elif man.x > WIN_WIDTH - man.width - 10:
            state.room = 3
            man.x = WIN_WIDTH * 0.031250
            man.y = WIN_HEIGHT * 0.815
    
    elif state.room == 2:
        if man.x < WIN_WIDTH * 0.075:
            man.jump = True
        if man.x > WIN_WIDTH - man.width - WIN_WIDTH * 0.006250 and man.y > WIN_HEIGHT * 0.6:
            state.room = 1
            man.x = WIN_WIDTH * 0.03125
        elif man.x < WIN_WIDTH * 0.05 and man.y < WIN_HEIGHT * 0.6:
            state.room = 3
            man.x += WIN_WIDTH * 0.09375
        elif man.y < 0:
            state.room = 7
            man.y = WIN_HEIGHT * 0.9
    
    elif state.room == 3:
        if man.x < WIN_WIDTH * 0.00625 and man.y > WIN_HEIGHT * 0.6:
            state.room = 1
            man.x = WIN_WIDTH - man.width - WIN_WIDTH * 0.03125
            man.y = WIN_HEIGHT * 0.815
        elif man.x > WIN_WIDTH - man.width - WIN_WIDTH * 0.00625:
            man.x = WIN_WIDTH * 0.0625
            state.room = 4
        elif man.x < WIN_WIDTH * 0.05 and man.y < WIN_HEIGHT * 0.6:
            state.room = 2
            man.x += WIN_WIDTH * 0.09375
    
    elif state.room == 4:
        if man.x < 20:
            man.x = WIN_WIDTH * 0.9375
            state.room = 3
        if man.y > WIN_HEIGHT - man.height - 10:
            state.room = 9
            man.y = 0
        if man.x > 1190 - man.width and man.y < 150:
            state.game2_triggered = True
    
    elif state.room == 5:
        if man.x > WIN_WIDTH * 0.9875 - man.width and man.y < WIN_HEIGHT * 0.15:
            state.room = 6
            man.y = WIN_HEIGHT * 0.7
            man.x = WIN_WIDTH * 0.5
    
    elif state.room == 6:
        if state.gud_count > 3 and state.room6_count > 0:
            state.room6_count -= 1
        if state.room6_count == 0:
            state.room = 4
            man.y = WIN_HEIGHT * 0.615
    
    elif state.room == 7:
        if man.x > 1140:
            state.room = 8
            man.x = 50
        if man.x < 20 and man.y < 450:
            state.room = 11
            man.x = 1100
            state.secret = True
    
    elif state.room == 8:
        if man.x < 20:
            state.room = 7
            man.x = 1110
        elif man.y > 735:
            state.room = 1
            man.y = 0
    
    elif state.room == 9:
        if man.x > 1180 - man.width:
            state.room = 10
            man.x = 50
    
    elif state.room == 10:
        pass
    
    elif state.room == 11:
        if man.x > 1150:
            state.room = 7
            man.x = 50


def kode_puzzle(man, state):
    """Handle the code puzzle logic for room 5."""
    if man.x < WIN_WIDTH * 0.0125 and man.y == 550 - man.height:  # Left top
        man.x = WIN_WIDTH * 0.98125 - man.width
        man.y = WIN_HEIGHT * 0.615
        if state.kode1 and not state.kode2:
            state.kode2 = True
        else:
            state.reset_code_puzzle()
    
    elif man.x < WIN_WIDTH * 0.0125 and man.y == WIN_HEIGHT * 0.615:  # Left bottom
        man.x = WIN_WIDTH * 0.98125 - man.width
        man.y = 550 - man.height
        if state.kode1 and state.kode2 and not state.kode3:
            state.kode3 = True
        elif state.kode1 and state.kode2 and state.kode3:
            state.kode4 = True
        else:
            state.reset_code_puzzle()
    
    elif man.x > WIN_WIDTH * 0.9875 - man.width and man.y == 550 - man.height:  # Right top
        man.x = WIN_WIDTH * 0.01875
        man.y = WIN_HEIGHT * 0.615
        if not state.kode1:
            state.kode1 = True
        else:
            state.kode1 = True
            state.kode2 = False
            state.kode3 = False
            state.kode4 = False
            state.kode5 = False
    
    elif man.x > WIN_WIDTH * 0.9875 - man.width and man.y == WIN_HEIGHT * 0.615:  # Right bottom
        man.x = WIN_WIDTH * 0.01875
        man.y = 550 - man.height
        if state.kode1 and state.kode2 and state.kode3 and state.kode4:
            state.kode5 = True
            state.koden = True
        else:
            state.reset_code_puzzle()


def gris_ai(man, enemy, state, grav):
    """Handle enemy AI and damage mechanics."""
    if state.room == 9:
        man.health = 5
        enemy.health1 = 8
        enemy.health2 = 8
        enemy.health3 = 8
    
    elif state.room == 10:
        if enemy.health1 > 0 or enemy.health2 > 0 or enemy.health3 > 0:
            if enemy.count > 0:
                enemy.count -= 1
                enemy.x += enemy.vel
            elif enemy.count > -enemy.walk:
                enemy.count -= 1
                enemy.x -= enemy.vel
            else:
                enemy.count = enemy.walk
        
        if enemy.health3 > 0:
            if man.hit:
                pass
            elif (man.x + man.width > enemy.x - 3 and
                  man.x < enemy.x + enemy.width + 3 and
                  man.y + man.height > enemy.y and
                  man.y < enemy.y + enemy.height):
                man.health -= 1
                man.hit = True


def fall_damage(man, state, grav):
    """Handle damage from falling."""
    if man.y > 750:
        man.health -= 1
        man.y = 400
        man.hit = True
        man.damagecooldown = 60


def check_room_interactions(man, state, keys):
    """Check room-specific interactions."""
    if state.room == 4:
        if keys.get('pygame.K_e') and man.x > WIN_WIDTH * 0.4875 - man.width and man.x < WIN_WIDTH * 0.55:
            state.room = 5
    
    elif state.room == 6:
        if state.dialog_sleep > 0:
            state.dialog_sleep -= 1
        elif keys.get('pygame.K_e') and state.dialog_sleep < 1:
            state.dialog_sleep = 20
            state.gud_count += 1
