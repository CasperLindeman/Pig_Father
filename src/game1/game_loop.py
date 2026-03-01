"""
Game 1: Main game loop for the platformer game.
"""
import pygame
from utils.constants import GRAVITY, DEFAULT_PLAYER_VELOCITY, WIN_WIDTH, WIN_HEIGHT, DARK_RED, PINK
from game1.entities import Man, Krone, Enemy, Projectile
from game1.game_state import Game1State
from game1.collision import platform, check_hitbox
from game1.gameplay import teleport, kode_puzzle, gris_ai, fall_damage, check_room_interactions
from game1.render import sprites


def run_game_1(win, images, clock):
    """Main game loop for Game 1 (platformer)."""
    # Initialize game state
    state = Game1State()
    
    # Create initial entities
    man = Man(WIN_WIDTH * 0.375, WIN_HEIGHT * 0.815, WIN_WIDTH * 0.05 / 1.6, WIN_HEIGHT * 0.05)
    krone = Krone(man.x, man.y - WIN_HEIGHT * 0.05, WIN_WIDTH * 0.05 / 1.6, WIN_HEIGHT * 0.05, images.get('krone'))
    enemy = Enemy(350, 460, 200, 300)
    enemy._grisdead_image = images.get('grisdead')
    
    # Create fonts
    font = pygame.font.SysFont(None, 100)
    font2 = pygame.font.SysFont(None, 50)
    
    # Game loop
    run = True
    while run:
        clock.tick(60)
        
        # Track runtime for speedrun times
        if enemy.health3 > 0:
            state.update_runtime()
        
        if state.delay > 0:
            state.delay -= 1
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit game
        
        # Update man color based on status
        if man.djevel:
            man.colour = DARK_RED
        else:
            man.colour = PINK
        
        # Handle damage cooldown and color flashing
        if man.hit:
            if man.damagecooldown == 0:
                man.colour = (255, 255, 255)
                man.damagecooldown = 60
            elif man.damagecooldown > 1:
                man.colour = (255, 255, 255)
                man.damagecooldown -= 1
            elif man.damagecooldown == 1:
                man.hit = False
                man.damagecooldown -= 1
        
        # Check fall damage
        fall_damage(man, state, GRAVITY)
        
        # Health check - if dead, end game
        if man.health < 1:
            return False
        
        # Check if game2 triggered
        if state.game2_triggered:
            return True
        
        # Input handling
        keys = pygame.key.get_pressed()
        
        # Movement and world interaction
        if keys[pygame.K_a] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
        
        if keys[pygame.K_d] and man.x < WIN_WIDTH - man.width - man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
        
        # Jumping
        if not man.is_jump:
            if state.room == 2 and man.x > WIN_WIDTH * 0.78125 and man.y < WIN_HEIGHT * 0.6:
                man.y -= 8
            elif man.jump:
                if keys[pygame.K_w]:
                    man.is_jump = True
                else:
                    man.y += GRAVITY
            if not man.jump:
                man.y += GRAVITY
        
        if man.is_jump:
            if man.jump_count >= -10:
                man.y -= man.jump_count * abs(man.jump_count) * 0.2 * 0.75
                man.jump_count -= 0.5
            else:
                man.is_jump = False
                man.jump_count = 10
        
        # Bullet handling
        for bullet in state.bullets[:]:  # Use slice to avoid modification during iteration
            if bullet.x < WIN_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                state.remove_bullet(bullet)
                continue
            
            if check_hitbox(bullet, state.room, [], None, None, None, {}):
                state.remove_bullet(bullet)
        
        # Shooting
        if keys[pygame.K_SPACE] and state.delay < 1 and krone.is_krone:
            state.delay = 60
            if man.left:
                facing = -1
                bullet_image = images.get('bullet_L')
            elif man.right:
                facing = 1
                bullet_image = images.get('bullet_R')
            else:
                facing = 1
                bullet_image = images.get('bullet_R')
            
            bullet = Projectile(man.x + man.width * 0.5, man.y - 20, 20, 16, facing, bullet_image)
            state.add_bullet(bullet)
        
        # Room-specific input
        check_room_interactions(man, state, {})
        
        # Update game logic
        teleport(man, state)
        
        # Apply platform collisions based on room
        if state.room == 1:
            platform(man, 0, WIN_HEIGHT * 0.865, 850, 150, GRAVITY)
            platform(man, WIN_WIDTH * 0.81875, WIN_HEIGHT * 0.865, 300, 150, GRAVITY)
        
        elif state.room == 2:
            platform(man, 0, WIN_HEIGHT * 0.865, WIN_WIDTH, 150, GRAVITY)
            platform(man, 0, WIN_HEIGHT * 0.565, WIN_WIDTH, WIN_HEIGHT * 0.05, GRAVITY)
            platform(man, 0, 400, 30, 250, GRAVITY)
        
        elif state.room == 3:
            platform(man, 0, WIN_HEIGHT * 0.865, WIN_WIDTH, 150, GRAVITY)
            # Platform collisions from entity list
            platform(man, WIN_WIDTH * 0.625, WIN_HEIGHT * 0.765, WIN_WIDTH * 0.4375, WIN_HEIGHT * 0.1, GRAVITY)
        
        elif state.room == 4:
            platform(man, 0, WIN_HEIGHT * 0.665, WIN_WIDTH * 0.9375, WIN_HEIGHT * 0.1, GRAVITY)
            platform(man, 0, WIN_HEIGHT * 0.95, WIN_WIDTH * 0.3, 100, GRAVITY)
            platform(man, WIN_WIDTH * 0.4, WIN_HEIGHT * 0.95, WIN_WIDTH * 0.6, 100, GRAVITY)
            platform(man, 1100, 150, 150, 30, GRAVITY)
        
        elif state.room == 5:
            platform(man, 0, WIN_HEIGHT * 0.665, WIN_WIDTH, WIN_HEIGHT * 0.3, GRAVITY)
            if state.koden:
                # Code puzzle solved - apply platform collisions
                pass
            else:
                kode_puzzle(man, state)
        
        elif state.room == 6:
            platform(man, 0, WIN_HEIGHT * 0.8, WIN_WIDTH, WIN_HEIGHT * 0.3, GRAVITY)
        
        elif state.room == 7:
            platform(man, 0, WIN_HEIGHT * 0.95, WIN_WIDTH, 100, GRAVITY)
        
        elif state.room == 8:
            platform(man, 0, WIN_HEIGHT * 0.95, 600, 100, GRAVITY)
            platform(man, 700, WIN_HEIGHT * 0.95, 600, 100, GRAVITY)
            platform(man, 1170, 0, 30, WIN_HEIGHT, GRAVITY)
        
        elif state.room == 9:
            platform(man, 0, 700, 1200, 100, GRAVITY)
            platform(man, 0, 0, 50, 750, GRAVITY)
        
        elif state.room == 10:
            platform(man, 0, 0, 30, 500, GRAVITY)
            platform(man, 1170, 0, 30, 700, GRAVITY)
            platform(man, 0, 700, 1200, 100, GRAVITY)
            if enemy.health3 > 0:
                platform(man, enemy.x, enemy.y, enemy.width, enemy.height, GRAVITY)
                # Check if player hits enemy from above (bounce attack)
                if (man.x + man.width > enemy.x and man.x < enemy.x + enemy.width and
                    man.y + man.height > enemy.y - 10 and man.y < enemy.y + 50):
                    if not man.bounce and man.damagecooldown == 0:
                        # Bounce attack
                        enemy.health3 -= 1
                        man.bounce = True
                        man.bouncetime = 40
                        man.damagecooldown = 15
            
            gris_ai(man, enemy, state, GRAVITY)
        
        # Bounce physics
        if man.bounce:
            if man.bouncetime > 0:
                man.y -= man.bouncetime
                man.bouncetime -= 1
            elif man.bouncetime == 0:
                man.bounce = False
        
        # Render everything
        entity_lists = {
            'platforms': [],
            'obstacles': [],
            'jumpAb': None,
        }
        sprites(win, man, krone, enemy, state, entity_lists, images, font, font2)
    
    return False
