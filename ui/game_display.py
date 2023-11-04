from ui.constants import BLACK, WHITE, BACKGROUND


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
        self.screen =self.pygame.display.set_mode(
            (self.pixel_size + self.SAFE_AREA + self.board_padding * 2, self.window_height),self.pygame.RESIZABLE)
        
        initial_go_board_state = [[0 for _ in range(self.NUM_LINES + 1)] for _ in range(self.NUM_LINES + 1)]

        self.display_board(initial_go_board_state)


    def get_valid_screen_size(self, new_screen_size):
        # Round to the nearest multiple of NUM_LINES
        new_screen_size = ((new_screen_size[0] - self.SAFE_AREA) // self.NUM_LINES * self.NUM_LINES,
                           (new_screen_size[1] - self.SAFE_AREA) // self.NUM_LINES * self.NUM_LINES)
        return max(432, min(new_screen_size[0], new_screen_size[1]))
    
    def resize(self, new_screen_size):
        self.pixel_size = self.get_valid_screen_size(new_screen_size)
        self.cell_size = (
            self.pixel_size // self.NUM_LINES) - (2 * self.BORDER_SIZE // self.NUM_LINES)
        self.window_height = self.pixel_size + \
            self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
        self.board_padding = self.cell_size
        self.screen = self.pygame.display.set_mode(
            (self.pixel_size + self.SAFE_AREA + 2 * self.board_padding, self.window_height), self.pygame.RESIZABLE)
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

        self.board_padding = self.cell_size

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