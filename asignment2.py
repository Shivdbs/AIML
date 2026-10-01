#1
from unittest.mock import inplace

salary = int(input("Enter your salary: "))

if salary < 30000:
    print("Tax rate: 5%")

elif 30000 <= salary <= 70000:
    print("Tax rate: 15%")

else:
    print("Tax rate: 25%")

#2
a=int(input())
b=int(input())

def print_value(a,b):
    for i in range(a,b+1): #inclusive
        if i%2==0:
            print(i)

#3 print digits n%10
def print_digit(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

#4
def count_digits(n):
    count =0
    while n>0:
        n=n//10
        count+=1
    return count


#5
# digit = n % 10    # extract last digit
# n = n // 10       # remove last digit
def sum_digits(n):
    total=0
    while n>0:
        digit=n%10
        total=total+digit
        n=n//10

    return total
#6
for i in range(1,101):
    if i%3 and i%5==0:
        print(i)
#7
while True:
    value = input("Enter a number or Quit: ")

    if value == "Quit":
        break

    n = int(value)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

#8
def calculator(a, b, operation):
    if operation == "+":
        print(a + b)

    elif operation == "-":
        print(a-b)

    elif operation == "*":
        print(a*b)

    elif operation == "/":
        print(a/b)

#9

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return False
#10 Number guessing game

secret=7
guess=int(input("Guess the Number: "))
if guess > secret:
    print("Too high")

elif guess <secret:
    print("Too low")

else:
    print("Correct")