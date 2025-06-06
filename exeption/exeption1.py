try:
    a = int(input("enter num1 : "))
    b = int(input("enter num2 : "))

    print(a+b)
    
    l1 = [1,2,3,4,5]
    for i in range(0,8):
        print(l1[i])
    
except Exception as e:
    print("error occured...")
    print(e)
    

print("good bye....")