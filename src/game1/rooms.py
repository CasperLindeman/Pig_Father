"""
Game 1: Room definitions and entity initialization.
"""
from utils.constants import (
    WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE, PINK, DARK_RED, DARK_YELLOW
)
from game1.entities import (
    Man, Enemy, Krone, JumpAb, Platform1, Platform2, Platform3,
    Projectile, Hindring, Hindring2
)


def create_room_1(images):
    """Room 1: Tutorial area with boss preview."""
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.865, 850, 150),
            (WIN_WIDTH * 0.81875, WIN_HEIGHT * 0.865, 300, 150),
        ],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_2(images):
    """Room 2: Jump tutorial."""
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.865, WIN_WIDTH, 150),
            (0, WIN_HEIGHT * 0.565, WIN_WIDTH, WIN_HEIGHT * 0.05),
        ],
        'walls': [(0, 400, 30, 250)],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_3(images):
    """Room 3: Crown collection puzzle."""
    hindring3 = Hindring(
        WIN_WIDTH * 0.25, WIN_HEIGHT * 0.165,
        WIN_WIDTH * 0.046875, WIN_HEIGHT * 0.4,
        5, images.get('hindring1')
    )
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.865, WIN_WIDTH, 150),
        ],
        'walls': [],
        'obstacles': [hindring3],
        'collectibles': [],
        'entities': [
            Platform1(WIN_WIDTH * 0.625, WIN_HEIGHT * 0.765,
                     WIN_WIDTH * 0.4375, WIN_HEIGHT * 0.1, images.get('room3_1')),
            Platform1(WIN_WIDTH * 0.84375, WIN_HEIGHT * 0.765 - WIN_HEIGHT * 0.1,
                     WIN_WIDTH * 0.4375, WIN_HEIGHT * 0.104, images.get('room3_1')),
            Platform1(WIN_WIDTH * 0.3125, WIN_HEIGHT * 0.765 - WIN_HEIGHT * 0.1 * 2,
                     WIN_WIDTH * 0.4375, WIN_HEIGHT * 0.104, images.get('room3_1')),
            Platform1(WIN_WIDTH * -0.125, WIN_HEIGHT * 0.765 - WIN_HEIGHT * 0.1 * 2,
                     WIN_WIDTH * 0.4375, WIN_HEIGHT * 0.104, images.get('room3_1')),
        ],
    }


def create_room_4(images):
    """Room 4: World transition room."""
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.665, WIN_WIDTH * 0.9375, WIN_HEIGHT * 0.1),
            (0, WIN_HEIGHT * 0.95, WIN_WIDTH * 0.3, 100),
            (WIN_WIDTH * 0.4, WIN_HEIGHT * 0.95, WIN_WIDTH * 0.6, 100),
            (1100, 150, 150, 30),
        ],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_5(images):
    """Room 5: Code puzzle room."""
    platforms = [
        (0, WIN_HEIGHT * 0.665, WIN_WIDTH, WIN_HEIGHT * 0.3),
        Platform2(0, WIN_HEIGHT * 0.550, WIN_WIDTH * 0.1875, WIN_HEIGHT * 0.02, BLACK),
        Platform2(WIN_WIDTH * 0.8125, WIN_HEIGHT * 0.55, WIN_WIDTH * 0.187500, WIN_HEIGHT * 0.02, BLACK),
        Platform2(WIN_WIDTH * 0.1875, WIN_HEIGHT * 0.425, WIN_WIDTH * 0.09375, WIN_HEIGHT * 0.04, BLACK),
        Platform2(WIN_WIDTH * 0.3125, WIN_HEIGHT * 0.3, WIN_WIDTH * 0.09375, WIN_HEIGHT * 0.04, BLACK),
        Platform2(WIN_WIDTH * 0.5, WIN_HEIGHT * 0.175, WIN_WIDTH * 0.09375, WIN_HEIGHT * 0.04, BLACK),
        Platform2(WIN_WIDTH * 0.78125, WIN_HEIGHT * 0.3, WIN_WIDTH * 0.125, WIN_HEIGHT * 0.04, BLACK),
        Platform2(WIN_WIDTH * 0.90625, WIN_HEIGHT * 0.175, WIN_WIDTH * 0.125, WIN_HEIGHT * 0.04, BLACK),
    ]
    return {
        'platforms': platforms,
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_6(images):
    """Room 6: Dialog gate room."""
    return {
        'platforms': [(0, WIN_HEIGHT * 0.8, WIN_WIDTH, WIN_HEIGHT * 0.3)],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_7(images):
    """Room 7: Dark descent room with destructible obstacles."""
    hindring7 = Hindring2(WIN_WIDTH * 0.75, 0, 10, 200, 3, DARK_RED)
    hindring7_2 = Hindring2(100, 0, 10, 270, 3, DARK_RED)
    
    plat7_4 = Platform2(WIN_WIDTH * 0.75 - 40, hindring7.height, 100, 100, WHITE)
    plat7_5 = Platform2(0, WIN_HEIGHT * 0.95 - 230, WIN_WIDTH * 0.5, 30, DARK_RED)
    plat7_6 = Platform2(0, plat7_5.y - 100, 20, 100, (0, 255, 0))
    plat7_7 = Platform2(1180, plat7_5.y - 200, 20, 100, (0, 255, 0))
    plat7_8 = Platform2(0, plat7_5.y - 200, 20, 100, (255, 255, 0))
    plat7_9 = Platform2(1180, plat7_5.y - 300, 20, 100, (255, 255, 0))
    plat7_10 = Platform2(570, 0, 30, 200, DARK_RED)
    plat7_11 = Platform2(0, plat7_5.y - 220, 300, 30, DARK_RED)
    plat7_12 = Platform2(400, 0, 10, 100, DARK_RED)
    plat7_13 = Platform2(385, 100, 40, 40, (150, 0, 150))
    
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.95, WIN_WIDTH, 100),
            (plat7_5.x, plat7_5.y, plat7_5.width, plat7_5.height),
        ],
        'walls': [],
        'obstacles': [hindring7, hindring7_2],
        'collectibles': [],
        'entities': [plat7_4, plat7_5, plat7_6, plat7_7, plat7_8, plat7_9, plat7_10, plat7_11, plat7_12, plat7_13],
    }


def create_room_8(images):
    """Room 8: Devil transformation room."""
    return {
        'platforms': [
            (0, WIN_HEIGHT * 0.95, 600, 100),
            (700, WIN_HEIGHT * 0.95, 600, 100),
        ],
        'walls': [(1170, 0, 30, WIN_HEIGHT)],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_9(images):
    """Room 9: Healing room."""
    return {
        'platforms': [(0, 700, 1200, 100), (0, 0, 50, 750)],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def create_room_10(images):
    """Room 10: Final boss arena."""
    enemy = Enemy(350, 460, 200, 300)
    
    plat10_1 = Platform3(50, 350, 150, 50, 1, False, 300, 450)
    plat10_2 = Platform3(1000, 500, 150, 50, 1, False, -150, 450)
    plat10_3 = Platform3(300, 350, 150, 50, 1, True, 450, 450)
    plat10_4 = Platform3(700, 200, 150, 50, 3, True, 0, 150)
    
    return {
        'platforms': [
            (0, 0, 30, 500),
            (1170, 0, 30, 700),
            (0, 700, 1200, 100),
        ],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [plat10_1, plat10_2, plat10_3, plat10_4],
        'enemy': enemy,
    }


def create_room_11(images):
    """Room 11: Secret room (credits)."""
    return {
        'platforms': [],
        'walls': [],
        'obstacles': [],
        'collectibles': [],
        'entities': [],
    }


def get_room(room_num, images):
    """Get room data by room number."""
    rooms = {
        1: create_room_1,
        2: create_room_2,
        3: create_room_3,
        4: create_room_4,
        5: create_room_5,
        6: create_room_6,
        7: create_room_7,
        8: create_room_8,
        9: create_room_9,
        10: create_room_10,
        11: create_room_11,
    }
    return rooms[room_num](images)
