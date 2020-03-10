def row_sums(square):
    """This function will return the sum of each row in the magic square
    """ 
    result = []
    
    for rows in square:
        row = 0
        for numbers in rows:
            row = row + numbers
        result.append(row)
    return result
        
