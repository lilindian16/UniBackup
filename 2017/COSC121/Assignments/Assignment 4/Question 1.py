def records_from_file(filename):
    """This RETURNS a list from a given file. Each item in the list is a tuple
    containing a course tuple and a student tuple. The course tuple contains the 
    course code and name while the student tuple contains the student name and
    family name as well as their ID number as an integer.
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
	