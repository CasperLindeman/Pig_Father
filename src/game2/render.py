"""
Game 2: Rendering and UI for action RPG.
"""
import pygame


X = 50  # Grid cell size
Y = 50


def render_walls(win, room, man, key4, enemies):
    """Render all walls and obstacles for a room."""
    WHITE = (255, 255, 255)
    GRAY = (80, 80, 80)
    GUL = (255, 255, 0)
    
    # Perimeter walls
    pygame.draw.rect(win, WHITE, (0, 0, 50, 350))
    pygame.draw.rect(win, WHITE, (0, 450, 50, 350))
    pygame.draw.rect(win, WHITE, (0, 0, 550, 50))
    pygame.draw.rect(win, WHITE, (0, 750, 550, 50))
    pygame.draw.rect(win, WHITE, (650, 0, 550, 50))
    pygame.draw.rect(win, WHITE, (650, 750, 550, 50))
    pygame.draw.rect(win, WHITE, (1150, 0, 50, 350))
    pygame.draw.rect(win, WHITE, (1150, 450, 50, 350))
    
    if room == 1:
        pygame.draw.rect(win, GRAY, (550, 0, 100, 50))
        pygame.draw.rect(win, GUL, (X * 10, Y * 6, 4 * X, 4 * Y))
        
        # Platforms
        for i in range(5):
            pygame.draw.rect(win, WHITE, (X * 9, Y * (5 + i), 50, 50))
        pygame.draw.rect(win, WHITE, (X * 10, Y * 10, 50, 50))
        pygame.draw.rect(win, WHITE, (X * 13, Y * 10, 50, 50))
        
        for i in range(5):
            pygame.draw.rect(win, WHITE, (X * (10 + i), Y * 5, 50, 50))
        
        for i in range(6):
            pygame.draw.rect(win, WHITE, (X * 14, Y * (5 + i), 50, 50))
    
    elif room == 2:
        # Complex maze layout
        maze_platforms = [
            (X * 0, Y * 7, 50, 2 * 50),
            (X * 11, Y * 15, 2 * 50, 50),
            (X * 23, Y * 7, 50, 2 * 50),
            (X * 2, Y * 2, 50, 8 * 50),
            (X * 3, Y * 4, 3 * 50, 50),
            (X * 3, Y * 8, 2 * 50, 50),
            (X * 4, Y * 9, 2 * 50, 50),
            (X * 6, Y * 8, 50, 4 * 50),
        ]
        for x, y, w, h in maze_platforms:
            pygame.draw.rect(win, WHITE, (x, y, w, h))
        
        pygame.draw.rect(win, GUL, (X * 11, Y * 10, 2 * 50, 2 * 50))
    
    elif room == 3:
        pygame.draw.rect(win, WHITE, (X * 10, Y * 5, 50, 10 * 50))
        pygame.draw.rect(win, WHITE, (X * 11, Y * 5, 7 * 50, 50))
        pygame.draw.rect(win, WHITE, (X * 17, Y * 1, 50, 4 * 50))
    
    elif room == 4:
        pygame.draw.rect(win, WHITE, (X * 23, Y * 7, 50, 2 * 50))
        pygame.draw.rect(win, WHITE, (X * 11, Y * 15, 2 * 50, 50))
        pygame.draw.rect(win, WHITE, (X * 10, Y * 1, 50, 11 * 50))
        pygame.draw.rect(win, WHITE, (X * 10, Y * 11, 9 * 50, 50))
        pygame.draw.rect(win, WHITE, (X * 5, Y * 3, 50, 12 * 50))
        pygame.draw.rect(win, WHITE, (X * 18, Y, 50, 7 * 50))
        
        if not key4.key:
            pygame.draw.rect(win, GRAY, (X * 10, Y * 12, 50, 3 * 50))


def render_sprites(win, man, sword, enemies, key4, room):
    """Render all sprites and entities."""
    # Enemies
    for enemy in enemies:
        if enemy.health > 0:
            enemy.draw(win)
    
    # Sword
    if sword.is_sword and sword.cooldown > 15:
        sword.draw(win)
    
    # Key
    if room == 4 and not key4.key:
        key4.draw(win)
    
    # Health bar
    for i in range(5):
        if man.health > i:
            pygame.draw.rect(win, (255, 0, 0), (50 + i * 50 + 25, 75, 20, 20))
        pygame.draw.rect(win, (0, 0, 0), (50 + i * 50 + 25, 75, 20, 20), 2)
    
    # Player
    man.draw(win)


def sprites_game2(win, man, sword, enemies, key4, state):
    """Main rendering for Game 2."""
    win.fill((0, 0, 0))
    render_walls(win, state.room, man, key4, enemies)
    render_sprites(win, man, sword, enemies, key4, state.room)
    pygame.display.update()
