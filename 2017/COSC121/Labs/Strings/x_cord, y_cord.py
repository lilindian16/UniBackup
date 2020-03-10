def format_point(x_cord, y_cord):
    """takes two floating point co-ordinates and converts them to one floating
       point
    """
    single_float_x = x_cord
    single_float_y = y_cord
    return("[{0:.1f},{1:.1f}]".format(single_float_x, single_float_y))
    