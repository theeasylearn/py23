name = "hello world tr"
print(name.upper())

# count = 1
# for i in name:
#     if count%2==0:
#         print(i.upper())
    
#     else :
#         print(i.lower())
        
#     count+=1
    
    
print(name.isdigit())
print(name.isupper())

l1 = ["a","b","c"]
a = "-".join(l1)
print(a)

name = name.replace("l","L",1)
print(name)

l1 = name.split()
print(l1)

import mypackage.mymodule as m

m.add(1,2)
