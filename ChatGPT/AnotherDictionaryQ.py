students = {
    'Alice': {'Math', 'Science'},
    'Bob': {'History'},
    'Charlie': {'Math', 'History', 'Science'},
    'David': {'Art'}
}

def func(students):
    return {name: course for name, course in students.items() if len(course) > 1}

print(func(students))




'''
{
    'Alice': {'Math', 'Science'},
    'Charlie': {'Math', 'History', 'Science'}
}
'''