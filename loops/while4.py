# print fibonaci serise
# 0 1 1 2 3 5 8 13
# a b c
#   a b c
#     a b c

n=int(input("enter a number : "))
# n=n-1

a=0
b=1
c=0
print(a,end=" ")  #0
print(b,end=" ")  #1


while c<n:
    c=a+b
    print(c,end=" ") 

    a=b
    b=c

# c=a+b
# print(c)  #2

# a=b
# b=c
# c=a+b
# print(c)  

# a=b
# b=c
# c=a+b
# print(c)