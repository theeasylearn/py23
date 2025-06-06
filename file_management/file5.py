# read data from one file and write to another file
# copy - paste

copy = input("enter file for read : ")
paste = input("enter file for write : ")

obj1 = open(copy,"r")
text = obj1.read()

obj1.close()

print("copied...")

obj2 = open(paste,"w")
obj2.write(text)

obj2.close()

print("paste....")

