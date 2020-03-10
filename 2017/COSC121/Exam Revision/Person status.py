class Person:
    """docstring"""
    def __init__(self, name, age, weight, height):
        """docstring"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    def bmi(self):
        """docstring"""
        return self.weight / (self.height ** 2)
    
    def status(self):
        """docstring"""
       
        bmi = Person.bmi(self)
        
        if bmi < 18.5:
            return("Underweight")
        elif bmi >= 18.5 and bmi < 25:
            return("Normal")
        elif bmi >= 25 and bmi < 30:
            return("Overweight")
        else:
            return("Obese")
        