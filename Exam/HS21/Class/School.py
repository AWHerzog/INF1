import random
class Student:
    def __init__(self, name):
        self.name = name
        self.year = 1
    
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def learn(self):
        self.year += 1
    
class School:
    national_taught = 0
    def __init__(self, name, years):
        self.name = name
        self.years = years
        self.educated = 0
    
    def educate(self, student):
        if student.get_year() not in self.years:
            raise ValueError
        r = random.randrange(0, 10)
        if r < 9:
            student.learn()
            self.educated += 1
            School.national_taught += 1
    def get_taught(self):
        return self.educated
    

a = Student("Ueli")
print(f"Student Name: {a.get_name()}")
print(f"Initial Year: {a.get_year()}")

# Create a School instance
s1 = School("Mätteliwise", [1, 2, 3, 4, 5, 6])

# Attempt to educate the student multiple times
for i in range(5):
    try:
        s1.educate(a)
        print(f"Attempt {i + 1}: Student Year after education: {a.get_year()}")
    except ValueError:
        print(f"Attempt {i + 1}: Student year {a.get_year()} is not eligible for this school.")

    # Print successful education count for the school and national level
    print(f"School's Educated Count after Attempt {i + 1}: {s1.get_taught()}")
    print(f"National Taught Count after Attempt {i + 1}: {School.national_taught}")

# Final check after all attempts
print("\nFinal Results:")
print(f"Final Year of Student {a.get_name()}: {a.get_year()}")
print(f"Total successful teachings by School {s1.name}: {s1.get_taught()}")
print(f"Total national successful teachings: {School.national_taught}")

