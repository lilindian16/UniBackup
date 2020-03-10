def num_pieces(board):
    """Return a count of the number of non-empty squares
       in the board.
    """
    count = 0
    for row in board:
        for square in row:
            value = is_filled(row)
            count += value
    return count


def is_filled(square):
    if square != '':
        count = 1
    else:
        count = 0
    return count