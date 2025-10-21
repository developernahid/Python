class Student:
    def set(self, name, age):
        self.name=name
        self.age=age
        
    def show(self):
        print(self.name,self.age)
        
        
s1=Student()
s1.set('Nahid',101)
s1.show()