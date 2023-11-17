import pygame
import random
from ui.game_display import GameDisplay
import ui.constants as constants
import os

CLOCK = pygame.time.Clock()

def main():
    # Initialize Pygame
    pygame.init()
    game_display = GameDisplay(pygame)
    main_menu(game_display)
    run_ui(game_display)

def main_menu(game_display):
    running = True
    while running:
        CLOCK.tick(constants.FPS)
        hover_start, hover_cpu, hover_quit = game_display.display_main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if hover_start:
                        game_display.set_current_screen("game")
                        return
                    elif hover_cpu:
                        pick_cpu(game_display)
                        return
                    elif hover_quit:
                        pygame.quit()

def pick_cpu(game_display):
    running = True
    while running:
        CLOCK.tick(constants.FPS)
        options = game_display.display_options()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    index = 0
                    for entry in os.listdir("AIlist/"):
                        if options[index]:
                            print(entry)
                            game_display.set_current_screen("game")
                            return
                        index += 1

def run_ui(game_display):
    # Define the example Go board (19x19) with initial empty intersections
    size = 19
    example_go_board_state = [[random.choice([0, 1, 2]) for _ in range(size)] for _ in range(size)]

    # Call the display_board method to display the board
    game_display.display_board(example_go_board_state)

    # Main game loop
    running = True
    while running:
        CLOCK.tick(constants.FPS)
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