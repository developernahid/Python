names=["Nahid","Nirob","Arif"]
print(names[0])
names.append("Pritom")
print(names)
names.insert(1,"Rahad")
print(names)
names[0]="Pungta"
print(names)
names.remove("Pungta")
print(names)
names.pop(3)
print(names)
names.insert(0,'Nahid')
print(names)

print("Print Using Loop:")
for i in names:
    print(i)
    
for i in range(len(names)):
    print(i,names[i])