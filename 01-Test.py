print("I love Python Programming!!!")
#This is single line comment

id=143
print("My Student id:",id)

temp=25.4
print("Today's tempareture is: ",temp)

firstName='Nahid' # '' or "" both are used to declare string
lastName="Hasan"
print("My name is: ",firstName,lastName)
print(f"My name's : {firstName} {lastName}")

#Declare multiple variable in one line
a,b,c=10,20,30
print(f"The value of a,b & c :{a},{b} & {c}")
print("The value of a,b & c :",a,b,c)

#Packed Unpacked 
dept=["CSE","BBA","EEE","LAW"]
print(dept)
a,b,c,d=dept
print("BUBT all departments: ",a,b,c,d)
#Or we can print like this using f string
print(f"BUBT all departments: {a}, {b}, {c}, {d}")

#Multiple variable but same value
x=y=z="I love you"
print(x)
print(y)
print(z)


#Global & Local Variable
n="Pyhton" #Global varibale
def myFunction():
    n="Java" #Local Variable
    print("I love ",n) #Call local variable
myFunction()

'''Function declare in Python
>>Use def keyword before function name, then set function name then :
>>Then call the function 
'''

def myFunction2():
    print("I love ",n) #Call global variable
myFunction2()

#Data Type in Python
#Basic int,float,double,string,character ache
v=4j
print(v,type(v))

v=["Nahid",'Rahad',"Nirob",'Arif',"Tasin"]
print(v, type(v)) #List mane [] bracket


v=("Nahid",'Rahad',"Nirob",'Arif',"Tasin")
print(v, type(v)) #Tuple () bracket hoile

v=10;
print(range(v)) #Range- 0 to value porjonto

v={"Nahid",'Rahad',"Nirob",'Arif',"Tasin"}
print(v, type(v)) #Set mane {} bracket

v={"name":"Nahid","age":50}
print(v, type(v)) #Dictionary like ekta variable: tar value

v=({"Nahid",'Rahad',"Nirob",'Arif',"Tasin"})
print(v, type(v)) #frozenset () er moddhe {}

v=tuple(("A","B","C"))
print(v)