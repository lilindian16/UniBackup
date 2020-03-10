def print_quiz_mark(mark_gained, max_mark=10):
    """This function will print out a ratio and percent of your mark gained
    and your max mark
    """
  
    percent = ((mark_gained / max_mark) * 100)
    words = ("Your quiz mark was ")
    mark_ans = str('{:.1f}'.format(mark_gained))
    max_ans = str('{:.1f}'.format(max_mark))
    ratio_p = str('{:.1f}'.format(percent))
    print((words) + (mark_ans) + "/" + (max_ans) + " (" + (ratio_p) + "%)") 