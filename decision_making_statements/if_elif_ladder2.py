# check a string is uppercase , lowercase , is number
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Hello 
# HELLO
# hello

text = input("enter a string : ")
# print(text[0] in lower)

if text in upper:
    print(f"{text} is uppercase")
    
elif text in lower:
    print(f"{text} is lowercase")
    
elif text in number:
    print(f"{text} is a number")    
    
else:
    print("not found!!!")