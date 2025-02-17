def bangladesh_to_german(bangladesh_gpa):
    if bangladesh_gpa >= 3.75:
        return 1.0 
    elif bangladesh_gpa >= 3.50:
        return 1.5 
    elif bangladesh_gpa >= 3.00:
        return 2.0 
    elif bangladesh_gpa >= 2.50:
        return 2.5 
    elif bangladesh_gpa >= 2.00:
        return 3.0 
    else:
        return 4.0 

bangladesh_gpa = float(input("Enter Bangladeshi GPA (0.0 - 4.0): "))
german_grade = bangladesh_to_german(bangladesh_gpa)
print(f"Approximate German grade: {german_grade}")