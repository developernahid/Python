class Person:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(self.name)    
        
class Student(Person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id=id
        
    def display(self):
        print(self.id)
        

s1= Student('Nahid',101)
s1.show()
s1.display()