def print_names2(people):
    """This function prints out the names of people in a list using the while
    function
    """
    i = 0
    while i < len(people):
        print(" ".join(people[i]))
        i += 1