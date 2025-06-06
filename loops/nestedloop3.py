text = "abcdefghijklmnopqrstuvwxyz"

data = input("enter a latter : ")

# print(text.index('e'))

if len(data) == 1:
    for j in range(0,text.index(data)+1):
        for i in range(0,j):
            print(text[i],end=" ")
        print(text[j])

else:
    print("give single character!!!")

# for i in range(0,1):
#     print(text[0],end=" ")
# print(text[1])

# for i in range(0,2):
#     print(text[i],end=" ")  
# print(text[2])

# for i in range(0,3):
#     print(text[i],end=" ")
# print(text[3])

