class Gleep:
    """Attributes
    """
    
    def __init__(self, name, weight):
        """
        """
        
        self.name = name
        self.weight = weight

           
        
   
    def move(self):
        """
        """
        if self.weight >= 100:
            print("Too fat to move")
            
        else:
            print("OK, OK, I'm moving")
    
    
    def eat(self, amount):
        """
        """
        self.weight += amount * 2
        print("Yummy")
        
    
    
    def __str__(self):
        
        return("A {} kg Gleep called {}".format(self.weight, self.name))  