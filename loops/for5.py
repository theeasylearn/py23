# 153 -> 1*3 = 1
        #5*3 = 125
        # 3*3 = 27    => 153
        
# write a program that check number is amstrong or not

n =int(input("enter a number : "))

n=str(n)
length = len(n)

sum=0
for i in n:
    # print(int(i)**length)
    sum = sum+(int(i)**length)

# print(sum)    
# print(n) 
n= int(n)   
if sum == n:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")

