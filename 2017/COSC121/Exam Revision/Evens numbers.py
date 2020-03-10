def evens(numbers):
    """docstring"""
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
            
    return result