def my_enumerate(items):
    """This function will return a list of items in it enumerated form without
    calling the built in enumerate function
    """
    enumerated = []
    for number in range(len(items)):
        answer = (number, items[number])
        enumerated.append(answer)
    return enumerated
        
        
    
    