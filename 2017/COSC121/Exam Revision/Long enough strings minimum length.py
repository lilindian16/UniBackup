def long_enough(strings, min_length):
    """docstring"""
    result = []
    for string in strings:
        if len(string) >= min_length:
            result.append(string)
    return result