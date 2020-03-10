def print_nth_item(data, n):
    """Prints the nth number of a list (data)"""
    
    try:
        print((data[n]))
    except:
        print("Invalid position provided.")
