class employee:
    def __init__(self,name,age,leave=0,salary=0,years=0):
        self.name=name
        self.age=age
        self.leave=leave
        self.salary=salary
        self.years=years
        
    def increment(self):
        if self.years>5 and self.leave<5:
            self.salary+=15000
            
        elif self.years>5:
            self.salary+=10000
            
        elif self.leave<5:
            self.leave+=5000
            
        else:
            print("no increment yet!!!")
    
    def getdetails(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("leave : ",self.leave)
        print("years : ",self.years)
        print("salary : ",self.salary)
        
# e1 = employee("ram patel",19,3,100000)
# e1.getdetails()

e2 = employee("mantan",25,10,200000,10)
e2.getdetails()
e2.increment()
e2.getdetails()

