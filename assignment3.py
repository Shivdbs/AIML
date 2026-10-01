#1 .check palindrome from a input string manual reverse without [::-1]

text=input("Enter the string: ")
reversed_text=""

for ch in text:
    reversed_text=ch+reversed_text
if text==reversed_text:
    print(text," is a Palindrome")
else:
    print(text," is not a Palindrome")

#2. Average of integers in a list

numbers=[]

n=int(input("how many numbers:"))

for i in range(n):
    value=int (input("Enter number: "))
    numbers.append(value)
print(numbers)

   #to find avg
average=sum(numbers)/n
print("your average is: ",average)


#3. create 2 list take inl\puts merge then sort them then print

l1=[]
n1=int(input("enter the length of l1"))
for i in range(n1):
    l1.append(int(input("enter the number:")))
l2=[]
n2=int(input("enter the length of l2"))
for i in range(n2):
    l2.append(int(input("enter the number:")))

merged=l1+l2
print("merged list=",merged)
merged.sort()
print("sorted list=",merged)


#4. take a tuple then make 2 out of it containing odds and evens
numbers=(1,2,4,45,6,32,65,33,901,19434,5234)
odd_num=()
even_num=()
for i in numbers:
    if i%2==0:
        even_num+=(i,)
    else:
        odd_num+=(i,)
print(odd_num)
print(even_num)

#5. add students marks to the dictionary

students = {}

while True:
    choice = input("Enter A, B, C, D or Q to quit: ")

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.update({name: marks})

    elif choice == "B":
        name = input("Enter student name: ")

        if students.get(name) != None:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found")

    elif choice == "C":
        name = input("Enter student name: ")

        if students.get(name) != None:
            print("Marks:", students.get(name))
        else:
            print("Student not found")

    elif choice == "D":
        for name, marks in students.items():
            print(name, marks)

    elif choice == "Q":
        break


#6. Dictionary mapping each word to its length
words=["apple","banana","kiwi","mango"]
word_lengths={}
for word in words:
    word_lengths[word]=len(word)

print(word_lengths)

#7.  Count spaces in a string
text=input("Enter your string: ")

count=0
for ch in text:
    if ch==" ":
        count+=1
print("Number of spaces:",count)

#8 check if 2 lists have no common element
#use a set for both lists and find intersection
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

set1=set(list1)
set2=set(list2)

common=set1&set2

if len(common)>0:
    print(common)
else:
    print("No common element")

#9. print the duplicates form a list
numbers=[1,2,3,4,4,5,3,7,7,2,2,10]

seen=set()
duplicates=set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicates: ",duplicates)

#10 Print unique characters and their count
text=input("enter the text: ")
uniq=set(text)

print("Uniques: ",uniq)
print("number of unique characters: ",len(uniq))