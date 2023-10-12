import pygame
from constants import BLACK,BACKGROUND,GRAY,WIDTH,HEIGHT
from board import Board

class GameDisplay:

  # fps of tha game
  FPS = 60

  def start(self):
    # Run the game loop
    pygame.init()
    pygame.display.set_caption("Go Board")
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    
    running = True
    
    clock = pygame.time.Clock()
    board = Board()
    
    while running:
      clock.tick(self.FPS)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
        if event.type == pygame.MOUSEBUTTONDOWN:
          pass
        
      board.draw_board(WIN)
      pygame.display.update()
      
    # Quit Pygame
    pygame.quit()