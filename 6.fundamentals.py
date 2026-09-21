#strings

word1="I love"
word2="python"

sentence=word1+" "+word2

print(sentence)

#indexing
word="Python"
print(word[2])

print(word[2:4])

 sent="fjnvn efnjer  gjkeng qeq "

 print(sent[:len(word)])

 #string formatting

 a=5
 b=10
 sum=a+b#normal formatting
 print("language is{}".format("python"))

 print("Sum of {} & {} is {}".format(a,b,sum))

 index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based formatting

print("{a} values if vars {a} & {b}".format(a=5,b=10))


#f-strings

a=5
b=10
print(f"sum of {a}  & {b} is {a+b}")

