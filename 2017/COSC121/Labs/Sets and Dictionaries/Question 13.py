def isbn_dictionary(filename):
    """docstring"""
    
    try:
        infile = open(filename)
    
    except FileNotFoundError:
        print(("The file {} was not found.").format(filename))
        
    else:
        contents = infile.readlines()
        
        
        
        
        
        