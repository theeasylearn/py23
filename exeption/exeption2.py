try:
    file = open("../exercise2.txt")
    
except:
    print("give correct file name")

else:
    print(file.read())
    file.close()


