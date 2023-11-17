from ui.constants import BLACK, WHITE, BACKGROUND, DARK_GRAY
import os


class GameDisplay:

    def __init__(self,pygame) -> None:
        # Define constants
        self.NUM_LINES = 18
        self.BORDER_SIZE = 3
        self.SAFE_AREA = 50
        self.GRID_LINE_WIDTH = 1
        self.CONTROLS_HEIGHT = 100
        
        self.pygame = pygame

        self.pixel_size = 540
        self.cell_size = self.pixel_size // self.NUM_LINES
        self.board_padding = self.cell_size

        self.window_height = 0
        self.window_width = 0

        self.current_screen = "main_menu"

        self.set_up_pygame()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = ((y - self.SAFE_AREA // 2) - self.cell_size // 2) // self.cell_size 
        col = ((x - self.SAFE_AREA // 2) - self.cell_size // 2) // self.cell_size
        return row, col

    def set_up_pygame(self):
        # Initialize Pygame
        
        self.pygame.display.set_caption("Go Board")

        # Calculate the total height of the window (including the button section)
        self.window_height = self.pixel_size + \
            self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
        self.window_width = self.pixel_size + self.SAFE_AREA + self.board_padding * 2
        self.screen =self.pygame.display.set_mode((self.window_width, self.window_height),self.pygame.RESIZABLE)
        
        initial_go_board_state = [[0 for _ in range(self.NUM_LINES + 1)] for _ in range(self.NUM_LINES + 1)]

        # self.display_board(initial_go_board_state)
        self.display_main_menu()


    def get_valid_screen_size(self, new_screen_size):
        # Round to the nearest multiple of NUM_LINES
        new_screen_size = ((new_screen_size[0] - (self.SAFE_AREA + self.board_padding)) // self.NUM_LINES * self.NUM_LINES,
                           (new_screen_size[1] - (self.SAFE_AREA + self.board_padding)) // self.NUM_LINES * self.NUM_LINES)
        return max(432, min(new_screen_size[0], new_screen_size[1]))
    
    def resize(self, new_screen_size):
        print(f"new screen size: {new_screen_size}")
        self.pixel_size = self.get_valid_screen_size(new_screen_size)
        print(f"pixel size: {self.pixel_size}")
        self.cell_size = (
            self.pixel_size // self.NUM_LINES) - (2 * self.BORDER_SIZE // self.NUM_LINES)
        self.window_height = self.pixel_size + \
            self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
        self.board_padding = self.cell_size
        self.window_width = self.pixel_size + self.SAFE_AREA + 2 * self.board_padding
        
        self.screen = self.pygame.display.set_mode((self.window_width, self.window_height), self.pygame.RESIZABLE)

        if self.current_screen == "main_menu":
            self.display_main_menu()
        else:
            self.display_board(self.pieces_array)

    def display_board(self, new_pieces_array):
        self.pieces_array = new_pieces_array
        # Create a background surface and fill it with the background color
        background_surface = self.pygame.Surface(
            (self.pixel_size + self.SAFE_AREA + 2 * self.board_padding, self.window_height))
        background_surface.fill(BACKGROUND)

        # Create a controls surface
        controls_surface = self.pygame.Surface(
            (self.pixel_size + 2 * self.board_padding, self.CONTROLS_HEIGHT))
        controls_surface.fill(BLACK)

        # Draw buttons or other elements on the control surface
        # For example:
        # self.pygame.draw.rect(controls_surface, (255, 0, 0), (0, 0, 100, self.CONTROLS_HEIGHT))

        # Create a board surface and fill it with the background color

        # self.board_padding = self.cell_size

        board_surface = self.pygame.Surface((self.pixel_size + 2 * self.board_padding, self.pixel_size + 2 * self.board_padding))
        board_surface.fill(BACKGROUND)

        for i in range(self.NUM_LINES):
            self.pygame.draw.line(board_surface, BLACK, (self.cell_size * i + self.board_padding, self.board_padding),
                             (self.cell_size * i + self.board_padding, self.pixel_size + self.board_padding), self.GRID_LINE_WIDTH)
            self.pygame.draw.line(board_surface, BLACK, (self.board_padding, self.cell_size * i + self.board_padding),
                             (self.pixel_size + self.board_padding, self.cell_size * i + self.board_padding), self.GRID_LINE_WIDTH)

        # Star points
        star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9),
                       (15, 9), (3, 15), (9, 15), (15, 15)]
        for point in star_points:
            self.pygame.draw.circle(
                board_surface, BLACK, (self.cell_size * point[0] + self.board_padding, self.cell_size * point[1] + self.board_padding), 6)

        # Draw a rim around the game board
        self.pygame.draw.rect(board_surface, BLACK, (self.board_padding, self.board_padding,
                         self.pixel_size, self.pixel_size), 
                         self.BORDER_SIZE)
        
        for row in range(len(self.pieces_array)):
            for col in range(len(self.pieces_array[row])):
                if self.pieces_array[row][col] == 1:
                    self.pygame.draw.circle(
                        board_surface, BLACK, (self.cell_size * col + self.board_padding, self.cell_size * row + self.board_padding), self.cell_size // 2 - 1)
                elif self.pieces_array[row][col] == 2:
                    self.pygame.draw.circle(
                        board_surface, WHITE, (self.cell_size * col + self.board_padding, self.cell_size * row + self.board_padding), self.cell_size // 2 - 1)

        self.screen.blit(background_surface, (0, 0))
        self.screen.blit(controls_surface, (self.SAFE_AREA //
                         2, self.pixel_size + self.SAFE_AREA))
        # Blit the background and board surfaces on the main screen
        self.screen.blit(
            board_surface, (self.SAFE_AREA // 2, self.SAFE_AREA // 2))

        # Update the screen
        self.pygame.display.flip()


    def display_main_menu(self):
        self.pygame.display.set_caption("Go")
        button_width = self.pixel_size // 2
        button_height = 50
        margin = self.window_width // 2 - button_width // 2

        start_button_rect = self.pygame.Rect(margin, self.window_height // 2, button_width, button_height)
        against_cpu_rect = self.pygame.Rect(margin, self.window_height // 1.72, button_width, button_height)
        quit_button_rect = self.pygame.Rect(margin, self.window_height // 1.5, button_width, button_height)

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
        button_width = self.pixel_size // 2
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