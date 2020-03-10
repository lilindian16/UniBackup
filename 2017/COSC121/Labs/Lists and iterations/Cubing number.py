def cubes(data):
    """This will cube each number in a parameter and return the answers in a 
    list
    """
    result = []
    for number in data:
        result.append(number * number * number)
    return result