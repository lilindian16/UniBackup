def bmi(weight, height):
    """"Return the body mass index for weight (kg) and height (m)"""
    return weight / height ** 2

def interact():
    """The user can input their weight and height here"""
    weight = int(input("What is your weight in kgs? "))
    height = int(input("What is your height in centimeters? "))
    print("Your BMI is: ", bmi(weight, height/100))
    
interact()