#general
class Employee:
    def __init__(self):
        print("designation=Employee")

#specific
class Teacher(Employee):
    def get_designation(self):
        print("designation=Teacher")

t1=Teacher()
t1.get_designation()


#duck-type
class Teacher():
    def get_designation(self):
        print("designation=Teacher")
class Accountant():
    def get_designation(self):
        print("designation=Accountant")

acc1=Accountant()
acc1.get_designation()
