"""This program will prompt the user to enter a filename that they want to 
   analyse. Then they are prompted to enter a command and this command will be
   executed. The accepted commands are list students and list courses. The 
   resulting data will be printed out. The user will then be prompted to enter 
   antoher command or enter 'q' to quit.
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
    list_students_and_id = []
    for values_in_datasheet in contents[1: ]:
        course_and_student_tuple = process_info_from_file(values_in_datasheet)
        list_students_and_id.append(course_and_student_tuple)
    
    return list_students_and_id
        
        
def process_info_from_file(values_in_datasheet):
    """This function will process the data in the file that is input by the 
    user. It returns a tuple containing the student id and the student's first
    name and last name which is capitalized.
    """    
    result = values_in_datasheet.strip().split(',')
    course_tuple = tuple(result[0:2])
    student_id = int(result[2])
    first_name = result[3]
    last_name = result[4]
    student_tuple = (student_id, first_name, last_name)
    both_tuples_combined = (course_tuple, student_tuple)
    return(both_tuples_combined)


def dict_of_courses_and_id(records):
    """This function takes the list of tuples from the function records_from_file
    returns a dictionary that maps the course code to the course name. The 
    course code is the key
    """
    course_and_id_dict = {}             #This creates an empty dictionary
    for all_tuples in records:
        course_id, course_name = process_course_info(all_tuples)
        course_and_id_dict[course_id] = course_name
    return course_and_id_dict
        
        
def process_course_info(tuples_in_records):
    """This function is a helper function for dict_of_courses_and_id(records). 
    It takes a tuple that contains all the course information and splits it into
    the course id and course name. The answer is then returned.
    """
    course_info_tuple = tuples_in_records[0]   #Extracts all course information
    course_id = course_info_tuple[0]
    course_name = course_info_tuple[1]
    return(course_id, course_name)
    
    
def all_students(records):
    """This takes the list that was created by the function records_from_file.
    It then returns a dictionary that maps the student numbers as integers 
    to the student's name which is a tuple.
    """
    
    student_number_and_name = {}
    for each_tuple in records:
        student_number, student_name = process_all_tuples(each_tuple)
        student_number_and_name[student_number] = student_name
    return(student_number_and_name)


def process_all_tuples(each_tuple):
    """This processs each tuple from the records from records_from_file function.
    It returns the student number (id) and student name.
    """
    all_student_information = each_tuple[1]
    student_number = int(all_student_information[0])
    student_name = (all_student_information[1:3])
    
    return(student_number, student_name)


def course_rolls(records):
    """This takes the list produced from the function records_from_file. Then 
    it returns a dictionary that maps the course codes to sets of sutudent 
    numbers. The key is the course code and the value is the student numbers.
    """
    
    dict_map_course_and_stud_num = {}
    
    for each_tuple in records:
        course_id, student_id = process_each_tuple(each_tuple)
        
        if course_id in dict_map_course_and_stud_num:
            dict_map_course_and_stud_num[course_id].add(student_id)
            
        else:
            dict_map_course_and_stud_num[course_id] = set()
            dict_map_course_and_stud_num[course_id].add(student_id)
    
    return(dict_map_course_and_stud_num)


def process_each_tuple(given_tuple):
    """This processes each tuple from function records_from_file. It returns
    the course_id and student_id number.
    """
    course_info = given_tuple[0]
    student_info = given_tuple[1]
    course_id = course_info[0]
    student_id = student_info[0]
    
    return(course_id, student_id)
    
    
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
    if command_from_user[0] == 'list':
        return True
        

def process_second_command(command_from_user, filename):
    """This is another helper function for process_command. It determines 
    whether the input argument is valid. Then it finally processes the data. If 
    the parameter entered is not valid, it prints out an error message.
    """
    
    command = 'list'
    argument = command_from_user[1]
    
    if argument == 'students' or argument == 'courses':
        process_data(command, argument, filename)
   
    else:
        print("Unknown parameter for list command")          
            
        
def process_data(command, argument, filename):
    """This is the helper function to print the data. It will either call the
    function to print all the students and info or print the courses and info.
    """
    if command == 'list' and argument == 'students':
        print_all_students(filename)
        
    elif command == 'list' and argument == 'courses':
        print_all_courses(filename)
        
        
def print_all_students(filename):
    """This will print a list of all the students and their respective id 
    numbers. This is the main printing function.
    """        
    records = records_from_file(filename)
    students_and_id = all_students(records)
    
    print("All students:")
    
    for id_num, student in sorted(students_and_id.items()):
        first_name = student[0]
        last_name = student[1].upper()        
        print(("  {0}: {1} {2}").format(id_num, first_name, last_name))
    print()
        

def print_all_courses(filename):
    """This will print a list of all the courses and their respective code
    numbers. This is the main printing function.
    """   
    records = records_from_file(filename)
    course_code_and_name = dict_of_courses_and_id(records)
    print("All courses:")
    for course_code, course_name in sorted(course_code_and_name.items()):
        print(("  {}: {}").format(course_code, course_name))
    print()
    
    


def main():
    """Every home deserves one
    """
    file_requested = obtain_filename()
    process_command(file_requested)

        
#Runs the program        
main()