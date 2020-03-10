from datetime import date

def calc_average(value_of_day):
    """This finds and returns the average reading of PM10 for each day from the
    selected file
    """
    if len(value_of_day) > 0:
        days_total = 0
        for value in value_of_day:
            if value is not None:
                days_total += value
        if len(value_of_day) > 0:
            days_average = days_total / len(value_of_day)
        else:
            days_average = None
    else:
        days_average = None   
    return days_average

def max_day(value_of_day):
    """This determines and returns the maximum PM10 reading for each day from 
    the selected file
    """
    if len(value_of_day) > 0:
        maximum_day = value_of_day[0]
        for value in value_of_day:
            if value > maximum_day:
                maximum_day = value
    else:
        maximum_day = None
    return maximum_day
    
def value_day(lines_of_data):
    """This finds each day that needs to be analysed by the program and returns
    the days in a list
    """
    value_of_day = []
    for value in lines_of_data:
        floating_value = float(value)
        if floating_value >= 0:
            value_of_day.append(floating_value) 
    return value_of_day


def date_proper(date_data_taken):
    """This creates a properly formatted date and returns it
    """
    year_number = int(date_data_taken[0:4])
    month_number = int(date_data_taken[5:7])
    date_number = int(date_data_taken[8:10])
    date_correct_format = date(year_number, month_number, date_number)
    return date_correct_format

def create_summary(lines):
    """This is the function that creates the summary for each day and returns
    it
    """
    summaries = []
    for line in lines:
        lines_of_data = line.strip().split(',')
        date_data_taken = lines_of_data[0]
        lines_of_data = lines_of_data[1:]
        value_of_day = value_day(lines_of_data)
        maximum_day = max_day(value_of_day)
        days_average = calc_average(value_of_day)
        date_correct_format = date_proper(date_data_taken)
        summary_tuple = (date_correct_format, maximum_day, days_average)
        summaries.append(summary_tuple)
    return summaries
    
    
def day_summaries(lines):
    """This is the main function that combines the summaries for each day and
    returns the whole summary
    """    
    summaries = create_summary(lines)
    summaries.sort()
    return summaries
