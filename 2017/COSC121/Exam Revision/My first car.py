class Car:
    """Attributes"""
    def __init__(self, model, year, speed=0):
        """docstring"""
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        """docstring"""
        self.speed += 5
        
    def brake(self):
        """docstring"""
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5
            
    def honk_horn(self):
        """docstring"""
        print("{} goes 'beep beep'".format(self.model))
        
    def __str__(self):
        """docstring"""
        return (('{0} ' + '(' + '{1}) ' + 'moving at {2} km/h.').format
                (self.model, self.year, self.speed))