def get_column(game, col_num):
    """This function will take a legal game of noughts and returns a 
    three-element list containing the values from the given column number
    """
    result1 = game[0][col_num]
    result2 = game[1][col_num]
    result3 = game[2][col_num]
    column_items = result1, result2, result3
    return list(column_items)