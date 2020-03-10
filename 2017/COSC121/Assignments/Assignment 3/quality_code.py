from datetime import date

# get file name
# and keep asking until
# filename is valid
# and file is opened
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



# print summary of line loaded
print('-='*30)
print('Loaded {} ok.'.format(filename))
print('{} line in file'.format(len(line)))
print('-='*30)
print()


# get line to process
num_lines_process = -1
while not num_lines_process > 0 or not num_lines_process <= len(line):
    print('{} line in file'.format(len(line)))
    num_lines_process = int(input('Process first n line, n=? '))
    if num_lines_process < 0 or num_lines_process > len(line):
        print('Invalid n!')
    print()

# trim down to only the first n line
lines = []
for i in range(0, num_lines_process):
    lines.append(line[i])



# process line and make list of max and average values for each day
# the list is sorted by date
summaries = []
for line in lines:
    lines_of_data = line.strip().split(',')
    date_data_taken = lines_of_data[0]
    lines_of_data = lines_of_data[1:]

    year_number = int(date_data_taken[0:4])
    month_number = int(date_data_taken[5:7])
    date_number = int(date_data_taken[8:10])

    date_correct_format = date(year_number, month_number, date_number)

    value_of_day = []
    for value in lines_of_data:
        floating_value = float(value)
        if floating_value >= 0:
            value_of_day.append(floating_value)

    if len(value_of_day) > 0:
        maximum_day = value_of_day[0]
        for value in value_of_day:
            if value > maximum_day:
                maximum_day = value
    else:
        maximum_day = None

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

    summary_tuple = (date_correct_format, maximum_day, days_average)
    summaries.append(summary_tuple)

summaries.sort()

# count number of days over limit
x = 0
for r in summaries:
    if r[2] is not None and r[2] > 50:
        x += 1

# print number of days over limit
print('{} days out of {} exceeded 50 ug/m3'.format(x, len(lines)))


print()


# display maximum graph
print('-='*30)
print('Graph of daily maximums')
print('-='*30)
b = float('-inf')
for r in summaries:
    if r[1] is not None and r[1] > b:
        b = r[1]
for (date_number, maximum_day, _) in summaries:
    if maximum_day is not None:
        stars = '=' * int(maximum_day/b*40)
        template = '{} {:6.2f} {}'
        print(template.format(date_number, maximum_day, stars))
    else:
        print(date_number)
print()


#display average graph
print('-='*30)
print('Graph of daily averages')
print('-='*30)
mxav = float('-inf')
for r in summaries:
    if r[2] is not None and r[2] > mxav:
        mxav = r[2]
for (date_number, _, days_average) in summaries:
    if days_average is not None:
        stars = '=' * int(days_average/mxav*40)
        template = '{} {:6.2f} {}'
        print(template.format(date_number, days_average, stars))
    else:
        print(date_number)
print()
