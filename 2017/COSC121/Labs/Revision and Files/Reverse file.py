def print_reversed(filename):
    """This function will print out the words in a file with their line order 
    reversed
    """
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines[::-1]:
        print(str(line.strip()))
    
    
    
    
print_reversed("data.txt")