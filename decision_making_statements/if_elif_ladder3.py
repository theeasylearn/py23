# Grade Calculator

# Take marks as input and assign grades based on the following:
# 90+ → A
# 80-89 → B
# 70-79 → C
# 60-69 → D
# Below 60 → F

# 3 subject mrks
maths = int(input("enter maths marks : "))
science = int(input("enter science marks : "))
eng = int(input("enter english marks : "))

if (maths<0 or maths>100) or (eng<0 or eng>100) or (science<0 or science>100): 
    print("wrong marks!!!")

else:
    
    # persantage
    marks = (maths+eng+science) / 3
    print(round(marks,2))

    marks = round(marks,2)

    if marks>=90:
        print("Grad : A")
        
    elif marks>=80 and marks<=89 : 
        print("Grad : B")
        
    elif marks>=70 and marks<=79:
        print("Grad : C")
        
    elif marks>=60 and marks<=69:
        print("Grad : D")

    else:
        print("Grad : F [FAIL]")