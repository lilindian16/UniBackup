def work():
    """docstring"""
    full_name = input("Your first and last names? ")
    if ' ' in full_name:
        first_name, last_name = full_name.split()
        print("Name: {}, {}".format(last_name.upper(), first_name.capitalize()))
        
    else:
        print("ERROR: Only one name found")
work()