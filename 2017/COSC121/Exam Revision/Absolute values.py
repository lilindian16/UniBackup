def abs_values(numbers):
    """docstring"""
    result = []
    for number in numbers:
        if number < 0:
            number = number * -1
        result.append(number)
    return result