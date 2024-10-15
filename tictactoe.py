"""
Tic Tac Toe Player
"""

import math

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
    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # X plays first, so if the counts are the same, it's X's turn; otherwise, it's O's turn.
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy

    i, j = action
    
    # Check if the action is within bounds (0 to 2 for both row and column)
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid action: move out of bounds")
    
    # Check if the selected cell is already occupied
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: cell already occupied")
    
    # Create a deep copy of the board to avoid modifying the original
    new_board = copy.deepcopy(board)
    # Place the current player's mark on the new board
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    # If there are no empty cells, the game is over
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    
    return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = -math.inf
    best_move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_move = action
    return v, best_move


def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = math.inf
    best_move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_move = action
    return v, best_move
