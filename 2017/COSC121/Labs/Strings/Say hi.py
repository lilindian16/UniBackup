def say_hi():
    """Asks the user for their name and says Hi followed by their name, 
       correctly capitalized.
    """
    first_name = input("What is your name? ")
    proper_format_name = first_name.title()
    print("Hi " + proper_format_name)
    
