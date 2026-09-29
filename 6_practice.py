info={
    ("Shivam","Math"),
    ("Rounak","English"),
    ("Divyansh","English"),
    ("Aakansh","Math"),
    ("Chirag","Math"),
    ("Punit","English"),
    ("Kanishk","English"),
}
#set stores unique
unique_courses=set()
for tup in info:
   # print(tup[0]) # 0th index store name
    unique_courses.add(tup[1]) #course
    print(unique_courses)

for name,course in info:
    print(name,course)

#student enrolled in english
for name,course in info:
    if(course=="English"):
        print(name)

#dictionary of student (student,set of courses)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
