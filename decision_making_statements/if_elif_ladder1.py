# calculator

# 1->addition
# 2->subtraction
# 3->multiplication
# 4->division

print("""
# 1->addition
# 2->subtraction
# 3->multiplication
# 4->division""")

choice = int(input("enter your choice : "))

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

if choice==1:
    print(f"addition : {a+b}")
    
elif choice==2:
    print(f"subtraction : {a-b}")
    
elif choice==3:
    print(f"multiplication : {a*b}")
    
elif choice==4:
    print(f"division : {a/b}")
        
else:
    print('Invalid input!!!')
