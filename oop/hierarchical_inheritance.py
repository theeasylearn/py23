class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print(self.name)
        print(self.age)
        
class student(person):
    def __init__(self, name, age,roll):
        super().__init__(name, age)
        self.roll = roll
        
    def student_details(self):
        print(self.roll)
        
class teacher(person):
    def __init__(self, name, age,id,*n):
        super().__init__(name, age)
        self.id=id
        self.n = n
        
    def teacher_details(self):
        print(self.id)
        sum=0
        for i in self.n:
            sum = i+sum
        print(sum)
        
s1 = student("devarsh",17,101)
s1.student_details()
s1.get_details()

t1 = teacher("devarsh",17,202,1,4)
t1.teacher_details()
t1.get_details()