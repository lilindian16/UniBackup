def print_numbered_lines(filename):
    """This function prints out the lines in a file with the number of the line 
    is on next to it separated with a colon
    """
    infile = open(filename, 'r')
    lines = infile.readlines()
    for number in lines:
        
        
        
print_numbered_lines("marks2.txt")