def caught_speeding(speed, is_birthday):
    """This will decide whether the persons receives a ticket or not based on 
    their speed and if it is their birthday.
    """
    if (is_birthday) == False:
        if speed <= 60:
            return 0
        elif speed > 60 and speed <= 80:
            return 1
        else:
            return 2
        
    if (is_birthday) == True:
        if speed <= 65:
            return 0
        elif speed >65 and speed <= 85:
            return 1
        else: return 2
        
        
        
    
    
    