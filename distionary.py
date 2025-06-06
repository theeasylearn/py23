# dict = {key:value , kay:value....}

student = {"name":"manthan","age":20,"mobile":1234567890,"gender":True}

print(student)
print(type(student))

#accessing single value of dict
print(student["name"])
print(student["age"])
print(student["mobile"])
print(student["gender"])

# change value of key
student["age"] = 25
print(student)

# delete key-value
del student["gender"]
print(student)

# ------------------------------------------------------
# clear all items
# student.clear()
# print(student)

# copy dict
d1 = student.copy()
print(d1)

# return keys from dict
print(student.keys())

# return values from dict
print(student.values())

# return key-values
print(student.items())

# delete key - value
student.pop("mobile")
print(student)

# delete last key-value
student.popitem()
# student.popitem()
print(student)

# add new key - value
student.update({"email":"abc@gmail.com"})
print(student)

# update existing key's value
student.update({"email":"xyz@gmail.com"})
print(student)

# -------------------------------------------------------
product = {
           "name":"Iphone16",
           "colors":[
                    "white","black","silver",
                    ("special","golden")
                    ],
           "d2":{"size":"32inch","weight":"200gm"}
          }

print(product)
print(product["colors"][3][1])
