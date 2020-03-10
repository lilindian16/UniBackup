"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

import math

def read_bound(bound_name): #This is all working
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly. The upper bound is the last number the program tries to see
       if it is a perfect square
       """
    bound = None
    while bound is None:
        prompt = input(bound_name)
        if prompt.isnumeric():
            bound = int(prompt)
            return bound
        else:
            print("You must enter a positive number. ")
        
        

def is_perfect_square(num): #This is all working
    """Return true if and only if num is a perfect square"""
    
    square_root = int(math.sqrt(num))
    number = square_root * square_root
    
    if number == num:
        return True
    
            

def print_squares(lower_bound, upper_bound, squares):
    """Print a given list of all the squares up to a given upper bound"""
    
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()    

    

def main():
    """Every home should have one"""
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)
    
    print_squares(lower_bound, upper_bound, squares)
    
main()
    
 