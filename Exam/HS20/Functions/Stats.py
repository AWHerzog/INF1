
def stats(students):
    
    res = {}
    for key, value in students.items():
        total_grade = sum(grade for _, grade in value)
        num_subjects = len(value)
        res[key] = round(total_grade / num_subjects, 2)
    
    subject_grades = {}
    subject_counts = {}
    for k, v in students.items():
        for subject, grade in v:
            if subject not in subject_grades:
                subject_grades[subject] = 0
                subject_counts[subject] = 0
            subject_grades[subject] += grade
            subject_counts[subject] += 1
    
    res2 = {subject: round(subject_grades[subject] / subject_counts[subject], 2) for subject in subject_grades}
    
    return res, res2
    
raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)
