def character_set_counts(string_1, string_2, string_3):
    """docstring"""
    string_1 = set(string_1)
    string_2 = set(string_2)
    string_3 = set(string_3)
    
    one_two = string_1.intersection(string_2)
    one_two_three = one_two - string_3
    return len(one_two_three)