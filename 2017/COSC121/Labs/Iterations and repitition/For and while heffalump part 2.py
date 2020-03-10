def num_rushes(slope_height, rush_height_gain, back_sliding):
    """This function will work out how many tries it takes for the heffalump
    to climb the tree using for and while loops
    """
    current_height = 0
    rushes = 0
    
    while current_height < slope_height:
        rushes += 1
       
        current_height += rush_height_gain
        rush_height_gain *= 0.95
        
        if current_height >= slope_height:
            break
        current_height -= back_sliding
        back_sliding *= 0.95
            
    return rushes 
    
    
    
