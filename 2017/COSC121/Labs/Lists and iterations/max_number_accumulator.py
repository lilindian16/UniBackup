def my_max(data):
    """This will compute the maximum value of a data set using the accumulator
    method
    """
    max_number = data[0]
    for num in data:
        if num > max_number:
            max_number = num
    return max_number
