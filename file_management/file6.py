import os


def append_text(name,content):
    file = open(name,"a")
    file.write("\n"+content)

    file.close()    
    print("data witten in file")
    
# name = input("enter file name : ")
# content = input("enter content : ")

# append_text(name,content)

def rename_file(old,new):
    os.rename(old,new)
    print("rename successfuly")
    
# # rename_file("demo2.txt","demo2.py")
# # rename_file("demo2.py","new.py")
# # ../- exit
# # ./ - current folder
# # rename_file("new.py","../new.py")


def delete_file(name):
    os.remove(name)
    print("file deleted successfuly")
    
# # delete_file("lesson1.py")
# delete_file("lesson1.py")


os.rename("demo.txt","demo2.txt")
os.remove("new.txt")