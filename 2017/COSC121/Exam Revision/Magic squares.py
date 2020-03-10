def sum_row(square):
    """
    """
    result = []
    
    for row in square:
        count = 0
        for number in row:
            count += number
        result.append(count)
        
    print(result)
    
def sum_col(square):
    """
    """
    result = []
    for column in range(len(square)):
        count = 0
        for row in range(len(square)):
            count = count + square[row][column]
        result.append(count)
    print(result)
            
            
square = [
    [1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]
]

sum_row(square)
sum_col(square)
    
        
        
        