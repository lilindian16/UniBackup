"""This program will prompt the user to enter a filename that they want to 
   analyse. Then they are prompted to enter a command and this command will be
   executed
"""


def records_from_file(filename):
    
    """This RETURNS a list from a given file. Inside the list, each line 
    contains a tuple. This contains a tuple with information about the course 
    and a tuple containing information about the student. The course tuple
    contains the course code and its name as a string. The student tuple 
    contains the student name, family name as a string as well as their 
    ID number as an integer. For example, it would return
    (('ABC000', 'DEFGHIJ'), (123456, 'DEF', 'GHI'))
    """
    
    infile = open(filename)
    contents = infile.readlines()
    final_result = []
    for values_in_datasheet in contents[1: ]:
        result = values_in_datasheet.strip().split(',')
        course_tuple = tuple(result[0:2])
        student_id = int(result[2])
        first_name = result[3]
        last_name = result[4]
        student_tuple = (student_id, first_name, last_name)
        both_tuples_combined = (course_tuple, student_tuple)
        final_result.append(both_tuples_combined)
   
    return final_result


def all_courses(records):
    """This function takes the list of tuples from the function records_from_file
    returns a dictionary that maps the course code to the course name. The 
    course code is the key
    """
    
    course_and_id_dict = {}             #This creates an empty dictionary
    for all_tuples in records:
        course_info_tuple = all_tuples[0]       #Extracts all course information
        course_id = course_info_tuple[0]
        course_name = course_info_tuple[1]
        
        course_and_id_dict[course_id] = course_name
        
    return course_and_id_dict


def all_students(records):
    """This takes the list that was created by the function records_from_file.
    It then returns a dictionary that maps the student numbers as integers 
    to the student's name which is a tuple.
    """
    
    student_number_and_name = {}
    for each_tuple in records:
        all_student_information = each_tuple[1]
        student_number = int(all_student_information[0])
        student_name = (all_student_information[1:3])
        
        student_number_and_name[student_number] = student_name
        
    return student_number_and_name


def course_rolls(records):
    """This takes the list produced from the function records_from_file. Then 
    it returns a dictionary that maps the course codes to sets of sutudent 
    numbers. The key is the course code and the value is the student numbers.
    """
    
    dict_map_course_and_stud_num = {}
    
    for each_tuple in records:
        
        course_info = each_tuple[0]
        student_info = each_tuple[1]
        course_id = course_info[0]
        
        
        if course_id in dict_map_course_and_stud_num:
            dict_map_course_and_stud_num[course_id].add(student_info)
            
        else:
            dict_map_course_and_stud_num[course_id] = set()
            dict_map_course_and_stud_num[course_id].add(student_info)
    
    return(dict_map_course_and_stud_num)

    
def obtain_filename():
    """This gets the filename that the user wants to be analysed.
    """
    file_wanted = input("Filename? ")
    return file_wanted

def process_command(filename):
    """This will prompt the user to enter their command and parameter as a 
       string input. Then it will process the command and print the result. 
       If the command or parameter is not valid, a message will be displayed.
    """
    close = False
    while close is False:
        command_from_user = input("Command? (q to quit): ")
        if command_from_user == 'q':
            close = True
            print("Adios")
           
        else:
            command_from_user = command_from_user.split()
            if first_is_valid(command_from_user):
                process_second_command(command_from_user, filename)
            else:
                print("Unknown command")
                
                
def first_is_valid(command_from_user):
    """This is a helper function for process_command. It detemines whether
    the input command is list and if it is it returns true.
    """
    arguement_entered_user = command_from_user[0]
    if arguement_entered_user == 'list':
        return True
    
    elif arguement_entered_user == 'clashes':
        return True
    
    else:
        return False
        

def process_second_command(command_from_user, filename):
    """This is another helper function for process_command. It determines 
    whether the input argument is valid. Then it finally processes the data.
    """
    records = records_from_file(filename)
    courses = all_courses(records)
    command_entered_user = command_from_user[0]
    argument_entered_user = command_from_user[1]
    
    if command_entered_user == 'clashes':
        if argument_entered_user in courses.keys():
            argument = argument_entered_user
            process_data(command_entered_user, argument, filename)     
        else:
            print("Unknown course code")
            
    else:
        process_listing_command(command_from_user, filename)

def process_listing_command(command_from_user, filename):
    """This is a helper function that processes a parameter if it is given
    the command 'list'.
    """
    
    command = 'list'
    argument_entered_user = command_from_user[1]
    
    if argument_entered_user == 'students':
        argument = 'students'
        process_data(command, argument, filename)
            
    elif argument_entered_user == 'courses':
        argument = 'courses'
        process_data(command, argument, filename)
        
    elif argument_entered_user == 'rolls':
        argument = 'rolls'
        process_data(command, argument, filename)
            
    else:
        print("Unknown parameter for list command")     
            
        
def process_data(command, argument, filename):
    """This is the helper function to print the data.
    """
    if command == 'list' and argument == 'students':
        print_all_students(filename)
    elif command == 'list' and argument == 'courses':
        print_all_courses(filename)
    elif command == 'list' and argument == 'rolls':
        print_rolls(filename)
    elif command == 'clashes':
        process_listing_clashes(filename, argument)
        
        
def print_all_students(filename):
    """This will print a list of all the students and their respective id 
    numbers. This is the main printing function.
    """ 
    records = records_from_file(filename)
    students_and_id = all_students(records)
    print("All students:")
    for id_num, student in sorted(students_and_id.items()):
        stud_first_name = student[0]
        stud_last_name = student[1]        
        print(("  {0}: {1} {2}").format(id_num, stud_first_name, 
                                        stud_last_name.upper()))
    print()
        
        
def print_all_courses(filename):
    """This will print a list of all the courses and their respective code
    numbers. This is the main printing function.
    """   
    records = records_from_file(filename)
    course_code_and_name = all_courses(records)
    print("All courses:")
    for course_code, course_name in sorted(course_code_and_name.items()):
        print(("  {}: {}").format(course_code, course_name))
    print()
    
def print_rolls(filename):
    """This processes all the students doing each course. It then prints out
    the course name and all the people who are doing the course.
    """
    records = records_from_file(filename)
    course_code_stud_info = course_rolls(records)
    print("Course rolls:")
    for entry, value in sorted(course_code_stud_info.items()):
        print(entry)
        for item in sorted(value):
            number = item[0]
            name_first = item[1]
            name_last = item[2].upper()
            print(("  {}: {} {}").format(number, name_first, name_last))
        print()
        
def process_listing_clashes(filename, argument):
    """This processes the listing of all the people who have clashes with
    their subjects.
    """
    print(("Clashes with {}:").format(argument))
    process_if_clashing(filename, argument)
    
    
def process_if_clashing(filename, argument):
    """This function finds whether or not students have clashes.
    """
    records = records_from_file(filename)
    course_and_name = course_rolls(records)
    for course_keys in sorted(course_and_name.keys()):
        if argument != course_keys:
            print("In {} and {}".format(argument, course_keys))
            set_being_compared = set(course_and_name[course_keys])
            argument_set = set(course_and_name[argument])
            clashes = set_being_compared.intersection(argument_set)
            print_all_clashes(clashes)
            
            
def print_all_clashes(clashes):
    """This is the main printing function for the clashes command. It will
    print out the people who have clashes.
    """
    if len(clashes) > 0:
        for tup_stud_info in sorted(clashes):
            stud_num, first_name, last_name = process_set_clashes(tup_stud_info)
            print("  {}: {} {}".format(stud_num, first_name, last_name))
        print()
            
            
    else:
        print("  Nobody.")
        print()
            
    
    
def process_set_clashes(tup_stud_info):
    """This processes the tuple inside the sorted clashes set. This then 
    returns the student id number, first name and last name which is capitalized.
    """
    stud_num = tup_stud_info[0]
    first_name = tup_stud_info[1]
    second_name = tup_stud_info[2].upper()
    
    return(stud_num, first_name, second_name)

            
        
        
                
        
    
    
def main():
    """Every home deserves one
    """
    file_requested = obtain_filename()
    process_command(file_requested)
    
    
#Runs the program        
main()