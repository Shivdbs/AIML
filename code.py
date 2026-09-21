print("Hello world")
name="shivam"
age=35
PI=3.14

print("my age is: ",age-5) #prints 35-5
print (type(name))

num=2
isPrime=True
print (type(isPrime))
total_price=100

#arithmetic
a=10
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#relational
a=10
b=5
print(a==b)
print(a>=b)

#relational
var=False
print(not(5>8)) #true

print((5>4)and(6<3)) #false
print((4==2)or(5==5)) #true

x=3
x+=5
print(x)   #8n


#type cast/conversion
a=10
b=5
print(type(a/5)) #implicit python auto convert

ans=5+10.0
print(type(ans))

ans1=int(5+10.0)
print(type(ans1)) #casting

ans2=5+10.0
print(type(ans2))#conversion

val1=int("123")
print(type(val1))

val2=bool(0)
print(val2,type(val2))

#user input
a=input("enter value of a:")
print(a)

#sum of two numbers

a=input("enter a: ")
b=input("enter b: ")

sum=a+b
print(sum)


a=int(input("enter a: "))
b=int(input("enter b: "))
sum=a+b
print(sum)

#print average of two numbers
a=int(input("enter first number: "))
b=int(input("enter second number: "))
average=(a+b)/2
print("the average is: ",average)

