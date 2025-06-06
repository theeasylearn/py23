colors = {"red","blue","green","yellow","red"}
print(colors)
print(type(colors))

colors.add("black")
print(colors)

colors.remove("red")
print(colors)

# -------------------------------------------
s1 = {1,2,3,4}
s2 = {4,5,6,7}

# uniqe - union
print(s1.union(s2))
print(s2.union(s1))

# intersection - comman
print(s1.intersection(s2))
print(s2.intersection(s1))

# difference 
# s1 - s2
print(s1.difference(s2))

# s2 - s1
print(s2.difference(s1))