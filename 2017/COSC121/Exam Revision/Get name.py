def get_name(name_dict, id_num):
    """docstring"""
    if id_num in name_dict:
        name = name_dict[id_num]
        return name
    else:
        return None