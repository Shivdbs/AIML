import json
json_str='{"name":"Shivam","age":23,"gender":"male"}'

py_obj1={
    "name":"Shivam",
    "isTeacher":True
}


py_obj=json.loads(json_str)
print(type(py_obj),py_obj)

print(type(py_obj1),py_obj1)


#python dictionary then dump data into JSON Module
data={
    "name":"Shivam",
    "age":23,
    "isTeacher":True
}

with open("data.json","r") as f:
    py_obj3=json.load(f)
    print(type(py_obj3),py_obj3)
# use indent=4 so that every thing not in one line and can sort keys in ascending oder
with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)
