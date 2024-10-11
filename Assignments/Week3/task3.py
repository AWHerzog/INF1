#!/usr/bin/env python3

# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.


def get_bmi_category(height, weight):
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.
    if height <= 0 or weight <= 0:
        return "N/A"
    
    BMI = weight / height**2
    if BMI <= 18.5:
        return f"BMI: {BMI:.2f}, Category: Underweight"
    if 18.5 < BMI <= 25:
        return f"BMI: {BMI:.2f}, Category: Normal Weight"
    if 25 < BMI <= 30:
        return f"BMI: {BMI:.2f}, Category: Pre-obesity"
    if 30 < BMI <= 35:
        return f"BMI: {BMI:.2f}, Category: Obesity class I"
    if 35 < BMI <= 40:
        return f"BMI: {BMI:.2f}, Category: Obesity class II"
    if  BMI > 40:
        return f"BMI: {BMI:.2f}, Category: Obesity class III"
    else:
        return f"N/A"
    # Return the BMI values and the correct category after you have calculated the BMI.


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category(1.8, 80))