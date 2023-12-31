
from ui.constants import BLACK,WHITE,GRAY
import pygame   

# the piece class is used to represent the pieces on the board
class Piece:
    PADDING = 0
    BORDER = 2
    
    def __init__(self, row, col, color, cell_size, safe_area):
        self.row = row
        self.col = col
        self.color = color
        self.cell_size = cell_size
        self.SAFE_AREA = safe_area
         
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    # calculate the position of the piece on the board
    def calc_pos(self):
        self.x = (self.cell_size * self.col) + self.SAFE_AREA // 2
        self.y = (self.cell_size * self.row) + self.SAFE_AREA // 2
        
    def setCellSize(self,cell_size):
        self.cell_size = cell_size
        self.calc_pos()
        
    # move the piece to the board by changing the color
    def move(self,turn):
        if(turn % 2 == 0):
            self.color = BLACK
        else:
            self.color = WHITE
        
    # draw the piece on the board
    def draw(self, win):
        radius = self.cell_size//3 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x,self.y),radius + self.BORDER )
        pygame.draw.circle(win, self.color, (self.x,self.y),radius)

    def __repr__(self):
        return str(self.color)
    
    def __str__(self):
        return str(self.color)
        
        