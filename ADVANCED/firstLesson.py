# # Ex3
# group22 = {
#     "name": "Python2023",
#     "cont": 35,
#     "male": 22,
#     "female": 13,
#     # "students" = ["Student1", "Student2", "Student3", "Student4", "Student5"],
#     # "ages" = [24, 33, 15, 45, 42],
# }

# group22["name"]

# print (group22.get("name", "error404"))
# print (group22.get("cont"))

group22 = {
    "name": "Python2023",
    "count": 35,
    "male": 22,
    "female": 13,
    "students": ["Student1", "Student2", "Student3", "Student4", "Student5"],
    "ages": [24, 33, 15, 45, 42]
}

group_name = group22["name"]
count = group22["count"]
male = group22["male"]
female = group22["female"]
students = group22["students"]
ages = group22["ages"]

print (group_name)