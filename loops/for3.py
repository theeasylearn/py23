# hello
# h:1 e:1 l:2 o:1

text = input("enter a string : ")
d1={}

# print(text.count('l'))

for i in text:
    d1[i] = text.count(i)
        
print(d1)

