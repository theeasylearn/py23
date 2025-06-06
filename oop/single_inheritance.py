# creating class 
#parent class 
class Person:
    def __init__(self,name):
        self.name = name 
        print('constructor called...')
    def walk(self):
        print(self.name + " can walk")
    def talk(self):
        print(self.name + " can talk")
    def eat(self):
        print(self.name + " can eat")

#inheritance 
#child class
class Student(Person):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language
    
    def read(self):
        print("I can read " + self.language)
    
    def write(self):
        print("I can write " + self.language)
    
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()

#create child class object       
s1 = Student('Manthan Italiya','Gujarati')
s1.read()
s1.write()
s1.whatICanDo()
s1.walk()
s1.talk()
