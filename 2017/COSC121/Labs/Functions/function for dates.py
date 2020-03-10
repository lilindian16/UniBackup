def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    date = day_num
    month = month_name
    year = year_num
    
    complete_date = str(date) + " " + str(month) + "," + " " + str(year)
    return complete_date
