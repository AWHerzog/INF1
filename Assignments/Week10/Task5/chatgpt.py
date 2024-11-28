def organize_student_grades(students):
    return {
        subject: {
            name: grade 
            for name, sub, grade in students
            if sub == subject
        } for subject in {sub for _, sub, _ in students}
    }

# Example usage:
students = [
    ('Alice', 'Math', 85),
    ('Bob', 'Science', 90),
    ('Charlie', 'Math', 78),
    ('David', 'English', 88),
    ('Eve', 'Science', 92)
]
print(organize_student_grades(students))
