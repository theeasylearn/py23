try:
    age = int(input("enter your age : "))

    if age<18:
        raise TypeError    

    else:
        print("you are eligible....")
        
except ValueError:
    print("give valid input...")
    
except TypeError:
    print("your under 18!!!")
    
except:
    print("error")
        
print("good bye....")