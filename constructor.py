class Student:
    def __init__(self):
        print("ibject is being constructed")
        
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa
stu1=Student("Rahul",9.0)
stu2=Student("Urvashi",8.4)
stu3=Student("Shardha",9.5)
#jo value pass krege vo is parameter m store hogi

print(stu1.cgpa,stu1.name)
print(stu2.name)
print(stu3.name)


print(f"{stu1.name }has a cgpa ={stu1.get_cgpa}")


