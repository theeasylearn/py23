from random import *
# import random

numbers =  ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
           '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '|', '`', '~']

n = int(input("enter number for numbers : "))
s = int(input("enter number for small : "))
c = int(input("enter number for capital : "))
sym = int(input("enter number for symbol : "))

# print(dir(random))
password = choices(numbers,k=n)+choices(small,k=s)+choices(capital,k=c)+choices(symbols,k=sym)

shuffle(password)

# print(str(password))
psw = ''
for i in password:
    psw = i+psw
    
print(psw)