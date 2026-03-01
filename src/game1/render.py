"""
Game 1: Rendering and UI display.
"""
import pygame
from utils.constants import WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE, DARK_RED, DARK_YELLOW


def message(msg, colour, x, y, font, win):
    """Render text message on screen."""
    text = font.render(msg, True, colour)
    win.blit(text, [x, y])


def render_health_bar(win, man):
    """Render player health bar."""
    health_x = 50 + 25
    health_y = 50
    
    for i in range(5):
        x = health_x + (i * 50)
        if man.health > i:
            pygame.draw.rect(win, (255, 0, 0), (x, health_y, 20, 20))
        pygame.draw.rect(win, BLACK, (x, health_y, 20, 20), 2)


def render_room_1(win, man, images, font, font2):
    """Render room 1: Tutorial area."""
    win.blit(images.get('bg', pygame.Surface((0, 0))), (0, 0))
    win.blit(images.get('gulv1', pygame.Surface((0, 0))), (0, WIN_HEIGHT * 0.815 + man.height))
    pygame.draw.rect(win, (5, 5, 0), (WIN_WIDTH * 0.70625, WIN_HEIGHT * 0.865, WIN_WIDTH * 0.18125, WIN_HEIGHT * 0.2))
    win.blit(images.get('bro', pygame.Surface((0, 0))), (WIN_WIDTH * 0.81875, WIN_HEIGHT * 0.865))
    win.blit(images.get('darkRoomEnt', pygame.Surface((0, 0))), (0, WIN_HEIGHT * 0.22))
    
    if not man.jump:
        if 350 < man.x < 500 and man.y > 600:
            pygame.draw.rect(win, WHITE, (380, 280, 300, 200))
            message("A and D", BLACK, 400, 300, font, win)
            message("to move", BLACK, 400, 400, font, win)
            pygame.draw.rect(win, WHITE, (300, 150, 550, 50))
            message("Top left corner is your health", BLACK, 310, 160, font2, win)


def render_room_2(win, man, krone, jumpAb, images):
    """Render room 2: Jump tutorial."""
    win.fill(BLACK)
    win.blit(images.get('jumpBord', pygame.Surface((0, 0))), (WIN_WIDTH * 0.059375, WIN_HEIGHT * 0.83))
    
    # Floor tiles
    for i in range(4):
        win.blit(images.get('DRGulv', pygame.Surface((0, 0))),
                (WIN_WIDTH * -0.05 + WIN_WIDTH * 0.285 * i, WIN_HEIGHT * 0.865))
        win.blit(images.get('DRGulv', pygame.Surface((0, 0))),
                (WIN_WIDTH * -0.05 + WIN_WIDTH * 0.285 * i, WIN_HEIGHT * 0.938))
    
    win.blit(images.get('levitasjon', pygame.Surface((0, 0))), (WIN_WIDTH * 0.71875, WIN_HEIGHT * 0.08))
    
    if not man.jump:
        jumpAb.draw(win)
    
    if man.x < WIN_WIDTH * 0.075 and not krone.is_krone:
        pygame.draw.rect(win, WHITE, (380, 280, 300, 200))


def render_room_3(win, man, krone, images):
    """Render room 3: Crown collection puzzle."""
    win.blit(images.get('bg3', pygame.Surface((0, 0))), (0, 0))
    
    if man.x > 1050 and krone.is_krone:
        pygame.draw.rect(win, WHITE, (380, 280, 300, 200))


def render_room_4(win, man, images, font, font2):
    """Render room 4: World transition."""
    win.blit(images.get('bg4', pygame.Surface((0, 0))), (0, 0))
    win.blit(images.get('floor4', pygame.Surface((0, 0))), (0, WIN_HEIGHT * 0.665))
    pygame.draw.rect(win, BLACK, (1100, 150, 150, 30))
    
    if man.y == WIN_HEIGHT * 0.615:
        if WIN_WIDTH * 0.4875 - man.width < man.x < WIN_WIDTH * 0.55:
            win.blit(images.get('w', pygame.Surface((0, 0))), (WIN_WIDTH * 0.4875, WIN_HEIGHT * 0.22))
            pygame.draw.rect(win, WHITE, (WIN_WIDTH * 0.5, WIN_HEIGHT * 0.245, 40, 30))
            message("E", BLACK, WIN_WIDTH * 0.51, WIN_HEIGHT * 0.25, font2, win)
    
    if man.x > 990 - man.width or man.y > WIN_HEIGHT * 0.665:
        pygame.draw.rect(win, BLACK, (0, WIN_HEIGHT * 0.765, 1200, WIN_HEIGHT * 0.95 - WIN_HEIGHT * 0.765))
        pygame.draw.rect(win, BLACK, (WIN_WIDTH * 0.9375, WIN_HEIGHT * 0.665, 100, WIN_HEIGHT * 0.285))
        pygame.draw.rect(win, BLACK, (WIN_WIDTH * 0.3, WIN_HEIGHT * 0.94, WIN_WIDTH * 0.1, 200))


def render_room_5(win, state, images):
    """Render room 5: Code puzzle."""
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (211, 211, 211), (0, WIN_HEIGHT * 0.665, WIN_WIDTH, WIN_HEIGHT * 0.35))
    
    if state.koden:
        for i in range(5):
            win.blit(images.get('fakkel', pygame.Surface((0, 0))),
                    (WIN_WIDTH * 0.21875 + WIN_WIDTH * 0.125 * i, WIN_HEIGHT * 0.8))
    else:
        if state.kode1:
            win.blit(images.get('fakkel', pygame.Surface((0, 0))), (WIN_WIDTH * 0.218750, WIN_HEIGHT * 0.8))
        if state.kode2:
            win.blit(images.get('fakkel', pygame.Surface((0, 0))), (WIN_WIDTH * 0.34375, WIN_HEIGHT * 0.8))
        if state.kode3:
            win.blit(images.get('fakkel', pygame.Surface((0, 0))), (WIN_WIDTH * 0.46875, WIN_HEIGHT * 0.8))
        if state.kode4:
            win.blit(images.get('fakkel', pygame.Surface((0, 0))), (WIN_WIDTH * 0.59375, WIN_HEIGHT * 0.8))


def render_room_6(win, state, images):
    """Render room 6: Dialog gate."""
    win.blit(images.get('bg6', pygame.Surface((0, 0))), (0, 0))
    if state.gud_count == 1:
        win.blit(images.get('gud1', pygame.Surface((0, 0))), (0, 0))
    elif state.gud_count == 2:
        win.blit(images.get('gud2', pygame.Surface((0, 0))), (0, 0))
    elif state.gud_count == 3:
        win.blit(images.get('gud3', pygame.Surface((0, 0))), (0, 0))


def render_room_7(win, obstacle_list, plat_list, images):
    """Render room 7: Dark descent."""
    win.fill(BLACK)
    for obs in obstacle_list:
        obs.draw(win)
    for plat in plat_list:
        if hasattr(plat, 'draw'):
            plat.draw(win)


def render_room_8(win, man, djevel, images):
    """Render room 8: Devil transformation."""
    win.fill(BLACK)
    win.blit(images.get('djeveldør', pygame.Surface((0, 0))), (500, 500))
    pygame.draw.rect(win, (255, 155, 0), (500, 500, 10, 210))
    pygame.draw.rect(win, (255, 155, 0), (780, 500, 10, 210))
    pygame.draw.rect(win, (255, 155, 0), (500, 500, 280, 10))
    
    if man.x > 500 - man.width and man.x < 790:
        pygame.draw.rect(win, (0, 0, 255), (600, 710, 100, 100))


def render_room_9(win):
    """Render room 9: Healing room."""
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (211, 211, 211), (0, WIN_HEIGHT * 0.665, WIN_WIDTH, WIN_HEIGHT * 0.35))
    pygame.draw.rect(win, (150, 0, 150), (0, 0, 50, 750))
    pygame.draw.rect(win, (150, 0, 150), (0, 700, 1200, 100))


def render_room_10(win, enemy, plat_list, images, font):
    """Render room 10: Final boss arena."""
    win.fill(BLACK)
    pygame.draw.rect(win, (150, 0, 150), (0, 0, 50, 750))
    pygame.draw.rect(win, (150, 0, 150), (0, 700, 1200, 100))
    pygame.draw.rect(win, (150, 0, 150), (0, 0, 30, 500))
    pygame.draw.rect(win, (150, 0, 150), (1170, 0, 30, 700))
    
    for plat in plat_list:
        if hasattr(plat, 'draw'):
            plat.draw(win)
    
    enemy.draw(win)


def render_room_11(win, font):
    """Render room 11: Credits/secret room."""
    win.fill(BLACK)


def render_boss_death(win, enemy, man, state, font):
    """Render boss defeat screen."""
    if enemy.health3 < 1:
        pygame.draw.rect(win, BLACK, (0, 0, WIN_WIDTH, WIN_HEIGHT))
        message("You KILLED Satan", (255, 0, 0), 300, 100, font, win)
        message("Time:", WHITE, 400, 200, font, win)
        finaltime = str(state.runtime)
        message(finaltime, WHITE, 600, 200, font, win)
        if man.djevel:
            message("Completionist", WHITE, 400, 300, font, win)
        if state.runtime < 150:
            message("Speedrunner", WHITE, 400, 400, font, win)
        if state.runtime <= 90:
            message("True Master", DARK_YELLOW, 500, 400, font, win)
        if state.secret:
            message("!!!You found the Secret room!!!", WHITE, 110, 500, font, win)


def sprites(win, man, krone, enemy, state, entity_lists, images, font, font2):
    """Main rendering function that combines all room rendering."""
    if state.room == 1:
        render_room_1(win, man, images, font, font2)
    
    elif state.room == 2:
        render_room_2(win, man, krone, entity_lists.get('jumpAb'), images)
    
    elif state.room == 3:
        render_room_3(win, man, krone, images)
    
    elif state.room == 4:
        render_room_4(win, man, images, font, font2)
    
    elif state.room == 5:
        render_room_5(win, state, images)
    
    elif state.room == 6:
        render_room_6(win, state, images)
    
    elif state.room == 7:
        render_room_7(win, entity_lists.get('obstacles', []), entity_lists.get('platforms', []), images)
    
    elif state.room == 8:
        render_room_8(win, man, man.djevel, images)
    
    elif state.room == 9:
        render_room_9(win)
    
    elif state.room == 10:
        render_room_10(win, enemy, entity_lists.get('platforms', []), images, font)
    
    elif state.room == 11:
        render_room_11(win, font)
    
    # Render HUD
    render_health_bar(win, man)
    
    # Render crown
    krone.x = man.x - WIN_WIDTH * 0.00625
    krone.y = man.y - WIN_HEIGHT * 0.05
    if krone.is_krone:
        krone.draw(win)
    
    # Render bullets
    for bullet in state.bullets:
        bullet.draw(win)
    
    # Render boss death
    if state.room == 10:
        render_boss_death(win, enemy, man, state, font)
    
    # Draw player last
    man.draw(win)
    
    pygame.display.update()
