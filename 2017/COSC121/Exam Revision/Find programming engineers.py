def find_programming_engineers(engr101_students, cosc121_students):
    """docstring"""
    doing_both = engr101_students.intersection(cosc121_students)
    return doing_both