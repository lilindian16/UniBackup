
    
def vo2max_cooper(distance):
    """Calculates an estimate of Volume of oxygen max in mL/(kg/min)"""
    return (distance - 504.9) / 44.73


    
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
    
    
      
def print_vo2max_resting(test_pulse, age):
    """Calculates  vo2max using persons resting pulse and age"""
    max_pulse = 208 - 0.7 * age
    resting_pulse = test_pulse
    vo2_max = 15.3 * (max_pulse / resting_pulse)
    proper_vo2_max = format(vo2_max, '.3f')
    print("Estimated Vo2max is " + (proper_vo2_max))
    
    
def main():
    """This main function will be the function for all of the inputs"""
    persons_name = input("Given name? ")
    last_name = input("Family name? ")
    distance_run = input("12min run distance? ")
    persons_gender = input("Gender? ")
    test_pulse = input("Pulse after 3min step test? ")
    print(str(persons_name))
    print(str(last_name))
main()




    

        
        

