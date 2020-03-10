def print_squares_to_number(number):
    """docstring"""
    if number < 1:
        print("ERROR: number must be at least 1")
    else:
        for number in range(1, (number + 1)):
            print(("{} * {} = {}").format(number, number, number * number))
    