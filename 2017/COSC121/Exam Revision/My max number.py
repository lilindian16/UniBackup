def my_max(data):
    """docstring"""
    maximum = float('-inf')
    for number in data:
        if number > maximum:
            maximum = number
    return maximum