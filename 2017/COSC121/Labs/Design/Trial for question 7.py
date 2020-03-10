def get_filename(): #Works
    """Return the name of the student data file to be processed"""
    return "data.csv"

def read_data(filename): #Works
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    
    try:
        result = []
        in_file = open(filename, 'r')
        data = in_file.readlines()
        result = []
        for i in data:
            tmp = i.split(",")
            result.append((str(tmp[0]), float(tmp[1])))
        return(result)
    
    except IOError:
        return None
        
        
    
def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple
       containing statistics extracted from the list. The tuple elements are
       minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    # ****** YOUR CODE HERE ******
    data_obtained = student_data
    #Obtain the maximum score
    num_for_max = (0, 0)
    num_for_min = (0, 100)
  
    for item in data_obtained:
        if item[1] >= num_for_max[1]:
            num_for_max = item    
        if item[1] <= num_for_min[1]:
            num_for_min = item
            
    maximum_mark = num_for_max[1]
    minimum_mark = (num_for_min[1])
    
    #Find the top students 
    top = []
    for item in data_obtained:
        if item[1] == num_for_max[1]:
            top += [item[0]]
    
    top_students = top #NEEDS TO BE SORTED ALPHABETICALLY!!!!!
    
    #Calculate the average mark
    sum_nums = 0
    for item in data_obtained:
        sum_nums += item[1]
        average_mark = sum_nums / len(data_obtained)
        
    top_students.sort()       
    return(minimum_mark, maximum_mark, average_mark, top_students)
 
def print_results(stats):
    """Print the statistics given. The parameters 'stats' is a
       tuple of the form returned by the 'statistics' function
       above.
    """
    file_name = get_filename()
    data = read_data(file_name)
    stats = statistics(data)
    (minimum, maximum, average, top_students) = stats
    print("Minimum: {:.1f}".format(minimum))
    print("Maximum: {:.1f}".format(maximum))
    print("Average: {:.1f}".format(average))

    if len(top_students) == 1:
        print("Top student: {}".format(top_students[0]))
    else:
        print("Top-equal students:\n  {}".format(", ".join(top_students)))
 
def main():
    """ The main function (yeah, this comment is noise)"""
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)



main()

        
