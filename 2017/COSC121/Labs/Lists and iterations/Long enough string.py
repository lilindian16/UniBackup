def long_enough(strings, min_length):
    """This funtion will take a list and remove all the strings that are not 
    longer than the set minimum length
    """
    result = []
    for word in strings:
        if len(word) >= min_length:
            result.append(word)
    return result