class Employee:
    start_time = "10pm"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time


class AdminStaff(Employee):
    def __init__(self, role):
        super().__init__()  # Properly initialize the parent class
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)  # Passes role to AdminStaff
        self.salary = salary


class Teacher(Employee):
    def __init__(self, subject):
        super().__init__()  # Properly initialize the parent class
        self.subject = subject


# Testing the fixed code
t1 = Teacher("Math")
print(t1.subject, t1.start_time, t1.end_time)

acc1 = Accountant(25_000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)
