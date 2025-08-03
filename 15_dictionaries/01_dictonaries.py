
# dictionaries store key value pairs and allow fast lookups like age marks etc


marks = { "Neeraj" : 34,   "jack": 45, "lily": 94}

print (marks, type(marks))

print(marks["lily"])     # command use to get data of particular one
marks["neeraj"] = 3   # change the data directly

# marks.clear()        # clear all the given data from the terminal


marks.pop("lily")   # delete a specific data names 


print(marks)

print(marks.keys())    # tell the names like word all in paragraph

print(marks.values())   #tell the nmeric values in data



