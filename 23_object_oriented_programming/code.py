class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("aca", (90, 95, 98, 78))
print(student.name)
print(student.average())
