tup=(1,2,3,4,5,6,"abc",3.14)
print(tup)
print(type(tup))
print(len(tup))
print(tup[2])

tupl=(1) #expression

print(type(tupl)) #prints str so put a comma , after the value to print type as tuple
print(tup[:])

#for loop
sum=0
for val in tup:
    sum+=val
print(f"sum of the vals is{sum}")

print(tup.index(2))
print(tup.count(2))
