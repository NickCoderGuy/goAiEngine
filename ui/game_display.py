import pygame


class GameDisplay:
    # Define some colors

    def __init__(self) -> None:
        self.BLACK = (0, 0, 0)
        self.BACKGROUND = (227, 195, 107)
        self.GRAY = (128, 128, 128)
        self.PIXEL_SIZE = 540
        self.NUM_LINES = 18
        self.CELL_SIZE = self.PIXEL_SIZE // self.NUM_LINES
        self.BORDER_SIZE = 3
        self.GRID_LINE_WIDTH = 1

        self.set_up_pygame()

    def set_up_pygame(self):
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Go Board")
        screen = pygame.display.set_mode(
            (self.PIXEL_SIZE, self.PIXEL_SIZE), pygame.RESIZABLE)

        self.update_grid(screen)

        # Run the game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    # Ensure a square board
                    self.PIXEL_SIZE = self.get_valid_screen_size(event.size)
                    self.CELL_SIZE = (self.PIXEL_SIZE //
                                      self.NUM_LINES) - (2 * self.BORDER_SIZE // self.NUM_LINES)
                    screen = pygame.display.set_mode(
                        (self.PIXEL_SIZE, self.PIXEL_SIZE), pygame.RESIZABLE)
                    self.update_grid(screen)

        # Quit Pygame
        pygame.quit()

    def get_valid_screen_size(self, new_screen_size):
        # Round to nearest multiple of NUM_LINES
        new_screen_size = (new_screen_size[0] // self.NUM_LINES * self.NUM_LINES,
                           new_screen_size[1] // self.NUM_LINES * self.NUM_LINES)
        return max(540, min(new_screen_size[0], new_screen_size[1]))

    def update_grid(self, screen):
        screen.fill(self.BACKGROUND)

        for i in range(self.NUM_LINES):
            pygame.draw.line(screen, self.BLACK, (self.CELL_SIZE * i, 0),
                             (self.CELL_SIZE * i, self.PIXEL_SIZE), self.GRID_LINE_WIDTH)
            pygame.draw.line(screen, self.BLACK, (0, self.CELL_SIZE * i),
                             (self.PIXEL_SIZE, self.CELL_SIZE * i), self.GRID_LINE_WIDTH)

        # Star points
        star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9),
                       (15, 9), (3, 15), (9, 15), (15, 15)]
        for point in star_points:
            pygame.draw.circle(
                screen, self.BLACK, (self.CELL_SIZE * point[0], self.CELL_SIZE * point[1]), 6)

        # Draw a rim around the game board
        pygame.draw.rect(
            screen, self.BLACK, (0, 0, self.PIXEL_SIZE, self.PIXEL_SIZE), self.BORDER_SIZE)

        # Update the screen
        pygame.display.flip()
