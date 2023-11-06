from ui.board import Board
from ui.constants import BLACK, WHITE, GRAY, BACKGROUND, ROWS, COLS


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
        self.board = Board(self.cell_size, self.SAFE_AREA)
        # Height of the button section

        self.set_up_pygame()

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = (y - self.SAFE_AREA // 2 + self.cell_size // 2) // self.cell_size 
        col = (x - self.SAFE_AREA // 2 + self.cell_size // 2) // self.cell_size
        return row, col

    def set_up_pygame(self):
        # Initialize Pygame
        
        self.pygame.display.set_caption("Go Board")

        # Calculate the total height of the window (including the button section)
        self.window_height = self.pixel_size + \
            self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
        self.screen =self.pygame.display.set_mode(
            (self.pixel_size + self.SAFE_AREA, self.window_height),self.pygame.RESIZABLE)
        
        self.update_screen()


    def get_valid_screen_size(self, new_screen_size):
        # Round to the nearest multiple of NUM_LINES
        new_screen_size = (new_screen_size[0] // self.NUM_LINES * self.NUM_LINES,
                           new_screen_size[1] // self.NUM_LINES * self.NUM_LINES)
        return max(432, min(new_screen_size[0], new_screen_size[1]))

    def update_screen(self):
        # Create a background surface and fill it with the background color
        background_surface = self.pygame.Surface(
            (self.pixel_size + self.SAFE_AREA, self.window_height))
        background_surface.fill(BACKGROUND)

        # Create a controls surface
        controls_surface = self.pygame.Surface(
            (self.pixel_size, self.CONTROLS_HEIGHT))
        controls_surface.fill(BLACK)

        # Draw buttons or other elements on the control surface
        # For example:
        # self.pygame.draw.rect(controls_surface, (255, 0, 0), (0, 0, 100, self.CONTROLS_HEIGHT))

        # Create a board surface and fill it with the background color
        board_surface = self.pygame.Surface((self.pixel_size, self.pixel_size))
        board_surface.fill(BACKGROUND)

        for i in range(self.NUM_LINES):
            self.pygame.draw.line(board_surface, BLACK, (self.cell_size * i, 0),
                             (self.cell_size * i, self.pixel_size), self.GRID_LINE_WIDTH)
            self.pygame.draw.line(board_surface, BLACK, (0, self.cell_size * i),
                             (self.pixel_size, self.cell_size * i), self.GRID_LINE_WIDTH)

        # Star points
        star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9),
                       (15, 9), (3, 15), (9, 15), (15, 15)]
        for point in star_points:
            self.pygame.draw.circle(
                board_surface, BLACK, (self.cell_size * point[0], self.cell_size * point[1]), 6)

        # Draw a rim around the game board
        self.pygame.draw.rect(board_surface, BLACK, (0, 0,
                         self.pixel_size, self.pixel_size), self.BORDER_SIZE)

        # Blit the background and board surfaces on the main screen
        self.screen.blit(background_surface, (0, 0))
        self.screen.blit(controls_surface, (self.SAFE_AREA //
                         2, self.pixel_size + self.SAFE_AREA))
        self.screen.blit(
            board_surface, (self.SAFE_AREA // 2, self.SAFE_AREA // 2))

        self.board.draw(self.screen, self.cell_size)

        white_left, black_left = self.board.get_pieces_left()
        turn = self.board.get_turn()
        white_captures, black_captures = self.board.get_captures()

        # draw the text to display the number of pieces left

        self.screen.blit(self.pygame.font.SysFont('Arial', 20).render('White pieces left: ' + str(white_left) + ' White Captures: ' +
                         str(white_captures), True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 20))
        self.screen.blit(self.pygame.font.SysFont('Arial', 20).render('Black pieces left: ' + str(black_left) + ' Black Captures: ' +
                         str(black_captures), True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 40))

        # draw the text to display whose turn it is

        if (turn % 2 == 0):
            self.screen.blit(self.pygame.font.SysFont('Arial', 20).render(
                'Black\'s turn', True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 60))
        else:
            self.screen.blit(self.pygame.font.SysFont('Arial', 20).render(
                'White\'s turn', True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 60))

        # Update the screen
        self.pygame.display.flip()
