import pygame
from constants import BLACK,BACKGROUND,GRAY,WIDTH,HEIGHT,SQUARE_SIZE,LINE_WIDTH,NUM_LINES

class Board:
  def __init__(self):
    self.state = [[0 for i in range(NUM_LINES)] for j in range(NUM_LINES)]
    self.turn = 1
    self.selected_piece = None
    self.black_left = 181
    self.white_left = 180

  def draw_board(self,win):

    # Grid lines
    win.fill(BACKGROUND)
    
    # Grid lines
    for i in range(NUM_LINES):
      pygame.draw.line(win, BLACK, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, WIDTH), LINE_WIDTH)
      pygame.draw.line(win, BLACK, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)

    # Star points
    star_points = [(3, 3), (9, 3), (15, 3), (3, 9), (9, 9), (15, 9), (3, 15), (9, 15), (15, 15)]
    for point in star_points:
      pygame.draw.circle(win, BLACK, (SQUARE_SIZE * point[0] + 1, SQUARE_SIZE * point[1] + 1), 6)

    # Draw a rim around the game board
    pygame.draw.rect(win, BLACK, (0, 0, WIDTH + 100, WIDTH + 100), LINE_WIDTH)
