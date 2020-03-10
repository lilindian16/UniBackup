"""This is the refactored and clean version of the quality code provided. It 
   creates summaries of PM10 values from a selected file and creates graphs
   to illustrate different pieces of information
"""
from datetime import date

MAXIMUMUG = 50



def calc_average(value_of_day):
    """This finds and returns the average reading of PM10 for each day from the
    selected file.
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
    the selected file.
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
    the days in a list.
    """
    value_of_day = []
    for value in lines_of_data:
        floating_value = float(value)
        if floating_value >= 0:
            value_of_day.append(floating_value) 
    return value_of_day


def date_proper(date_data_taken):
    """This creates a properly formatted date and returns it.
    """
    year_number = int(date_data_taken[0:4])
    month_number = int(date_data_taken[5:7])
    date_number = int(date_data_taken[8:10])
    date_correct_format = date(year_number, month_number, date_number)
    return date_correct_format

def create_summary(lines):
    """This is the function that creates the summary for each day and returns
    it.
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
    returns the whole summary.
    """    
    summaries = create_summary(lines)
    summaries.sort()
    return summaries


def try_open_file():
    """This will try to open a filename that the user inputs. If it can't be 
    found, Invalid file name is printed out. Otherwise the file is opened,
    read, closed and returned.
    """
    opened = False
    while not opened:
        filename = input('Filename? ')
        try:
            infile = open(filename)
            opened = True
        except FileNotFoundError:
            print('Invalid file name')
            opened = False
    line = infile.readlines()
    infile.close()
    return (filename, line)

def print_loaded_summary(filename, line):
    """This will print a notice too the user to let them know that their file 
    has been loaded and how many lines it contains.
    """
    print('-='*30)
    print('Loaded {} ok.'.format(filename))
    print('{} lines in file'.format(len(line)))
    print('-='*30)
    print()
    
def get_num_lines_process(line):
    """This function will prompt the user to enter how many lines of the file
    they want to have analysed. The program then will use this and start the 
    analysis from the selected line number.
    """
    num_lines_process = -1
    while num_lines_process <= 0 or not num_lines_process <= len(line):
        print('{} lines in file'.format(len(line)))
        num_lines_process = int(input('Process first n lines, n=? '))
        if num_lines_process < 0 or num_lines_process > len(line):
            print('Invalid n!')
        print()
    lines = []
    for i in range(0, num_lines_process):
        lines.append(line[i])
    return lines

def days_above_limit(summaries, lines):
    """This will print out the amount of days when the ug/m# maximum was 
    breached.
    """
    num_days = 0
    for reading_summary in summaries:
        if reading_summary[2] is not None and reading_summary[2] > MAXIMUMUG:
            num_days += 1
    
    # print number of days over limit
    print('{} days out of {} exceeded {} ug/m3'.format(num_days, len(lines),
                                                       MAXIMUMUG))
    print()
    

def printlines_before_maxgraph():
    """This just prints the banner before the daily maximum graph is drawn.
    """
    print('-='*30)
    print('Graph of daily maximums')
    print('-='*30)    

def print_daily_maximum_graph(summaries):
    """This prints the daily maximum graph.
    """
    base_number = float('-inf')
    for reading_summary in summaries:
        if reading_summary[1] is not None and reading_summary[1] > base_number:
            base_number = reading_summary[1]
    for (date_number, maximum_day, _) in summaries:
        if maximum_day is not None:
            stars = '=' * int(maximum_day/base_number*40)
            template = '{} {:6.2f} {}'
            print(template.format(date_number, maximum_day, stars))
        else:
            print(date_number)
    print()    
    
def printlines_before_avgraph():
    """This just prints the banner before the daily average graph is printed.
    """
    print('-='*30)
    print('Graph of daily averages')
    print('-='*30)    
    
def print_daily_average_graph(summaries):
    """This prints the daily average graph.
    """
    maximum_average = float('-inf')
    for reading_summary in summaries:
        if reading_summary[2] is not None and reading_summary[2] > maximum_average:
            maximum_average = reading_summary[2]
    for (date_number, _, days_average) in summaries:
        if days_average is not None:
            stars = '=' * int(days_average/maximum_average*40)
            template = '{} {:6.2f} {}'
            print(template.format(date_number, days_average, stars))
        else:
            print(date_number)
    print()
    
    
def main():
    """Even my home has one.
    """
    filename, line = try_open_file()
    print_loaded_summary(filename, line)
    lines = get_num_lines_process(line)
    summaries = day_summaries(lines)
    days_above_limit(summaries, lines)
    printlines_before_maxgraph()
    print_daily_maximum_graph(summaries)
    printlines_before_avgraph()
    print_daily_average_graph(summaries)

#Runs the program    
main()