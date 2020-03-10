"""Docstring"""

def open_file(input_csv_filename): # compliant with the pylint check and working
    """Opens the file
    """
    datafile = open(input_csv_filename)
    data = datafile.readlines()
    datafile.close() 
    return data

def special_values_from_data(line):
    """docstring
    """
    columns = line.split(',')
    month = int(columns[0])
    num_days = int(columns[1])
    total_rainfall = 0
    return (columns, month, num_days, total_rainfall)
    
    
     

def obtain_results(data):
    """docstring
    """
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns, month, num_days, total_rainfall = special_values_from_data(line)
        for col in columns[2:2 + num_days]:
            total_rainfall += float(col)
        results.append((month, total_rainfall))
    return results            
    
    
def print_stuff(results):
    """This is the main printing function
    """
    print('Rainfall totals for each month')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))
        
        
def print_monthly_totals(file):
    """Every home deserves one
    """
    input_csv_filename = file
    data = open_file(input_csv_filename)
    results = obtain_results(data)
    print_stuff(results)

    
def main():
    """every home deserves one
    """
    print_monthly_totals('rainfalls2011.csv')


main()
