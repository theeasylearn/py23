name = input("enter file name : ")
text = input("enter content : ")

file = open(name,"w")

file.write("\n"+text)
print("data witten in file....")

file.close()