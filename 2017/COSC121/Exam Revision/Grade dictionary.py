class Student():
    def __init__(self, student_number, name, grade):
        """Initialise Student object with a given ID number, name and grade, where
           grade is a string, such as 'C', 'B+', 'A+' etc."""
        self.student_number = student_number
        self.name = name
        self.grade = grade

    def __repr__(self):
        """The string representation of self, used by Python when printing lists
           of students. [You don't need to understand this.]
        """
        return "{} {}".format(self.student_number, self.name)
    
    def grade_dictionary(students):
        """
        """
        dictionary = dict()
        for student in students:
            number, name, grade = student.Student()