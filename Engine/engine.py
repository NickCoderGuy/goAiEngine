from constants import *

turn_counter = BLACK
pass_counter = 0
board = [[[EMPTY] * LENGTH] * LENGTH]

def newGame():
    global turn_counter, pass_counter, board
    turn_counter = BLACK
    pass_counter = 0
    board = [[[EMPTY] * LENGTH] * LENGTH]

def changeTurn():
    global turn_counter
    if turn_counter == BLACK:
        turn_counter = WHITE
    else:
        turn_counter = BLACK

def endGame():
    return
def passTurn():
    global turn_counter, pass_counter
    changeTurn()
    pass_counter += 1
    if pass_counter == 2:
        endGame()

def resign():
    endGame()

def placePiece(x, y):
    global turn_counter, pass_counter, board
    if board[x][y] == EMPTY:
        board[x][y] = turn_counter
        pass_counter = 0
        changeTurn()
