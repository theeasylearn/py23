# check minimum number among 3 numbers
n1 = float(input("enter number1 : "))
n2 = float(input("enter number2 : "))
n3 = float(input("enter number3 : "))

if n1<n2:
    if n1<n3:  #false-> n3<n1<n2 
        print(f"{n1} is minimum")
    else:
        print(f"{n3} is minimum")   
elif n2<n1:
    if n2<n3:
        print(f"{n2} is minimum")
    else:
        print(f"{n3} is minimum")            
elif n1==n2:  #225   522
    if n2==n3:
        print("all are same")
    
    elif n3<n2:
        print(f"{n3} is minimum")
        
    else:
        print(f"{n1} is minimum")
else:
    print(f"{n3} is minimum")
    
    