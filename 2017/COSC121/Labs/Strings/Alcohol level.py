"""Program to determine if a person is allowed to drive, given their
   age and blood alcohol level.
"""


def main():
    """This is the main program to run"""
    alcohol_level_string = input("Enter blood alcohol level (mg/100ml): ")
    alcohol_level = float(alcohol_level_string)
    age_string = input("Enter age in years: ")
    age = float(age_string)
    if (age < 20 and alcohol_level > 0) or alcohol_level >= 50:
        print("You're not allowed to drive")
    elif(age >= 20 and (alcohol_level >= 30 and alcohol_level < 50)):
        print("You're legally allowed to drive, but please don't")
    else:
        print("You're allowed to drive")
        
        
#Run the program
main()