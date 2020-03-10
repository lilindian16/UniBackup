def print_quiz_mark(mark_gained, max_mark=10):
    """docstring"""
    print(("Your quiz mark was {0:.1f}/{1} ({2:.1f}%) ".format(mark_gained, max_mark, 
                                                           mark_gained / 
                                                           max_mark * 100)))