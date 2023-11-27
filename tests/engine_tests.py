import sys
sys.path.append("/home/dp4ster/School/428/goAiEngine")
from engine import gogame, govars
import numpy as np
def main():
    board = gogame.init_state(19)

    board = gogame.next_state(board, 20)
    board = gogame.next_state(board, 40)

    print(str(board))

    try:
        board = gogame.next_state(board, 40) #try to make the same move

    except AssertionError:
        print("you made an invalid move!")

    return 0




if __name__ == "__main__":
    main()