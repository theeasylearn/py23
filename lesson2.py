text = "hello world"

# slice operator
print(text[0])
print(text[1])
print(text[2])
print(text[3])

print("-----------------------")
# print hello
# print(text[0],end="")
# print(text[1],end="")
# print(text[2],end="")
# print(text[3],end="")
# print(text[4],end="")

# string_name[start=0:end=last:size=1]
print(text[0:5:1])
print(text[:])

# olleh
print(text[4::-1])

print(text[::-1])

a="hello\n"
b="word"
print(a+" "+b)  #concatination

print(a*5)  # repeatation

data = "12345"
print(len(data))