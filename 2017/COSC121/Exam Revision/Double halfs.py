def double_half(s):
    """docstring"""
    result = ""
    result += str(s[0]) * 2
    for number in list(s):
        if int(number[s]) % 2 == 0:
            result += str(number[s]) * 2
        else:
            result += str(number[s])
    return result
    
    
    