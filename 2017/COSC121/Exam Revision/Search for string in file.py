def main():
    """
    """
    
    filename = input("Filename? ")
    
    try:
        lines = open_and_read(filename)
    
    except:
        print("File not found")
        
    else:
        
        string = input("Search string? ")
        try_find_string(string, lines)
        

def open_and_read(filename):
    """
    """
    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    
    return lines

def try_find_string(string, lines):
    """
    """
    for line in lines:
        if str(string) in line:
            print(line.strip())


main()