def diagonals(game):
    """This function will return the letters that are contained in each 
    diagonal
    """
    first_left = game[0][0]
    first_right = game[0][2]
    middle = game[1][1]
    bottom_left = game[2][0]
    bottom_right = game[2][2]
    
    
    
    diagonal1 = first_left, middle, bottom_right
    diagonal2 = first_right, middle, bottom_left
    return list(diagonal1), list(diagonal2)
