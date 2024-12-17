def filter_and_sort_students(students, passing_score):
    
    filtered_students = [student for student in students if student["score"] >= passing_score]
    
    sorted_students = sorted(filtered_students, key=lambda x: (-x["score"], x["name"]))
    
    return sorted_students
            
    
# Example usage:
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 65},
    {"name": "Eve", "score": 85},
]

passing_score = 80
result = filter_and_sort_students(students, passing_score)
print(result)

# Expected Output:
# [{'name': 'Charlie', 'score': 90}, {'name': 'Alice', 'score': 85}, {'name': 'Eve', 'score': 85}]
