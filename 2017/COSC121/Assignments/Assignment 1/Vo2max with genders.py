def vo2max_step_3min(gender, pulse):
    """This will calculate a persons Vo2max using the 3 minute step test"""
       
    if gender == "m" or gender == "M":
        vo2max = 111.33 - 0.42 * pulse
        return(float(vo2max))
    
    elif gender == "f" or gender == "F":
        vo2max = 65.81 - 0.1847 * pulse
        return(float(vo2max))
        
    else:
        vo2max = -1
        return(str(vo2max))
   
   
   