from engine import gogame, govars
import numpy as np
import json


class GoGameFacade():

    def __init__(self) -> None:
        self.state_history = []

    def new_game(self):
        state = gogame.init_state(govars.SIZE)
        self.state_history = []
        self.state_history.append(state)
        return self.__serialize(state)


    def pass_turn(self):
        state = self.__get_current_board()
        board_shape = state.shape[1:]
        pass_idx = np.prod(board_shape)
        new_state = gogame.next_state(state, pass_idx)

        self.state_history.append(state)
        return self.__serialize(new_state)


    def make_move(self, x, y):
        state = self.__get_current_board()
        position = ((x) * govars.SIZE) + y
        new_state = gogame.next_state(state, position)

        self.state_history.append(new_state)
        return self.__serialize(new_state)


    def __combine(self, black_board, white_board):
        full_board = black_board + (white_board * 2)
        return full_board

    def __serialize(self, state):
        json_dict = {}
        json_dict['board'] = self.__combine(state[govars.BLACK], state[govars.WHITE])
        json_dict['turn'] = gogame.turn(state)
        return json_dict

    def __get_current_board(self):
        return self.state_history[-1]