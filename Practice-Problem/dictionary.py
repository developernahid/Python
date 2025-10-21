student = {
    "name": "Nahid",
    "age": 22,
    "department": "CSE"
}
print(student["name"])
print(student.get("name"))

student["cg"]=3.30
print(student)

student.pop("department")  # Removes by key
print(student)

del student["age"]         # Also removes by key
print(student)

student.clear()            # Removes all items
print(student)
