person = ["manthan",20,56.4,True]
print(person)
print(type(person))

print(person[0])
print(person[1])
print(person[2])
print(person[3])

print(person[0:3])

num = [1,2,3,4,5]
print(num+person)

print(person*3)

# ---------------------------------------------
l1 = [1,2,3,4,5]
print(l1)

#append
l1.append(10)
l1.append(1)
print(l1)

# extend
# l2=["a","b","c"]
# l1.extend(l2)
# print(l1)

# insert
l1.insert(0,"red")
l1.insert(4,"blue")
print(l1)

# remove - item name
l1.remove("blue")
l1.remove(10)
print(l1)

# pop - position
l1.pop(0)
print(l1)

# clear all list item
# l1.clear()
# print(l1)

print(l1.index(4))

print(l1.count(4))

l1.sort()
print(l1)

l1.reverse()
print(l1)

nl = l1.copy()
print(nl)