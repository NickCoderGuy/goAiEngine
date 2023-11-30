import pygame
import random
from ui.game_display import GameDisplay
import ui.constants as constants
from engine.gogamefacade import GoGameFacade
import os

CLOCK = pygame.time.Clock()


def main():
    # Initialize Pygame
    pygame.init()
    game_display = GameDisplay(pygame)

    while True:
        CLOCK.tick(constants.FPS)
        option_selected = main_menu(game_display)
        if option_selected == "quit":
            pygame.quit()
            return
        elif option_selected == "pick_cpu":
            print("pick cpu")
            pick_cpu(game_display)
        elif option_selected == "start_game":
            exit_string = run_ui(game_display)
            if exit_string == "quit":
                pygame.quit()
                return


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
                        return "start_game"
                    elif hover_cpu:
                        return "pick_cpu"
                    elif hover_quit:
                        return "quit"


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
    engine_facade = GoGameFacade()
    initial_state = engine_facade.new_game()['board']
    
    # Define the example Go board (19x19) with initial empty intersections
    size = 19
    # example_go_board_state = [[random.choice([0, 1, 2]) for _ in range(size)] for _ in range(size)]

    # Call the display_board method to display the board
    print(f"initial state is {initial_state}")
    game_display.display_board(initial_state)

    # We should put make a list of states and then when we "hover_forward", we go to the next one (unless we are at
    # the current state) and then when we "hover_back", we go to the previous one (unless we are at the first state).

    # Main game loop
    running = True
    while running:
        CLOCK.tick(constants.FPS)

        hover_back, hover_forward, hover_pass, hover_exit, hover_resign, hover_download = game_display.display_ui_controls()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 means left mouse button

                if hover_back:
                    print("back")
                    pass
                elif hover_forward:
                    print("forward")
                    pass
                elif hover_pass:
                    print("pass move")
                    pass
                elif hover_exit:
                    print("exit game")
                    return "menu"
                elif hover_resign:
                    print("resign game")
                    pass
                elif hover_download:
                    print("download/save game")
                    pass

                # get the location of the mouse click
                row, col = game_display.get_row_col_from_mouse(
                    pygame.mouse.get_pos())

                # print(row, col)
                new_state = engine_facade.make_move(row, col)
                game_display.display_board(new_state['board'])
                


if __name__ == "__main__":
    main()
