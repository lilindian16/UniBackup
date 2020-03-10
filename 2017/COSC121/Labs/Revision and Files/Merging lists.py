def lossy_merge(list_1, list_2):
    """This will merge two lists while removing the last item from the first and
    removing thre first from the last
    """
    lst1 = list_1
    lst2 = list_2
    lst1.pop(-1)
    lst2.pop(0)
    
    return lst1 + lst2