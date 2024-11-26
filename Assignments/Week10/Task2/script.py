import os


def get_average_grade(path):
    if not os.path.exists(path):
        return None
    
    counter = 0
    total_grades = 0
    with open(path, "r") as g:
        for line in g:
            line = line.strip()

            if not line or line.startswith('#'):
                continue
            
            parts = line.split(':')
            if len(parts) != 2:
                continue

            try:
                grade = float(parts[1].strip())
                total_grades += grade
                counter += 1
            except ValueError:
                continue
            
            
    
    if counter == 0:
        return 0.0
    return total_grades / counter



print(get_average_grade("task/my_grades.txt"))