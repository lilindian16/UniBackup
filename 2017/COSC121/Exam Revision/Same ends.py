def same_ends(string_1, string_2):
    """docstring"""
    if string_1 == string_2:
        return False
    elif string_1[0] == string_2[0] and string_1[-1] == string_2[-1]:
        return True
    else:
        return False