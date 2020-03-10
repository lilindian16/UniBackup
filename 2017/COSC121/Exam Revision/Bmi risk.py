def bmi_risk(bmi, age):
    """docstring"""
    if bmi < 22 and age < 45:
        return ("Low")
    elif bmi < 22 and age >= 45:
        return ("Medium")
    elif bmi >= 22 and age < 45:
        return ("Medium")
    else:
        return ("High")
    