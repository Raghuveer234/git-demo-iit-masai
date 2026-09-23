# student = {
#     "name" : "Rahul",
#     "age" : "20",
#     "course" : "python",
#     "skills" : ["python", "Java", "C++"]
    
# }

# print(student["name"])

# import json


# data = {}

# try:
#     with open('dataa.json', 'r') as file:
#       data = json.load(file)
# except Exception:
#     print('Got an Error')

    # print('Got an Error')
# except: FileNotFoundError
# print('File is not present please check')

# excepts: json.JSONDecodeError
# print('invailid json is present, please fix the json')
#     # print('something went wrong')

# print(data)
# print('tanishq')
    
# dictionary -> stringified json : dumps
# stringified json -> dictionary : loads

# dictionary -> json file : dump
# json file -> dictionary : load

# student = {
#     "name" : "Rahul",
#     "age" : 21,
#     "active" : "true",

# }

# with open("data.json", "w") as file:
        # json.dump(student, file)
       


    
    



# students = {}

# with open("data.json", "r") as file:
#     students = json.load(file)


# print(students)
# print(type(students[0]))

# json_data_in_string = '{"name": "Rahul", "age": "21", "active": "true"}'


# dumps : dictionary -> stringified json

# student = json.loads(json_data_in_string)

# print(student)

# student = {
#     "name" : "Rahul",
#     "age" : "21",
#     "active" : "true",
    
# }

# json_data = json.dumps(student)

# print(type(json_data))
# print(json_data)


import json

# this is bug issue line
print('Tanishq')
try:
    print('Reading file')
except Exception:
    print('Something went wrong while Reading the file')
finally:
    print('finally')   


# finally: block is always executed even when try or except runs
    

age = int(input('Enter your age :'))

if age < 0:
    print('Invailid age')
    

print(age)


# student = {
#     "name" : "Rahul",
#     "age" : "23"
# }

# if not isinstance(student["age"], int):
#     print("age is not an integer, please fix it")

# isinstance(value, type)

# if "age" < 0 or "age" > 120:
    
#     print()

# print(student["class"])
# print(student.get("class"))
 

                                         



    
    

