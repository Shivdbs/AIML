# First Part: Class with default class attributes
class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

stu1 = Student()
stu2 = Student()
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)


# Second Part: Class with a constructor that accepts arguments
class StudentWithDetails:
    def __init__(self, name, cgpa):
        print("constructor was called")
        self.name = name
        self.cgpa = cgpa

stu1 = StudentWithDetails("Rahul", 9.0)
stu2 = StudentWithDetails("Urvashi", 8.4)
stu3 = StudentWithDetails("Shardha", 9.2)

print(stu1.name)
print(stu2.name)
print(stu3.name)
