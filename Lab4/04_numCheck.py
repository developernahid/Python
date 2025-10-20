n = int(input("Enter a number: "))
print(n)
if n >100:
    print("Error")
if n >= 80:
    print("A+")
elif n >= 75:
    print("A")
elif n >= 70:
    print("A-")
elif n >= 65:
    print("B+")
elif n >= 60:
    print("B")    
elif n < 40:
    print("F")
elif n < 0:
    print("Negative")
else:
    print("Invalid")
