def print_first_difference(string1, string2):
    """
    """
    different = False    
    while different == False:
        
        if len(string1) > len(string2):
            for i in range(0, len(string1)):
                if string1[i] == string2[i]:
                    different = False
                else:
                    different = True
                    print("String differs at position {}".format(i))
                    
                           