friends=("Nahid","Nirob","Arif")
print(friends)
print(friends[1])

temp= list(friends)
temp.append("Pritom")
print(temp)
friends=tuple(temp)
print(friends)

for i in friends:
    print(i)