# find factorial of given number
# 5 -> 1*2*3*4*5 = fact
# 3->6

count = 1 
fact = 1
n = int(input("enter a number : "))
while count<=n:
    fact = fact*count
    count+=1

print("factorial",fact)
# # 1
# fact = fact*count
# print(fact)
# count+=1

# # 1*2
# fact = fact*count
# print(fact)
# count+=1

# # 1*2*3
# fact = fact*count
# print(fact)
# count+=1

# # 1*2*3*4
# fact = fact*count
# print(fact)
# count+=1

