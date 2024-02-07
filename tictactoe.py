"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """ 
    # Dict to cout the number of X or O
    counter = {X: 0, O: 0}
    for i in range(3):
        for j in range(3):
            state = board[i][j]
            if state != EMPTY:
                if state == X:
                    counter[X] += 1
                elif state == O:
                    counter[O] += 1
                        
    if counter[X] > counter[O]:
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    """
    # if empyt consider it as valid move
    ans = set()
    for i in range(3):
        for j in range(3):
            state = board[i][j]
            if state == EMPTY:
                ans.add((i,j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise ValueError
    if action[0] >= 3 or action[0] < 0:
        raise IndexError
    if action[1] >= 3 or action[1] < 0:
        raise IndexError
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    play = player(board)
    if play == X:
        play = O
    else:
        play = X
    for i in range(3):
        # if they have all similar in row
        if board[i][0] == board[i][1] == board[i][2] == play:
            return play
        # if they have all similar in column
        if board[0][i] == board[1][i] == board[2][i] == play:
            return play
    # These are diagonals
    if board[0][0] == board[1][1] == board[2][2] == play:
        return play
    if board[2][0] == board[1][1] == board[0][2] == play:
        return play
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor == X:
        return 1
    elif victor == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if board is final state return None
    if terminal(board):
        return None
    play = player(board)
    if play == X:
        return maximizing(board)[1]
    else:
        return minimizing(board)[1]


# Funciton to choose max out of min value
def minimizing(board):
    if terminal(board):
        return (utility(board))
    ans = []
    for s in actions(board):
        x = maximizing(result(board, s))
        ans.append((x if x in [1, -1, 0] else x[0], s))
    return min(ans, key=lambda x: x[0])


# Function to choose min out of higest value
def maximizing(board):
    if terminal(board):
        return utility(board)
    ans = []
    for s in actions(board):
        x = minimizing(result(board, s))
        ans.append((x if x in [1, -1, 0] else x[0], s))
    return max(ans, key=lambda x: x[0])        

