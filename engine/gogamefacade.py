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
        return self.serialize(state)


    def pass_turn(self):
        state = self.get_current_board()
        board_shape = state.shape[1:]
        pass_idx = np.prod(board_shape)
        new_state = gogame.next_state(state, pass_idx)

        self.state_history.append(state)
        return self.serialize(new_state)


    def make_move(self, x, y):
        state = self.get_current_board()
        position = ((x) * govars.SIZE) + y
        new_state = gogame.next_state(state, position)

        self.state_history.append(state)
        return self.serialize(new_state)


    def combine(self, black_board, white_board):
        full_board = black_board + (white_board * 2)
        return full_board

    def serialize(self, state):
        json_dict = {}
        json_dict['board'] = self.combine(state[govars.BLACK], state[govars.WHITE])
        json_dict['turn'] = gogame.turn(state)

    def get_current_board(self):
        return self.state_history[-1]