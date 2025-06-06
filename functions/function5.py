# write function that calculate sum of n numbers

def getsum(*n):
    sum=0
    l1=n[0]
    for i in range(0,len(l1)):
        sum=sum+l1[i]
        
    return sum

l1=[1,2,4,5,5]
# choise = int(input("enter number of input : "))

# for i in range(choise):
#     value = int(input("enter value : "))
#     l1.append(value)
    
# # print(l1)

print(getsum(l1))

# l1=[1,2,3]
# a=0
# for i in range(0,3):
#     a=a+l1[i] 
    
# print(a)

        