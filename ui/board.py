class Board:
  def __init__(self) -> None:
    self.state = [[0 for i in range(self.NUM_LINES)] for j in range(self.NUM_LINES)]
    self.turn = 1
