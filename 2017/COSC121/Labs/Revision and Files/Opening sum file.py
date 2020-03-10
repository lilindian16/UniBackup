def sum_numbers_in_file(filename):
    """This function will take a file and return a sum of the numbers conatined
    inside it
    """
    
    
    
    
    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    total = 0
    for line in lines:
        number = int(line)
        total = total + number
    return total




        
        
    
    
    
