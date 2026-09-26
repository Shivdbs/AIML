info={
    "name":"shivam",
    "cgpa":10,
    "subjects":["math","science"]
}

print(type(info))
print(info["name"])
print(info["cgpa"])
print(info["subjects"])




#dictionary methods
print(info.keys)
dict_keys=info.keys()
#type cast
dict_keys_list=list(info.keys())
print((type(dict_keys_list)))

dict_vals=list(info.values())

print(dict_vals)

#dictionary items
dict_items=list(info.items())
print(dict_items)

#dictionary get function
print(info.get("cgpa"))

print("end of code")

#update method

info.update({
    "city":"Delhi"
})

print(info)