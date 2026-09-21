# 1. Age check for voting and driving
age = int(input("enter your age : "))
if age >= 18:
    print("you can vote ")
    print("you can drive")
else:
    print("you can not drive")

# 2. Traffic light color check
color = input("enter the color: ")
if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("wrong color for traffic light")

# 3. Age categorization
age = int(input("enter your age: "))
if age < 13:
    print("child")
elif age >= 13 and age < 18:
    print("teenager")
else:
    print("adult")

# 4. First login system (Using elif)
username = input("enter your username: ")
password = input("enter your password: ")
if username == "admin" and password == "pass":
    print("LOGIN successful!")
elif username != "admin":
    print("Wrong Username")
else:
    print("Wrong Password")

# 5. Check multiple of 5
num = int(input("enter the number: "))
if num % 5 == 0:
    print("Multiple of 5")
else:
    print("not multiple of 5")

# 6. Check even or odd
number = int(input("enter the number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

# 7. Second login system (Using nested if-else)
username = input("enter username :")
password = input("enter password :")
if username == "admin" and password == "pass":
    print("successfully logged in")
else:
    if username != "admin":
        print("wrong username")
    else:
        print("wrong password")

# 8. Match-Case (Requires Python 3.10+)
colour = input("enter the colour :")
match colour:
    case "green":
        print("HI")
    case "red":
        print("BYE")
    case _:
        print("Invalid color")

# 9. Loops
# Note: The infinite loop is commented out below so your script doesn't freeze when running.
# while True:
#     print("hello world")

# Finite loop using a counter/iterator variable
count = 1
while count <= 5:
    print(count, "hello world")
    count += 1
print("after loop, count =", count)

i=1 #iterator

while(i<=10):
    print (i)
    i+=1
print("after loop, count =", i)

#print in reverse
i=5
while(i>=1):
    print("hi",i)
    i-=1
#multiply table of any number n
num=int(input("enter the number n: "))
i=1
while(i<=10):
    print(i*num)
    i+=1

#break-used to terminate the loop and continue-to skip current iteration and moves directly to next one

i=1
while(i<=10):
    if(i%6==0):
        break
    print(i)
    i+=1
print("outside loop now")

i=1

while(i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1

print("outside the loop ....")

#print odd/even numbers jump 2 no.
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
i=0
while(i<=10):
    i+=1
    if(i%==0):
        continue
    print(i)

string ="hello"

#in=>membership operator

# for var in string:
#     print(var)
#check if letter 'o' present in the string

string="hello"

if'o' in string:
    print(" 'o' is present in the string")

for i in range(5):
    print(i)

word="artificial intelligence"

#count the number of i's
ans=0
for ch i in word:
    if ch=='i':
        count+=1
print("count of i =",count)


#count vowels
word="artificial"
count =0

for ch in word:
    if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
        count +=1
    print("ans=",count)

for i in range(1,10,2):
    print(i)


sum=0
n=int(input("enter the number: "))
for i in range(1,n+1):
    sum+=i
print("the sum is",sum)

#function defination
def sum(a,b):
    s=a+b
    return s
#function call
ans=sum(3,4)
 print(ans)
 print(sum(,3,4))

#calc average
def calc_avg(a,b,c):
    sum=a+b+c
    return sum/3
print(calc_avg(5,6,3))

#lambda function
sum=lambda a,b: a+b
print(sum(4,5))

avg=lambda a,b: (a+b)/2
print(avg(4,5))

#factorial
def print_fact(n):
    fact = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        fact *= i
    return fact

# Get input from the user and call the function
num = int(input("Enter the number: "))
print("Factorial is:", print_fact(num))
