class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def show(self):
        print(f"Name: {self.name} ID: {self.id}")
        
        
s1= Student("Nahid",143)
s1.show()