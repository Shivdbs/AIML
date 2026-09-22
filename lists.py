mark1=99
mark2=89
mark3=100
mark4=65
mark5=92

marks=[99,89,100,65,92]

print(marks)
print(len(marks))
 #slicing

mark=[99,89,100,65,92,"abc",100.99]

print(mark[:5])

print(mark[5:len(mark)])

print(marks[-5:-2])
mark.append(101)
mark.insert(2,10)

mark.sort()
print(mark)

mark.sort(reverse=True)

print(mark)

mark.reverse()


nums=[1,2,3,4,5,6]
for val in nums:
    print(val)
# also called linear search
x=10
idx=0

for val in nums:
    if(val==x):
        print(f"{x} found in index={idx}")
        break
    idx+=1