def evens(numbers):
    """This function will take a list of numbers and filter out the odd ones 
    leaving only even numbers and returning them as a list
    """
    result = []
    for number in numbers:
        if (number % 2) == 0:
            result.append(number)
    return result