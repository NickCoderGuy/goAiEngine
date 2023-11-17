from engine import gogame, govars
import numpy as np


def new_game():
    state = gogame.init_state(govars.SIZE)
    return state


def pass_turn(state):
    board_shape = state.shape[1:]
    pass_idx = np.prod(board_shape)
    new_state = gogame.next_state(state, pass_idx)
    return new_state


def make_turn(state, x, y):
    position = (x * govars.SIZE) + y
    new_state = gogame.next_state(state, position)
    return new_state
