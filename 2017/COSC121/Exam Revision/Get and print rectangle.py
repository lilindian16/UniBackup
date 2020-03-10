def get_and_print_rectangle():
    """docstring"""
    width = input("Rectangle width? ")
    height = input("Rectangle height? ")
    area = float(width) * float(height)
    print(("The area of the rectangle is: {}").format(area))
    
get_and_print_rectangle()