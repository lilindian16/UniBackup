def vertical_strings(string):
    """docstring"""
    letters = list(string)
    for letter in letters:
        print(letter * (len(letters)))