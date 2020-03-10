def point_string(x, y):
    """Return a string referencing a point at (x, y)"""
    return "Point is at (" + str(x) + ", " + str(y) + ")"

p1_string = point_string(10, 20)
p2_string = point_string(5000, -90)
print(p1_string)
print(p2_string)
print(point_string(0, 10))


