class Blork:
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        
        
    def say_hello(self):
        """docstring"""
        
        if self.has_horns:
            print(("HI! MY NAME IS {0}!").format(self.name.upper()))
            
        else:
            print(("Hi! My name is {0}!").format(self.name))
            
    def __str__(self):
        
        if not self.has_horns:
            return(('{} is a {:.2f} m tall blork!').format(self.name, 
                                                           self.height))
        
        else:
            return(('{} is a {:.2f} m tall horned blork!').format(self.name, 
                                                                  self.height))
            
        