class Car:
    """Defines the car class.
    Data attributes: model of type str
                     year of type int
                     speed km/h in type int
    """
    
    
    def __init__(self, model, year, speed=0):
        """Car constructor"""
        
        self.model = model
        self.year = year
        self.speed = speed
        
       
       
    def accelerate(self):
        """This adds 5 to the speed data attribute each time
        """
        self.speed += 5
        
        
    def brake(self):
        """This subtracts 5 from the speed but if speed is zero then it stays 
        zero
        """
        
        if self.speed == 0:
            self.speed = 0
        else:
            self.speed -= 5
            
            
    def honk_horn(self):
        """Prints (model) goes beep beep
        """
        
        print(("{0} goes 'beep beep'").format(self.model))
        
        
    def __str__(self):
        
        return (('{0} ' + '(' + '{1}' + '), ' + 'moving at {2} km/h.').format(
            self.model, self.year, self.speed))

        
    
        
    
