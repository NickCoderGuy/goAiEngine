import pygame
import random
import time
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
        if option_selected == "load_game":
            exit_string = pick_load_game(game_display)
            if exit_string == "quit":
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
                        return "load_game"

def pick_load_game(game_display):
    engine_facade = GoGameFacade()
    running = True
    while running:
        CLOCK.tick(constants.FPS)
        options = game_display.display_loaded_games()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    index = 0
                    for entry in os.listdir("saved_games/"):
                        if options[index]:
                            filename = "saved_games/" + entry
                            engine_facade.load_from_file(filename)
                            run_view_ui(game_display, engine_facade)
                            return "main_menu"
                        index += 1

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

def run_view_ui(game_display, engine_facade):
    game_display.set_current_screen("view")
    current_state_index = len(engine_facade.state_history) - 1
    state = engine_facade.get_state(current_state_index)
    game_display.display_board(state['board'])
    

    # Main game loop
    running = True
    while running:
        CLOCK.tick(constants.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 means left mouse button
                
                hover_back, hover_forward, hover_pass, hover_exit, hover_resign, hover_download = game_display.get_hover(pygame.mouse.get_pos())
                
                new_state = None

                if hover_back:
                    if current_state_index > 0:
                        current_state_index -= 1
                        state = engine_facade.get_state(current_state_index)
                        game_display.display_board(state['board'])

                elif hover_forward:
                    if current_state_index < len(engine_facade.state_history) - 1:
                        current_state_index += 1
                        state = engine_facade.get_state(current_state_index)
                        game_display.display_board(state['board'])
                    
                elif hover_pass:
                    # Don't do anything
                    pass
                elif hover_exit:
                    return "menu"
                elif hover_resign:
                    # Don't do anything
                    pass
                elif hover_download:
                    # Don't do anything
                    pass
                        
                turn = engine_facade.get_turn()
                
                if new_state is not None:
                    game_display.display_board(new_state['board'],turn)


def run_ui(game_display):
    engine_facade = GoGameFacade()
    initial_state = engine_facade.new_game()['board']
    game_display.set_current_screen("game")
    
    # Define the example Go board (19x19) with initial empty intersections
    size = 19
    # example_go_board_state = [[random.choice([0, 1, 2]) for _ in range(size)] for _ in range(size)]

    # Call the display_board method to display the board
    # print(f"initial state is {initial_state}")
    game_display.display_board(initial_state)

    # We should put make a list of states and then when we "hover_forward", we go to the next one (unless we are at
    # the current state) and then when we "hover_back", we go to the previous one (unless we are at the first state).

    # Main game loop
    running = True
    current_state_index = 0
    while running:
        CLOCK.tick(constants.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.VIDEORESIZE:
                game_display.resize(event.size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # event.button == 1 means left mouse button
                
                hover_back, hover_forward, hover_pass, hover_exit, hover_resign, hover_download = game_display.get_hover(pygame.mouse.get_pos())
                
                new_state = None

                if hover_back:
                    if current_state_index > 0:
                        current_state_index -= 1
                        state = engine_facade.get_state(current_state_index)
                        game_display.display_board(state['board'])

                elif hover_forward:
                    if current_state_index < len(engine_facade.state_history) - 1:
                        current_state_index += 1
                        state = engine_facade.get_state(current_state_index)
                        game_display.display_board(state['board'])
                    
                elif hover_pass:
                    print("pass move")
                    new_state = engine_facade.pass_turn()
                elif hover_exit:
                    print("exit game")
                    return "menu"
                elif hover_resign:
                    print("resign game")
                    pass
                elif hover_download:
                    print("download/save game")
                    # get current time stamp YYYY-MM-DD_HH-MM-SS
                    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                    engine_facade.dump_to_file(f"saved_games/{timestamp}.pkl")
                    pass

                # get the location of the mouse click
                row, col = game_display.get_row_col_from_mouse(
                    pygame.mouse.get_pos())
                
                # if the location is on the board, attempt to make the move
                if row >= 0 and row < constants.ROWS and col >= 0 and col < constants.COLS:
                    # move is on board
                    current_state_index = len(engine_facade.state_history) - 1
                    try:
                        new_state = engine_facade.make_move(row, col)
                        current_state_index = len(engine_facade.state_history) - 1
                    except:
                        print("invalid move")
                        # engine_facade.state_history.pop()
                        state = engine_facade.get_state(current_state_index)
                        game_display.display_board(state['board'])
                        
                turn = engine_facade.get_turn()
                
                if new_state is not None:
                    game_display.display_board(new_state['board'],turn)

if __name__ == "__main__":
    main()
