friends = {"Nahid", "Nirob", "Arif"}
print(friends)

for i in friends:
    print(i)
    if(i=="Nahid"):
        print("I Love You")
    else:
        print("I Hate you")
friends.add("Pookie")
print(friends)

friends.remove("Nahid")
print(friends)

friends.discard("Pookie")
print(friends)