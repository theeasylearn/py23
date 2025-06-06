# write a program that print a number and odd or even
# 5
# odd = [1,3,5] even = [2,4]

n = int(input("enter a number : "))
even={}
odd={}

for i in range(1,n+1,1):
    if i%2==0:
        # print("even")
        even[i] = i*i
        
    else:
        # print("odd")
        odd[i] = i*i
        
print("even : ",even)
print("odd : ",odd)
        

# if i%2==0:
#     print("even")
    
# else:
#     print("odd")
    
# i+=1
# if i%2==0:
#     print("even")
    
# else:
#     print("odd")
    
    