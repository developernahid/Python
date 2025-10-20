dict={
    "Name": "Nahid",
    "University":"BUBT",
    "SGPA":3.30
}
print(dict)
x= dict["University"]
print(x)
print(dict.keys())
print(len(dict))
y=dict.get("Name")
print(y)

dict["Intake"]=51
print(dict)
dict.update({"Name":"Nahid Hasan"})
print(dict)
z=dict.items()
print(z)
dict.pop("SGPA")
print(dict)
dict.popitem() #Last one delete
print(dict)

del dict["University"]
print(dict)
del dict
print(dict)