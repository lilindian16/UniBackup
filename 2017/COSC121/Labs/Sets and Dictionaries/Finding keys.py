def find_key(input_dict, value):
    """THIS FUNCTION FINDS THE KEY OF THE VALUE THAT IS ENTERED IN
    """
    
    if value in input_dict.values():
        for key in input_dict:
            if input_dict[key] == value:
                return key
    else:
        return None
    
    
