#1
name=input("enter the name")
age=input("enter the age")
print(f"Hello {name},you are {age} years old!")

#2
a =int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = a + b
difference = a-b
product = a*b
quotient = float(a/b)

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#3
a=int(input("Enter the first number: "))
b=int(input("enter the second number: "))
c=float(input("Enter the third number: "))

a=float(a)
b=float(b)
average=(a+b+c)/3
print(average)

#4
num = input("Enter the number: ")

num_int = int(num)
print(num_int, type(num_int))

num_float = float(num)
print(num_float, type(num_float))

num_string = str(num)
print(num_string, type(num_string))

#5
x = 10 + 3 * 2 ** 2
print(x)

#6
a=10
b=20

temp=a
a=b
b=temp

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("a =", a)
print("b =", b)
#7
celsius=input("enter the temprature: ")
celsius=float(celsius)

fahreneit=celsius*9/5+32

#8
import math
r = float(input("Enter the radius of the circle: "))

area = 3.14 * r ** 2

print("Area:", area)

#9
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)

#10
num=float(input("Enter a decimal number: "))

integer_part=int(num)

fractional_part=num-integer_part

print("Integer part of the number:", integer_part)
print("Fractional part of the number:", fractional_part)