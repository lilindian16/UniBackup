def is_it_odd_or_even(chosen_number):
    """This will see if the users number is even or odd"""
    users_number = chosen_number
    if chosen_number % 2 == 0:
        print("Your number is even!!!")
        
    elif chosen_number % 2 != 0:
        print("Lo siento pero your number is odd!!!!")
            
        
def users_chosen_number():
    """This will generate the users chosen number"""
    number_chosen = int(input("Please select a number: ")
    return (number_chosen)

users_chosen_number()
