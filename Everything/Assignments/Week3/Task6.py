#!/usr/bin/env python3

# Implement the following three functions according to the instructions.

def lump_sum(principal, interest_rate, number_periods):
    lump_sum = sum(principal * interest_rate * number_periods + principal)

def annuity(principal, interest_rate, number_periods):
    pass

# The "payment_type" parameter is a string "annuity" or "lump_sum".
# The function should return one of the functions above depending on the value of the "payment_type" parameter.
# In case of invalid "payment_type", return a string:
# "Invalid payment type. Allowed payment types are: annuity or lump_sum!".
def lump_sum(principal, interest_rate, number_periods):
    
    ia = principal * interest_rate * number_periods
    
    return ia + principal

def annuity(principal, interest_rate, number_periods):
    
    a = (principal * interest_rate) / (1 - (1 + interest_rate)**(-number_periods))
    
    return a * number_periods

# The "payment_type" parameter is a string "annuity" or "lump_sum".
# The function should return one of the functions above depending on the value of the "payment_type" parameter.
# In case of invalid "payment_type", return a string:
# "Invalid payment type. Allowed payment types are: annuity or lump_sum!".
def total_sum_repaid(payment_type):
    
    if payment_type == "annuity":
        return annuity
    elif payment_type == "lump_sum":
        return lump_sum
    else:
        return "Invalid payment type. Allowed payment types are: annuity or lump_sum!"


# The following lines call the functions and print the return value to the console. This way you can check what they do.
print(lump_sum(10000, 0.01, 10)) # 11000.0
print(annuity(10000, 0.01, 10)) # 10558.207655117132

# Before making the following calls, ensure that you implemented total_sum_repaid and it returns values of correct types.
# print(total_sum_repaid("annuity")(10000, 0.01, 10)) # 10558.207655117132
# print(total_sum_repaid("lump_sum")(10000, 0.01, 10)) # 11000.0
# print(total_sum_repaid("invalid_payment_type")) # Invalid payment type. Allowed payment types are: annuity or lump_sum