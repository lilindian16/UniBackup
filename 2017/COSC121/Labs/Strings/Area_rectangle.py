def get_and_print_rectangle():
    """ Input a rectangle's width and height then print its area """
    rect_width = input("Rectangle width? ")
    rect_height = input("Rectangle height? ")
    rect_area = float(rect_width) * float(rect_height)
    print("The area of the rectangle is: " + str(rect_area)) 
 
get_and_print_rectangle()
