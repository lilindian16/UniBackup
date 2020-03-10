"""files for creating person objects"""

class Person:
    """defines a person class, suitable for use in a hospital context    
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
                     
    methods: bmi()
             status()
    """
    
    def __init__(self, name, age, weight, height):
        """Creates a new person object with the specified name, age, weight and
        height
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    def bmi(self):
        """returns the bmi of the person
        """
        return self.weight / (self.height * self.height)
    
    
    def status(self):
        """This returns the persons health status based on their BMI
        """
        
        bmi = Person.bmi(self)
        
        if bmi < 18.50:
            return("Underweight")
        elif bmi >= 18.50 and bmi < 25.0:
            return("Normal")
        elif bmi >= 25.0 and bmi < 30.0:
            return("Overweight")
        else:
            return("Obese")
        
    def __str__(self):
            '''Returns the formatted string represent of the Person object'''
            name = self.name
            age = self.age
            bmi = self.bmi()
            status = self.status()
            template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
            return template.format(name, age, bmi, status)    
