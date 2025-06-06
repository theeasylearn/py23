from random import *

print(random())  #0.0 - 1.0

# give random float value between range
print(uniform(2 , 10))  

# give random int value between range
print(randint(1,100))

# give random int value between range with gap
print(randrange(1,100,10))

l1 = ['a','b','c','d']
print(choice(l1)) 

t1 = ('red','blue','green','yellow','black')
print(choice(t1))

l1=[1,2,3,4,5,6,7,8,9,0]
print(choices(l1,k=2))

shuffle(l1)
shuffle(l1)

print(l1)

print(sample(l1,5))