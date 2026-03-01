"""
Game 2: Main game loop for the action RPG.
"""
import pygame
from utils.constants import GAME2_WIN_HEIGHT, GAME2_WIN_WIDTH, GAME2_PLAYER_VELOCITY
from game2.entities import ManGame2, Sword, Opponent1, Key4
from game2.game_state import Game2State
from game2.collision import platform, check_sword_enemy_collision, check_enemy_damage
from game2.ai import update_enemy_ai
from game2.render import sprites_game2


def run_game_2(win, clock):
    """Main game loop for Game 2 (action RPG)."""
    # Resize window for game2
    win = pygame.display.set_mode((GAME2_WIN_WIDTH, GAME2_WIN_HEIGHT))
    pygame.display.set_caption("Pig Father - RPG")
    
    # Initialize game state
    state = Game2State()
    
    # Create player
    man = ManGame2(GAME2_WIN_WIDTH * 0.5, GAME2_WIN_HEIGHT * 0.5, 40, 40)
    
    # Create sword
    sword = Sword(0, 0, 10, 30)
    
    # Create enemies list
    enemies = []
    
    # Create key
    key4 = Key4(21 * 50, 2 * 50, 20, 20)
    
    # Create first room opponents
    opponent3_1 = Opponent1(11 * 50, 13 * 50, 30, 30, 3)
    opponent3_2 = Opponent1(11 * 50 + 25, 14 * 50, 30, 30, 3)
    
    # Game loop
    run = True
    while run and man.health > 0:
        clock.tick(60)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # Input handling
        keys = pygame.key.get_pressed()
        
        # 4-directional movement
        if keys[pygame.K_LEFT] and man.x > GAME2_PLAYER_VELOCITY:
            man.x -= GAME2_PLAYER_VELOCITY
            man.facing = 4
        
        if keys[pygame.K_RIGHT] and man.x < GAME2_WIN_WIDTH - man.width - GAME2_PLAYER_VELOCITY:
            man.x += GAME2_PLAYER_VELOCITY
            man.facing = 2
        
        if keys[pygame.K_UP] and man.y > GAME2_PLAYER_VELOCITY:
            man.y -= GAME2_PLAYER_VELOCITY
            man.facing = 1
        
        if keys[pygame.K_DOWN] and man.y < GAME2_WIN_HEIGHT - man.height - GAME2_PLAYER_VELOCITY:
            man.y += GAME2_PLAYER_VELOCITY
            man.facing = 3
        
        # Sword mechanics
        if not sword.is_sword:
            if man.sword and keys[pygame.K_x]:
                sword.is_sword = True
                sword.cooldown = 30
        
        if sword.is_sword:
            if sword.cooldown > 0:
                sword.cooldown -= 1
                # Update sword position based on facing direction
                sword.x = man.x
                sword.y = man.y
                
                if man.facing == 1:  # Up
                    sword.x += 15
                    sword.y -= sword.height
                    sword.width = 10
                    sword.height = 30
                elif man.facing == 2:  # Right
                    sword.x += man.width
                    sword.y += 15
                    sword.width = 30
                    sword.height = 10
                elif man.facing == 3:  # Down
                    sword.x += 15
                    sword.y += man.height
                    sword.width = 10
                    sword.height = 30
                elif man.facing == 4:  # Left
                    sword.x -= 30
                    sword.y += 15
                    sword.width = 30
                    sword.height = 10
                
                # Check sword collision with enemies
                killed_enemy, knockback_dir = check_sword_enemy_collision(sword, enemies, man)
                if killed_enemy:
                    state.remove_enemy(killed_enemy)
                    if knockback_dir:
                        # Apply knockback
                        if knockback_dir == 1:
                            man.y += 15
                        elif knockback_dir == 2:
                            man.x -= 15
                        elif knockback_dir == 3:
                            man.y -= 15
                        elif knockback_dir == 4:
                            man.x += 15
            else:
                sword.is_sword = False
        
        # Room transitions
        old_room = state.room
        _handle_room_transitions(man, state, enemies)
        
        if state.room != old_room:
            # Handle enemy spawning on room entry
            if state.room == 3 and old_room == 1:
                state.clear_enemies()
                state.add_enemy(opponent3_1)
                state.add_enemy(opponent3_2)
        
        # Platform collisions
        _apply_platform_collisions(man, state, enemies)
        
        # Enemy AI
        update_enemy_ai(enemies, man, sword)
        
        # Enemy damage to player
        state.damagecooldown, player_hit = check_enemy_damage(man, enemies, state.damagecooldown)
        if player_hit:
            man.health -= 1
            man.colour = (255, 0, 0)
        elif state.damagecooldown > 0:
            man.colour = (255, 0, 0)
        else:
            man.colour = (255, 0, 255)
        
        # Healing room
        if state.room == 9:
            man.health = 5
        
        # Render
        sprites_game2(win, man, sword, enemies, key4, state)
    
    return man.health > 0


def _handle_room_transitions(man, state, enemies):
    """Handle room transitions."""
    X, Y = 50, 50
    
    if state.room == 1:
        if X * 11 < man.x < X * 13 - man.width and man.y > 800 - 20 - man.height:
            man.y = Y * 1
            state.room = 2
        if man.x < 20 and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X * 23 - 10
            state.room = 3
        elif man.x > 1180 - man.width and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X
            state.room = 8
    
    elif state.room == 2:
        if X * 11 < man.x < X * 13 - man.width and man.y < 20:
            man.y = 800 - 50 - man.height
            state.room = 1
    
    elif state.room == 3:
        if X * 11 < man.x < X * 13 - man.width and man.y < 20:
            man.y = 800 - 50 - man.height
            state.room = 7
        elif X * 11 < man.x < X * 13 - man.width and man.y > 800 - 20 - man.height:
            man.y = Y * 1
            state.room = 4
        elif man.x > 1180 - man.width and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X
            state.room = 1
        elif man.x < 20 and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X * 23 - 10
            state.room = 6
    
    elif state.room == 4:
        if man.x < 20 and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X * 23 - 10
            state.room = 5
        if X * 11 < man.x < X * 13 - man.width and man.y < 20:
            man.y = 800 - 50 - man.height
            state.room = 3
    
    elif state.room == 5:
        if X * 11 < man.x < X * 13 - man.width and man.y < 20:
            man.y = 800 - 50 - man.height
            state.room = 6
        elif man.x > 1180 - man.width and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X
            state.room = 4
    
    elif state.room == 6:
        if man.x > 1180 - man.width and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X
            state.room = 3
        elif X * 11 < man.x < X * 13 - man.width and man.y > 800 - 20 - man.height:
            man.y = Y * 1
            state.room = 5
    
    elif state.room == 7:
        if X * 11 < man.x < X * 13 - man.width and man.y > 800 - 20 - man.height:
            man.y = Y * 1
            state.room = 3
    
    elif state.room == 8:
        if man.x < 20 and man.y > Y * 7 and man.y < Y * 9 - man.height:
            man.x = X * 23 - 10
            state.room = 1


def _apply_platform_collisions(man, state, enemies):
    """Apply platform collision detection based on current room."""
    X, Y = 50, 50
    vel = 5
    
    # Perimeter walls
    platform(man, 0, 0, 50, 350, enemies, vel)
    platform(man, 0, 450, 50, 350, enemies, vel)
    platform(man, 0, 0, 550, 50, enemies, vel)
    platform(man, 0, 750, 550, 50, enemies, vel)
    platform(man, 650, 0, 550, 50, enemies, vel)
    platform(man, 650, 750, 550, 50, enemies, vel)
    platform(man, 1150, 0, 50, 350, enemies, vel)
    platform(man, 1150, 450, 50, 350, enemies, vel)
    
    if state.room == 1:
        platform(man, 550, 0, 100, 50, enemies, vel)
        platform(man, X * 9, Y * 5, 50, 50 * 6, enemies, vel)
        platform(man, X * 10, Y * 5, 4 * 50, 50, enemies, vel)
        platform(man, X * 10, Y * 10, 50, 50, enemies, vel)
        platform(man, X * 13, Y * 10, 50, 50, enemies, vel)
        platform(man, X * 14, Y * 5, 50, 6 * 50, enemies, vel)
    
    elif state.room == 2:
        # Apply all maze platforms
        pass
    
    elif state.room == 3:
        platform(man, X * 10, Y * 5, 50, 10 * 50, enemies, vel)
        platform(man, X * 11, Y * 5, 7 * 50, 50, enemies, vel)
        platform(man, X * 17, Y * 1, 50, 4 * 50, enemies, vel)
    
    elif state.room == 4:
        platform(man, X * 23, Y * 7, 50, 2 * 50, enemies, vel)
        platform(man, X * 11, Y * 15, 2 * 50, 50, enemies, vel)
        platform(man, X * 10, Y * 1, 50, 11 * 50, enemies, vel)
        platform(man, X * 10, Y * 11, 9 * 50, 50, enemies, vel)
        platform(man, X * 5, Y * 3, 50, 12 * 50, enemies, vel)
        platform(man, X * 18, Y, 50, 7 * 50, enemies, vel)
