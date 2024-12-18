from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        

    
    @abstractmethod
    def get_details(self) -> tuple:
        pass


class Student(Person):

    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id

    def get_details(self) -> tuple:
        return (self.name, self.email, self.student_id)

class Professor(Person):

    def __init__(self, name: str, email: str, employee_id: str, office: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.office = office

    def get_details(self) -> tuple:
        return (self.name, self.email, self.employee_id, self.office)

class Course:

    def __init__(self, course_code: str, course_name: str, professor: Professor):
        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor
        self.students = []


    def add_student(self, student: Student) -> int:
        for i in self.students:
            if i.student_id == student.student_id:
                raise ValueError("Student is already enrolled")
        
        self.students.append(student)


    def get_students(self) -> list:
        return [student.get_details() for student in self.students]

    def remove_student(self, student_id: str) -> int:
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return len(self.students)
        
        raise ValueError("Student is not enrolled")

    def get_details(self) -> tuple:
        number_of_students = len(self.students)
        prof = self.professor.get_details()
        return (self.course_code, self.course_name, prof, number_of_students )

student01 = Student("Alice", "alice@uzh.ch", "24-000-001")
student02 = Student("Bob", "bob@uzh.ch", "24-000-002")
student03 = Student("Charlie", "charlie@uzh.ch", "24-000-003")
print(student01.get_details())

professor = Professor("Dr. Dave", "dave@uzh.ch", "01234567", "BIN-0.Z.00")
print(professor.get_details())

course = Course("CS999", "Daveology 101", professor)
print(course.get_details())

course.add_student(student01)
course.add_student(student02)
course.add_student(student03)
print(course.get_details())
print(course.get_students())

course.remove_student("24-000-003")
print(course.get_details())
print(course.get_students())
