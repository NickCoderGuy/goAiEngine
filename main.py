from ui.game_display import GameDisplay
import pygame

def main():
    run_ui()
   
def run_ui():
 # start board
    pygame.init()
    running = True
    game_display = GameDisplay(pygame)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                game_display.pixel_size = game_display.get_valid_screen_size(event.size)
                game_display.cell_size = (
                    game_display.pixel_size // game_display.NUM_LINES) - (2 * game_display.BORDER_SIZE // game_display.NUM_LINES)
                window_height = game_display.pixel_size + \
                    game_display.CONTROLS_HEIGHT + (1.5 * game_display.SAFE_AREA)
                game_display.screen = pygame.display.set_mode(
                    (game_display.pixel_size + game_display.SAFE_AREA, window_height), pygame.RESIZABLE)
                game_display.update_screen()

            # this is for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # get the location of the mouse click
                row, col = game_display.get_row_col_from_mouse(
                    pygame.mouse.get_pos())
                # get the piece at that location
                piece = game_display.board.get_piece(row, col)
                # move the piece
                game_display.board.move(piece)
                game_display.update_screen()
                

            if event.type == pygame.MOUSEMOTION:
                # row, col = get_row_col_from_mouse(pygame.mouse.get_pos())
                # piece = board.get_piece(row,col)
                pass

    pygame.quit()

if __name__ == "__main__":
    main()