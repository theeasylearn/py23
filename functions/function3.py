def getpercentage(maths=0,eng=0,science=0):
    if (maths<=100 and maths>=0) and (eng<=100 and eng>=0) and (science<=100 and science>=0):
        per = (maths+eng+science) / 3
        per = round(per,2)
        return per

    else:
        return "Give Valid Input!!!"
        
    

# maths = int(input("enter maths marks : "))
# eng = int(input("enter elnglish marks : "))
# science = int(input("enter science marks : "))

# print(getpercentage(maths,eng,science))
    
print(getpercentage(40,60))

# keyword argument
print(getpercentage(eng=90,maths=50,science=30))