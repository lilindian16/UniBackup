def print_nth_item_divided(data, n, divisor):
    """Prints the nth number of a list (data)"""
    
    try:
        result = ((data[n]) / (divisor))
        
    except IndexError:
        print("Invalid position provided.")
    except TypeError:
        print("Parameters must be numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        
    else:
        print(result)
    
    
    
    
    
    
    

    