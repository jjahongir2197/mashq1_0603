class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} | {self.age} yosh"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"{self.name} ga {grade} baho qo'shildi.")

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_info(self):
        avg = self.average_grade()
        return f"{self.name} | ID: {self.student_id} | O'rtacha: {avg}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_info(self):
        return f"{self.name} | Fan: {self.subject}"


class University:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print("\nTalabalar:")
        for s in self.students:
            print(s.get_info())

    def show_teachers(self):
        print("\nO'qituvchilar:")
        for t in self.teachers:
            print(t.get_info())


def run_university():
    uni = University()

    s1 = Student("Ali", 18, "S101")
    s2 = Student("Vali", 19, "S102")

    t1 = Teacher("Karim", 40, "Matematika")

    uni.add_student(s1)
    uni.add_student(s2)
    uni.add_teacher(t1)

    s1.add_grade(80)
    s1.add_grade(90)

    s2.add_grade(70)
    s2.add_grade(85)

    uni.show_students()
    uni.show_teachers()


run_university()
