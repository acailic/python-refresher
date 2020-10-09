from typing import List, Optional


class Student:
    def __init__(self, name: str,
                 grades: Optional[List[int]] = None):  # bad idea - to put [] as default param, its mutable
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("bob")
aca = Student("aca")
bob.take_exam(89)
print(bob.grades)
print(aca.grades)
