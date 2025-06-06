# creating class 
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

#will call constructor
p1 = Person('Manthan')
p1.walk()
p1.talk()
p1.eat()