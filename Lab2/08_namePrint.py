''' 
name= "My Name
is Nahid
Hasan"
for i in name:
    print(i)

print(name[11:16])
print(name[-11:-1])

if "Nahid" in name:
    print("Nahid name found")
else:
    print("Not found")

print(len(name)) #String length
print(name.upper())
print(name.lower())

b="    Nahid Hasan   "
print(len(b))
print(b.strip())
print(len(b))
print(b.replace("Hasan","Ali"))
print(b.replace('a','z'))
print(b.split(" ")) #Space or any character
print(b)

c='Abdul'
d='Mia'
#c=c+d;
print(c+" "+d)
e=50.5
print(f"{e:.4f}")
 '''

text="Bangladesh \"University\" Of Business & Technology"
print(text)

print("\110\111") #\ er pore 3 ta value mane oita octal value or letter ta print korbe
print("\x48\x49") #Hexadecimal hole x er pore hexa value ta dite hobe
print("Hello\tWorld!!") # Tab
print("Hello\rWorld!!") # Carriage return mane jekhane \r dibo tar por theke print hobe
print("Hello\bWorld!!")
print(text.center(120))