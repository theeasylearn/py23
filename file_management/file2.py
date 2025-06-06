name = input("enter file name : ")
obj = open(name,"r")
num = "0123456789"

for i in obj:
    for j in i:
        if j in num:
            continue
        else:
            print(j,end="")
            
            
# for i in obj.read():
    
    
obj.close()