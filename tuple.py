# inmutable
# orederd
# any datatype can occur

fruits = ("mango","apple","banana","orange","watermelan")
print(fruits)
print(type(fruits))

print(fruits[2:5])

print(fruits[0::2])

print(fruits + (1,2,3))
# print(fruits*2)

fruits = fruits*4
print(fruits)
print(fruits.count("apple"))
print(fruits.index("apple"))


l1 = list(fruits)
print(l1)

t1 = tuple(l1)
print(t1)