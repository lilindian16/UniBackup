def vo2max_rockport(weight, age, gender, time, pulse):
    """This will calculate the vo2max using the above parameters"""
    
    if gender == "m" or gender == "M":
        vo2max = 132.853 - (0.0769 * weight) - (0.3877 * age) \
            + (6.315) - (3.2649 * time) - (0.1565 * pulse)
        return(float(vo2max))
    
    elif gender == "f" or gender == "F":
        vo2max = 132.853 - (0.0769 * weight) - (0.3877 * age) \
            - (3.2649 * time) - (0.1565 * pulse)        
        return(float(vo2max))
        
    else:
        vo2max = (-1)
        return(float(vo2max))    
    