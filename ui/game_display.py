import pygame
from board import Board
from constants import BLACK,WHITE,GRAY,BACKGROUND,CELL_SIZE,NUM_LINES,ROWS,COLS
class GameDisplay:
    
    def __init__(self) -> None:
        # Define constants
        self.NUM_LINES = 18
        self.BORDER_SIZE = 3
        self.SAFE_AREA = 50
        self.GRID_LINE_WIDTH = 1
        self.CONTROLS_HEIGHT = 100

        self.pixel_size = 540
        self.cell_size = self.pixel_size // self.NUM_LINES
        self.board = Board(self.cell_size)

        # Height of the button section
        
        self.set_up_pygame()
        
    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        return row, col

    def set_up_pygame(self):
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Go Board")

        # Calculate the total height of the window (including the button section)
        self.window_height = self.pixel_size + self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
        self.screen = pygame.display.set_mode((self.pixel_size + self.SAFE_AREA, self.window_height), pygame.RESIZABLE)

        # Run the game loop
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.VIDEORESIZE:
                    self.pixel_size = self.get_valid_screen_size(event.size)
                    self.cell_size = (self.pixel_size // self.NUM_LINES) - (2 * self.BORDER_SIZE // self.NUM_LINES)
                    self.window_height = self.pixel_size + self.CONTROLS_HEIGHT + (1.5 * self.SAFE_AREA)
                    self.screen = pygame.display.set_mode((self.pixel_size + self.SAFE_AREA, self.window_height), pygame.RESIZABLE)
                    
                # this is for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get the location of the mouse click
                    row, col = self.get_row_col_from_mouse(pygame.mouse.get_pos())
                    # get the piece at that location
                    piece = self.board.get_piece(row,col)
                    # move the piece
                    self.board.move(piece)
                    
                if event.type == pygame.MOUSEMOTION:
                    #row, col = self.get_row_col_from_mouse(pygame.mouse.get_pos())
                    #piece = self.board.get_piece(row,col)
                    pass
                    
                
                self.update_screen()

        # Quit Pygame
        pygame.quit()

    def get_valid_screen_size(self, new_screen_size):
        # Round to the nearest multiple of NUM_LINES
        new_screen_size = (new_screen_size[0] // self.NUM_LINES * self.NUM_LINES,
                           new_screen_size[1] // self.NUM_LINES * self.NUM_LINES)
        return max(432, min(new_screen_size[0], new_screen_size[1]))

    def update_screen(self):
        # Create a background surface and fill it with the background color
        background_surface = pygame.Surface((self.pixel_size + self.SAFE_AREA, self.window_height))
        background_surface.fill(BACKGROUND)

        # Create a controls surface
        controls_surface = pygame.Surface((self.pixel_size, self.CONTROLS_HEIGHT))
        controls_surface.fill(BLACK)

        # Draw buttons or other elements on the control surface
        # For example:
        # pygame.draw.rect(controls_surface, (255, 0, 0), (0, 0, 100, self.CONTROLS_HEIGHT))

        # Create a board surface and fill it with the background color
        board_surface = pygame.Surface((self.pixel_size, self.pixel_size))
        board_surface.fill(BACKGROUND)

        for i in range(self.NUM_LINES):
            pygame.draw.line(board_surface, BLACK, (self.cell_size * i, 0),
                             (self.cell_size * i, self.pixel_size), self.GRID_LINE_WIDTH)
            pygame.draw.line(board_surface, BLACK, (0, self.cell_size * i),
                             (self.pixel_size, self.cell_size * i), self.GRID_LINE_WIDTH)

        # Star points
        star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9),
                       (15, 9), (3, 15), (9, 15), (15, 15)]
        for point in star_points:
            pygame.draw.circle(
                board_surface, BLACK, (self.cell_size * point[0], self.cell_size * point[1]), 6)

        # Draw a rim around the game board
        pygame.draw.rect(board_surface, BLACK, (0, 0, self.pixel_size, self.pixel_size), self.BORDER_SIZE)

        # Blit the background and board surfaces on the main screen
        self.screen.blit(background_surface, (0, 0))
        self.screen.blit(controls_surface, (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA))
        self.screen.blit(board_surface, (self.SAFE_AREA // 2, self.SAFE_AREA // 2))
        
        self.board.draw(self.screen,self.cell_size)
        
        white_left,black_left = self.board.get_pieces_left()
        turn = self.board.get_turn()
        
        # draw the text to display the number of pieces left
        
        self.screen.blit(pygame.font.SysFont('Arial', 20).render('White pieces left: ' + str(white_left), True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 20))
        self.screen.blit(pygame.font.SysFont('Arial', 20).render('Black pieces left: ' + str(black_left), True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 40))
        
        # draw the text to display whose turn it is
        
        if(turn % 2 == 0):
            self.screen.blit(pygame.font.SysFont('Arial', 20).render('Black\'s turn', True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 60))
        else:
            self.screen.blit(pygame.font.SysFont('Arial', 20).render('White\'s turn', True, WHITE), (self.SAFE_AREA // 2, self.pixel_size + self.SAFE_AREA + 60))

        # Update the screen
        pygame.display.flip()
