import pygame
import random
from ui.game_display import GameDisplay

def main():
    run_ui()
   
def run_ui():
    # Initialize Pygame
    pygame.init()

    # Define the standard Go board (19x19) with initial empty intersections
    size = 19
    example_go_board_state = [[random.choice([0, 1, 2]) for _ in range(size)] for _ in range(size)]

    # Create a GameDisplay object
    game_display = GameDisplay(pygame)

    # Call the display_board method to display the board
    game_display.display_board(example_go_board_state)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 means left mouse button
                # get the location of the mouse click
                row, col = game_display.get_row_col_from_mouse(
                    pygame.mouse.get_pos())
                
                print(row, col)
                
                # fixme implement this pseudocode ->
                # new_state = engine.getnextstate()
                # game_display.display_board(new_state)
                

    pygame.quit()

if __name__ == "__main__":
    main()