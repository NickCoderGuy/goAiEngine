from ui.constants import BLACK, WHITE, BACKGROUND, DARK_GRAY, GREEN, OLIVE, BLUE, FIREBRICK, TRANSPARENT
import os


class GameDisplay:

    def __init__(self, pygame) -> None:
        # Define constants
        self.pieces_array = None
        self.NUM_LINES = 18
        self.BORDER_SIZE = 3
        self.SAFE_AREA = 50
        self.GRID_LINE_WIDTH = 1
        self.CONTROLS_HEIGHT = 100
        self.BUTTON_PADDING = 10

        self.pygame = pygame

        self.grid_size = 540
        self.cell_size = self.grid_size // self.NUM_LINES
        self.board_padding = self.cell_size

        self.current_screen = "main_menu"

        self.pygame.display.set_caption("Go Board")

        # Calculate the total height of the window (including the button section)
        self.window_height = self.grid_size + self.CONTROLS_HEIGHT + (2 * self.SAFE_AREA) + (2 * self.board_padding)
        self.window_width = self.grid_size + self.SAFE_AREA + self.board_padding * 2
        self.screen = self.pygame.display.set_mode((self.window_width, self.window_height), self.pygame.RESIZABLE)

        self.display_main_menu()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = ((y - self.SAFE_AREA // 2) - self.cell_size // 2) // self.cell_size
        col = ((x - self.SAFE_AREA // 2) - self.cell_size // 2) // self.cell_size
        return row, col

    def get_valid_screen_size(self, new_screen_size):
        # Round to the nearest multiple of NUM_LINES
        new_screen_size = (
        (new_screen_size[0] - (self.SAFE_AREA + self.board_padding)) // self.NUM_LINES * self.NUM_LINES,
        (new_screen_size[1] - (self.SAFE_AREA + self.board_padding)) // self.NUM_LINES * self.NUM_LINES)
        return max(432, min(new_screen_size[0], new_screen_size[1]))

    def resize(self, new_screen_size):
        self.grid_size = self.get_valid_screen_size(new_screen_size)
        self.cell_size = (
                                 self.grid_size // self.NUM_LINES) - (2 * self.BORDER_SIZE // self.NUM_LINES)
        self.board_padding = self.cell_size
        self.window_height = self.grid_size + self.CONTROLS_HEIGHT + (2 * self.SAFE_AREA) + (2 * self.board_padding)
        self.window_width = self.grid_size + self.SAFE_AREA + 2 * self.board_padding

        self.screen = self.pygame.display.set_mode((self.window_width, self.window_height), self.pygame.RESIZABLE)

        if self.current_screen == "main_menu":
            self.display_main_menu()
        else:
            self.display_board(self.pieces_array)

    def display_board(self, new_pieces_array,turn=0):
        if self.current_screen != "game":
            self.set_current_screen("game")
            
        self.pieces_array = new_pieces_array
        # Create a background surface and fill it with the background color
        background_surface = self.pygame.Surface(
            (self.grid_size + self.SAFE_AREA + 2 * self.board_padding, self.window_height))
        background_surface.fill(BACKGROUND)

        board_surface = self.pygame.Surface(
            (self.grid_size + 2 * self.board_padding, self.grid_size + 2 * self.board_padding))
        board_surface.fill(BACKGROUND)

        for i in range(self.NUM_LINES):
            self.pygame.draw.line(board_surface, BLACK, (self.cell_size * i + self.board_padding, self.board_padding),
                                  (self.cell_size * i + self.board_padding, self.grid_size + self.board_padding),
                                  self.GRID_LINE_WIDTH)
            self.pygame.draw.line(board_surface, BLACK, (self.board_padding, self.cell_size * i + self.board_padding),
                                  (self.grid_size + self.board_padding, self.cell_size * i + self.board_padding),
                                  self.GRID_LINE_WIDTH)

        # Star points
        star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9),
                       (15, 9), (3, 15), (9, 15), (15, 15)]
        for point in star_points:
            self.pygame.draw.circle(
                board_surface,
                BLACK,
                (self.cell_size * point[0] + self.board_padding, self.cell_size * point[1] + self.board_padding), 6)

        # Draw a rim around the game board
        self.pygame.draw.rect(board_surface, BLACK, (self.board_padding,
                                                     self.board_padding,
                                                     self.grid_size,
                                                     self.grid_size), self.BORDER_SIZE)

        for row in range(len(self.pieces_array)):
            for col in range(len(self.pieces_array[row])):
                color = None
                if self.pieces_array[row][col] == 1:
                    color = BLACK
                if self.pieces_array[row][col] == 2:
                    color = WHITE

                if color is not None:
                    self.pygame.draw.circle(
                        board_surface,
                        color,
                        (self.cell_size * col + self.board_padding, self.cell_size * row + self.board_padding),
                        self.cell_size // 2 - 1)

        self.screen.blit(background_surface, (0, 0))
        # self.screen.blit(controls_surface, (self.SAFE_AREA //
        #                   2, self.pixel_size + self.SAFE_AREA))
        # Blit the background and board surfaces on the main screen
        self.screen.blit(
            board_surface, (self.SAFE_AREA // 2, self.SAFE_AREA // 2))

        self.display_ui_controls(turn)

        # Update the screen
        self.pygame.display.flip()

    def display_ui_controls(self,turn):
        # Create a controls surface
        control_surface_width = self.grid_size + 2 * self.board_padding
        controls_surface = self.pygame.Surface((control_surface_width, self.CONTROLS_HEIGHT))
        controls_surface.fill(BACKGROUND)

        # if black is greater than white then it is whites turn
        turn_color = WHITE if turn != 0 else BLACK
        
        self.pygame.draw.circle(controls_surface, turn_color, (1 * (control_surface_width / 9), self.CONTROLS_HEIGHT // 2),
                                    self.cell_size // 2 - 1)

        # draw the forward and back buttons
        back_arrow = self.pygame.image.load("ui/images/left-arrow.png")
        forward_arrow = self.pygame.image.load("ui/images/right-arrow.png")
        pass_button = self.pygame.image.load("ui/images/curve-down-arrow.png")
        resign_button = self.pygame.image.load("ui/images/finish.png")
        exit_button = self.pygame.image.load("ui/images/logout.png")
        download_button = self.pygame.image.load("ui/images/downloads.png")

        # put the forward arrow on the forward button in to the controls surface
        forward_arrow = self.pygame.transform.smoothscale(forward_arrow, (self.cell_size, self.cell_size))
        back_arrow = self.pygame.transform.smoothscale(back_arrow, (self.cell_size, self.cell_size))
        resign_button = self.pygame.transform.smoothscale(resign_button, (self.cell_size, self.cell_size))
        pass_button = self.pygame.transform.smoothscale(pass_button, (self.cell_size, self.cell_size))
        exit_button = self.pygame.transform.smoothscale(exit_button, (self.cell_size, self.cell_size))
        download_button = self.pygame.transform.smoothscale(download_button, (self.cell_size, self.cell_size))

        # move the buttons to the correct position
        back_rect = back_arrow.get_rect()
        forward_rect = forward_arrow.get_rect()
        pass_rect = pass_button.get_rect()
        resign_rect = resign_button.get_rect()
        exit_rect = exit_button.get_rect()
        download_rect = download_button.get_rect()

        # this sets the position of the buttons. change these to change button locations (width, height)
        y_location = self.grid_size + self.SAFE_AREA + 2 * self.board_padding + self.CONTROLS_HEIGHT // 2
        back_rect.center = (3 * (control_surface_width / 9), y_location)
        forward_rect.center = (4 * (control_surface_width / 9), y_location)
        resign_rect.center = (5 * (control_surface_width / 9), y_location)
        pass_rect.center = (6 * (control_surface_width / 9), y_location)
        exit_rect.center = (7 * (control_surface_width / 9), y_location)
        download_rect.center = (8 * (control_surface_width / 9), y_location)

        # this is necessary because the location is stored for
        # the hover function if needed
        self.back_rect = back_rect
        self.forward_rect = forward_rect
        self.pass_rect = pass_rect
        self.resign_rect = resign_rect
        self.exit_rect = exit_rect
        self.download_rect = download_rect

        # blit the controls surface
        self.screen.blit(controls_surface, (self.SAFE_AREA //
                                            2, self.grid_size + self.SAFE_AREA + 2 * self.board_padding))
        
        # for the hover function to work properly, 
        # the buttons must be blitted to the main screen,
        # not the controls surface
        self.screen.blit(back_arrow, back_rect)
        self.screen.blit(forward_arrow, forward_rect)
        self.screen.blit(resign_button, resign_rect)
        self.screen.blit(pass_button, pass_rect)
        self.screen.blit(exit_button, exit_rect)
        self.screen.blit(download_button, download_rect)

        
    def get_hover(self, mouse_position):
        # get if the mouse is hovering over the buttons
        hover_forward = self.forward_rect.collidepoint(mouse_position)
        hover_back = self.back_rect.collidepoint(mouse_position)
        hover_resign = self.resign_rect.collidepoint(mouse_position)
        hover_pass = self.pass_rect.collidepoint(mouse_position)
        hover_exit = self.exit_rect.collidepoint(mouse_position)
        hover_download = self.download_rect.collidepoint(mouse_position)

        return hover_back, hover_forward, hover_pass, hover_exit, hover_resign, hover_download

    def display_main_menu(self):
        self.pygame.display.set_caption("Go")
        button_width = self.grid_size // 2
        button_height = 50
        margin = self.window_width // 2 - button_width // 2

        start_button_rect = self.pygame.Rect(margin, self.window_height // 2, button_width, button_height)
        against_cpu_rect = self.pygame.Rect(margin,
                                            self.window_height // 2 + button_height + self.BUTTON_PADDING,
                                            button_width,
                                            button_height)
        quit_button_rect = self.pygame.Rect(margin,
                                            self.window_height // 2 + 2 * button_height + 2 * self.BUTTON_PADDING,
                                            button_width,
                                            button_height)

        hover_start = start_button_rect.collidepoint(self.pygame.mouse.get_pos())
        hover_cpu = against_cpu_rect.collidepoint(self.pygame.mouse.get_pos())
        hover_quit = quit_button_rect.collidepoint(self.pygame.mouse.get_pos())

        # Draw the background
        self.screen.fill(BACKGROUND)

        # Draw buttons
        self.draw_button("Start Game", start_button_rect, hover_start)
        self.draw_button("CPU", against_cpu_rect, hover_cpu)
        self.draw_button("Quit", quit_button_rect, hover_quit)

        self.pygame.display.flip()
        return hover_start, hover_cpu, hover_quit

    def display_options(self):
        button_width = self.grid_size // 2
        button_height = 50
        margin = self.window_width // 2 - button_width // 2

        # Draw the background
        self.screen.fill(BACKGROUND)

        index = 0
        buttons = []
        options = []
        for entry in os.listdir("AIlist/"):
            buttons.append(self.pygame.Rect(margin, self.window_height // (index + 1.5), button_width, button_height))
            options.append(buttons[index].collidepoint(self.pygame.mouse.get_pos()))
            self.draw_button(entry, buttons[index], options[index])
            index += 1

        self.pygame.display.flip()
        return options

    def draw_button(self, text, rect, hover):
        # Define fonts

        self.pygame.font.init()
        font = self.pygame.font.SysFont(None, 36)
        color = BLACK if not hover else DARK_GRAY
        self.pygame.draw.rect(self.screen, color, rect)

        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def set_current_screen(self, screen):
        # set to main_menu, board, or whatever other screen
        self.current_screen = screen

    def get_current_screen(self):
        return self.current_screen
