from constants import BLACK,NUM_LINES,ROWS,COLS,GRAY,CELL_SIZE
from piece import Piece

class Board:
  def __init__(self,cell_size) -> None:
    self.state = [[0 for i in range(NUM_LINES)] for j in range(NUM_LINES)]
    #black starts first
    self.turn = 0
    self.board = []
    self.selected_piece = None
    self.white_left = 180
    self.black_left = 181
    self.cell_size = cell_size 
    self.create_board()
    
  def get_turn(self):
    return self.turn
  
  def get_pieces_left(self):
    return self.white_left,self.black_left
  
  def move(self,piece):  
    if piece.color == GRAY:
      # since the piece is gray, it is not placed yet
      piece.move(self.turn)
      # if it is white's turn, then the piece is white and vice versa
      if(self.turn % 2 == 0):
        self.black_left -= 1
      else:
        self.white_left -= 1  
      self.turn += 1
    
  def get_piece(self,row,col):
    return self.board[row][col]
  
  # create the board by adding pieces to the board that are gray
  def create_board(self):
    for row in range(ROWS):
      self.board.append([])
      for col in range(COLS):
          self.board[row].append(Piece(row,col,GRAY,self.cell_size))   
          
  def re_recreate_board(self,cell_size):
    self.cell_size = cell_size
    self.board = []
    for row in range(ROWS):
      for col in range(COLS):
          piece = self.get_piece(row,col)
          self.board[row][col] = Piece(row,col,piece.color,self.cell_size)
          
  # draw the board
  def draw(self,win,cell_size):
    self.cell_size = cell_size
    for row in range(ROWS):
      for col in range(COLS):
        piece = self.board[row][col]
        if piece != 0:
          piece.draw(win)     