import os

# # create folder
os.mkdir("../python")

print(os.getcwd())

# # change dir
os.chdir("../functions")

# # print current woring directory
print(os.getcwd())

# os.chdir("../")
# print(os.getcwd())

# # remove empty dir
os.rmdir("demo")
# os.rmdir("../functions")