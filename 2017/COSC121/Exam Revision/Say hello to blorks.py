class Blork:
    """docstring"""
    def __init__(self, name, height, has_horns=False):
        """docstring"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        
    def say_hello(self):
        """docstring"""
        if self.has_horns:
            print("HI MY NAME IS {}!".format(self.name.upper()))
        else:
            print("Hi my name is {}!".format(self.name.title()))
            
    def __str__(self):
        """docstring"""
        if self.has_horns:
            return("{} is a {:.2f} m tall horned blork!".format(self.name, 
                                                               self.height))
        else:
            return("{} is a {:.2f} m tall blork!".format(self.name, self.height))
        