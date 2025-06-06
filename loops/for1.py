# for loop
# 1) range - start=0 , stop+1 , size=1
# 2) sequnce - list,tuple,str,dict....

# write a program that print table for n
# 5 x 1 = 5
# ------------------------
# 5 x 2 = 10
# ------------------------
# 5 x 3 = 15
# ------------------------


n = int(input("enter a number : "))

for i in range(1,11,1):
    ans = n*i
    if i==3:
       continue
    
    print(f"{n} x {i} = {ans}")
    print("-"*13)
    
   

# ans = n*count
# print(f"{n} x {count} = {ans}")

# count+=1
# ans = n*count
# print(f"{n} x {count} = {ans}")

# count+=1
# ans = n*count
# print(f"{n} x {count} = {ans}")