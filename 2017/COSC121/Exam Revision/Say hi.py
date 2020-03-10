def say_hi():
    """docstring"""
    name = input("What is your name? ")
    print(("Hi {}").format(name.title()))
    
say_hi()