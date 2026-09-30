f=open("sample.txt","r")  #file object is returned f contains all the operations

data=f.read
print(data)
print(f.read())

print(type(data))
data=f.readline()  #reads data line by line
print(data)
print(type(data))
#we always have to close the file

f.close()


#append

f=open("sample.txt","a")

f.write("\nNew text being appended\n to the file")

f.close()

#use x
f=open("sample3.txt","x") #file object
f.write("Some random text")

f.close()

#use +
f=open("sample.txt","r+")
f.write("123")
print(f.read())
f.read()
f.close()

with open("sample.txt","r") as f:
    data=f.read()
    print(f.read())
    print(len(data))