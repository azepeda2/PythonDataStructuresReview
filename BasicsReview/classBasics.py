class Student:
# how to define a constructor, with required input and default values
    def __init__(self, name, age, grade = "Freshman"):
        self.name = name
        self.age = age
        self.grade = grade

# how to create a toString for an class
    def __repr__(self):
        return f"Student(name='{self.name}' age='{self.age}' grade='{self.grade})"

# inheritance
class Senior(Student):
    def __init__(self, name, age, grade = "Senior"):
        super().__init__(name, age, grade)

    def __repr__(self):
        return f"Senior(name='{self.name}' age='{self.age}' grade='{self.grade})"

if __name__ == '__main__':
    # how to init a list of class students
    students = [
        Student("Bob", 20, "Sophomore"),
        Student("John", 18, "Freshman"),
        Student("Steve", 19, "Junior"),
        Student("Mary", 20, "Junior"),
        Student("Sussy", 19, "Junior"),
    ]

    print(students)

    # how to sort based on student age
    sorted_students = sorted(students, key=lambda student: student.age)

    print(sorted_students)

    # how to sort based on student name (ascending) then grade (ascending)
    sorted_students = sorted(students, key=lambda student: (student.name, student.grade))
    print(sorted_students)

    senior = Senior("Al", 21)
    print(senior)

    print(f"First three students from list: {sorted_students[0]}  {sorted_students[1]}  {sorted_students[2]}")

