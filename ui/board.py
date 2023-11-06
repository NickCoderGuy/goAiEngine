from ui.constants import BLACK,NUM_LINES,ROWS,COLS,GRAY,CELL_SIZE
from ui.piece import Piece

class Board:
  def __init__(self,cell_size,safe_area) -> None:
    #black starts first
    self.turn = 0
    # state of the board
    self.board = []
    
    self.selected_piece = None
    self.white_left = 180
    self.black_left = 181
    
    self.black_captures = 0
    self.white_captures = 0
    
    self.cell_size = cell_size 
    self.SAFE_AREA = safe_area
    self.create_board()
    
  def get_turn(self):
    return self.turn
  
  def get_pieces_left(self):
    return self.white_left,self.black_left
  
  def get_captures(self):
    return self.white_captures,self.black_captures
  
  def move(self,piece): 
    if piece != None and piece.color == GRAY:
      # since the piece is gray, it is not placed yet
      piece.move(self.turn)
      # if it is white's turn, then the piece is white and vice versa
      if(self.turn % 2 == 0):
        self.black_left -= 1
      else:
        self.white_left -= 1  
      self.turn += 1
    
  def get_piece(self,row,col):
    if(row >= ROWS or col >= COLS or row < 0 or col < 0):
      return None
    piece = self.board[row][col]
    return piece
  
  # create the board by adding pieces to the board that are gray
  def create_board(self):
    for row in range(ROWS):
      self.board.append([])
      for col in range(COLS):
          self.board[row].append(Piece(row,col,GRAY,self.cell_size, self.SAFE_AREA))   
            
  # draw the board
  def draw(self,win,cell_size):
    self.cell_size = cell_size
    for row in range(ROWS):
      for col in range(COLS):
        piece = self.board[row][col]
        piece.setCellSize(self.cell_size)
        if piece != 0:
          piece.draw(win)

  def to_string(self):
    for row in range(ROWS):
      for col in range(COLS):
        piece = self.board[row][col]
        print(piece,end=" ")
      print()
    print()