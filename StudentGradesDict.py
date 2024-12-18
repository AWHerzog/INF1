def student_grades(data):
    return {name: {subject: grade for n, subject, grade in data if n == name} for name in {n for n, _, _ in data}}

print(student_grades([("Alice", "Math", 90), ("Alice", "Science", 85), ("Bob", "Math", 75)]))
# Expected:
# {
#     'Alice': {'Math': 90, 'Science': 85},
#     'Bob': {'Math': 75}
# }
