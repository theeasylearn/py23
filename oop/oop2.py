# calculator

class calculator:
    def __init__(self,a,b):
        # instance variable
        self.a = a
        self.b = b
    
    def add(self):
        print(self.a+self.b)
        
    def sub(self):
        print(self.a-self.b)
        
    def multiply(self):
        print(self.a*self.b)
        
    def div(self):
        print(self.a/self.b)
        
obj1 = calculator(10,20)
obj1.add()
obj1.sub()
obj1.multiply()
obj1.div()

print("-"*100)
obj2 = calculator(5,6)
obj2.sub()