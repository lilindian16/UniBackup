def zip_lists(list1, list2):
    """docstring"""
    
    result = []
    
    if len(list1) > len(list2):
        for i in range(0, len(list1)):
            if i >= len(list2):
                result.append(list1[i])
            else:
                result.append(list1[i])
                result.append(list2[i])
            
            
        
    else:
        for i in range(0, len(list2)):
            if i >= len(list1):
                result.append(list2[i])
            else:
                result.append(list1[i])
                result.append(list2[i])
   
    return result
   

        
