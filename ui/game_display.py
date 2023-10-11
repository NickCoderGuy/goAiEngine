import pygame

class GameDisplay:
  # Define some colors
  BLACK = (0, 0, 0)
  BACKGROUND = (227, 195, 107)
  GRAY = (128, 128, 128)

  # Set the dimensions of the board
  PIXEL_SIZE = 874 # number should be divisible by 19 for even squares
  LINE_WIDTH = 2
  NUM_LINES = 19 # the standard size of a Go board
  CELL_SIZE = PIXEL_SIZE // NUM_LINES

  def __init__(self) -> None:
    self.set_up_pygame()

  def set_up_pygame(self):
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Go Board")
    screen = pygame.display.set_mode((self.PIXEL_SIZE, self.PIXEL_SIZE))
    screen.fill(self.BACKGROUND)

    # Grid lines
    for i in range(self.NUM_LINES):
      pygame.draw.line(screen, self.BLACK, (self.CELL_SIZE * i, 0), (self.CELL_SIZE * i, self.PIXEL_SIZE), self.LINE_WIDTH)
      pygame.draw.line(screen, self.BLACK, (0, self.CELL_SIZE * i), (self.PIXEL_SIZE, self.CELL_SIZE * i), self.LINE_WIDTH)

    # Star points
    star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9), (15, 9), (3, 15), (9, 15), (15, 15)]
    for point in star_points:
      pygame.draw.circle(screen, self.BLACK, (self.CELL_SIZE * point[0] + 1, self.CELL_SIZE * point[1] + 1), 6)

    # Draw a rim around the game board
    pygame.draw.rect(screen, self.BLACK, (0, 0, self.PIXEL_SIZE + 100, self.PIXEL_SIZE + 100), self.LINE_WIDTH)

    # Update the screen
    pygame.display.flip()

  def start(self):
    # Run the game loop
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    # Quit Pygame
    pygame.quit()