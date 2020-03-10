def max_num_in_file(filename):
    """This function will return the maximum value of a list inside a file
    """
    infile = open(filename, 'r')
    line = infile.readlines()
    infile.close()
    max_num = -1000000000000000000000000
    for line in line:
        number = int(line)
        if number >= max_num:
            max_num = number
            
    return max_num