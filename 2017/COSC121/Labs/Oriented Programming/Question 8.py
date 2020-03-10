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