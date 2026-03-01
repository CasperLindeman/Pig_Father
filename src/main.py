"""
Pig Father - Main Entry Point
Coordinates the platformer (Game 1) and action RPG (Game 2) games.
"""
import os
import pygame
from utils.constants import WIN_HEIGHT, WIN_WIDTH
from game1.game_loop import run_game_1
from game2.game_loop import run_game_2


def load_images():
    """Load all game images and return as a dictionary."""
    images = {}
    
    # Change to sprites directory
    sprite_dir = os.path.join(os.path.dirname(__file__), '..', 'sprites')
    
    image_files = {
        'bg': 'bg_1_2.png',
        'gulv1': 'gulv_1_2.png',
        'bro': 'bro_1_2.png',
        'darkRoomEnt': 'darkroom_2.png',
        'bg3': 'bgs_2.jpg',
        'bg4': 'bg4_2.png',
        'bg6': 'bg6_2.png',
        'floor4': 'floor4_2.png',
        'w': 'w_2.png',
        'krone': 'krone_2.png',
        'bullet_R': 'bullet_R_2.png',
        'bullet_L': 'bullet_L_2.png',
        'grisdead': 'gris.png',
        'room3_1': 'room3_1_2.png',
        'portal': 'portal_2.png',
        'hindring1': 'hindring1_2.png',
        'hindring2': 'hindring2_2.png',
        'hindring3': 'hindring3_2.png',
        'DRGulv': 'gulv_2_2.png',
        'jumpBord': 'jumpbord_2.png',
        'floorRoom2': 'gulv_2_2_2.png',
        'levitasjon': 'levitasjon_2.png',
        'fakkel': 'fakkel_2.png',
        'gud1': 'gud1_2.png',
        'gud2': 'gud2_2.png',
        'gud3': 'gud3_2.png',
        'djeveldør': 'djeveldør.png',
    }
    
    for name, filename in image_files.items():
        try:
            filepath = os.path.join(sprite_dir, filename)
            images[name] = pygame.image.load(filepath)
        except pygame.error as e:
            print(f"Warning: Could not load image {filename}: {e}")
            images[name] = None
    
    return images


def main():
    """Main entry point for Pig Father."""
    # Initialize Pygame
    pygame.init()
    
    # Create window
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Pig Father")
    
    # Create clock for FPS
    clock = pygame.time.Clock()
    
    # Load all images
    images = load_images()
    
    # Run Game 1 (Platformer)
    game1_completed = run_game_1(win, images, clock)
    
    # If game 1 completed, run Game 2 (Action RPG)
    #if game1_completed:
    #    game2_completed = run_game_2(win, clock)
    
    # Quit
    pygame.quit()
    print("Game ended. Thanks for playing!")


if __name__ == "__main__":
    main()
