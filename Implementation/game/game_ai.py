import random

def get_computer_move(board):
    # TODO: Implement better AI for game using minimax algorithm
    pass

def get_computer_move_rand(board):
    # very basic for now: random
    valid_columns = [col for col in range(len(board[0])) if board[0][col] == -1]
    if valid_columns:
        return random.choice(valid_columns)
    return -1
    return random.randint(0, 6)
