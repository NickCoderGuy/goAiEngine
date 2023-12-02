import sys
sys.path.append("/home/dp4ster/School/428/goAiEngine")
from engine import gogamefacade
import numpy as np

def main():
    facade = gogamefacade.GoGameFacade()

    facade.new_game()
    print(len(facade.state_history))
    facade.make_move(5, 5)
    facade.make_move(5, 5)

    return 0




if __name__ == "__main__":
    main()