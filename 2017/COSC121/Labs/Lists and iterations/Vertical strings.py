def vertical_strings(string):
    """This will format a string by repeating each letter by the length of the
    word and write it horizontally
    """
    for letter in string:
        print(letter * len(string))
    