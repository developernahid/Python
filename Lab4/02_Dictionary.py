dict={
    "Name": "Nahid",
    "University":"BUBT",
    "SGPA":3.30
}
for x in dict:
    print(dict[x]) #dict dile index
    
for i, j in dict.items():
    print(i, j)
    
person= {"child1":{"Name":"ABC","Age":20,"Dept":"CSE"},
         "child2":{"Name":"DEF","Age":30,"Dept":"EEE"},
         "child3":{"Name":"MNO","Age":24,"Dept":"CSE"},
         "child4":{"Name":"XYZ","Age":20,"Dept":"CS"}    
}
print(person)
print(person["child2"]["Dept"])
for n in person:
    print(person[n])

for x, y in person.items():
    print(x,y)
    for n in y:
        print(n+':',y[n])