# print("-----------------------------")
# print("python")
# print("-----------------------------")

# define function
# without argument without return value function
def printline():
    print("-----------------------------")

# with argument without return value
# argument received by function, is formal argument
def addition(a,b):
    print("addition : ",a+b)
    # changes in below line is applied to a b received as argument not in original variable
    a = 0
    b = 0
def subtraction(a,b):
    temp = a - b 
    print("subtraction = ",temp)
def multiplication(a,b):
    temp = a * b 
    print(f"multiplication = {temp}")
def division(a,b):
    temp = a / b 
    print(f"division = {temp}")
    
# function calling
printline()
printline()
print("python")
printline()
printline()

a = int(input("enter number1 : ")) # 10
b = int(input("enter number2 : ")) # 20 
# print(x,y)
# function call 
addition(a,b) # argument supplied to while calling function, is actual argument
subtraction(a,b)
multiplication(a,b)
division(a,b)