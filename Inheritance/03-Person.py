class Person:
    def __init__(self,name):
        self.name=name
    
        
class Student(Person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id=id
        
    def display(self):
        print(self.id,self.name)
        

s1= Student('Nahid',101)
s1.display()