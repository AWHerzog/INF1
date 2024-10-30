
def classify(name, age, child, adult, senior):
    
    if age < child:
        return f"{name} is an infant"
    elif adult > age >= child:
        return f"{name} is a child"
    elif senior > age >= adult:
        return f"{name} is an adult"
    return f"{name} is a senior "


print(classify("Bobby", 4,  5, 18, 65))
print(classify("Bobby", 5,  5, 18, 65))
print(classify("Bobby", 25, 5, 18, 65))
print(classify("Bobby", 70, 5, 18, 65))


"""
Bobby is an infant
Bobby is a child
Bobby is an adult
Bobby is a senior
"""