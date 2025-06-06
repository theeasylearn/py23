# check a string or number is palimbrom or not

# 1010 -> 0101
# 111 -> 111

# mam -> mam

# 1) input
# 2) reverse
# 3) check condition

data = input("enter a string : ")
# hello
# print(data[::-1])

# reverse_data = data[::-1]

if data == data[::-1] : 
    print(f"{data} is palimbrom")
    
else:
    print(f"{data} is not palimbrom")


l1 = [1,2,3,4,5]
print(l1)

print(l1[::-1])