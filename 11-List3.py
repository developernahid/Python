list= ['Nahid','Nirub','Rahud']
for x in list:
    print(x)
    
for x in range(len(list)):
    print(list[x])
    

i=0;
while i<len(list):
    print(list[i])
    i=i+1
    #shortcut
    [print(x) for x in list]
    
    #list comprehension
    num=[1,3,5,7,9]
    comp=[x*2 for x in num]
    print(comp)