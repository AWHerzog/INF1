students = {
    'Alice': [85, 90, 78],
    'Bob': [70, 88, 95],
    'Charlie': [100, 68, 80]
}

def student_average_grade(students):
    return {name: round(sum(grade) / len(grade), 2) for name, grade in students.items() }


print(student_average_grade(students))

'''
{
    'Alice': 84.33,
    'Bob': 84.33,
    'Charlie': 82.67
}
'''