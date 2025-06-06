# make count for vowel,consonant from file
vowel = 0
consonant = 0
number = 0

name = input("enter file name : ")
obj = open(name,"r")

# print(obj.read())
content = obj.read()

for i in content:
    if i in "aeiou":
        vowel+=1
    
    elif i in "0123456789":
        number+=1
      
    else:
        consonant+=1

print("vowels : ",vowel)
print("consonants : ",consonant)
print("number : ",number)
obj.close()
