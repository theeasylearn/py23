'''
a b c d
a b c
a b
a
'''
name = input("enter your name")
alphabets = list(name)
size = len(alphabets)
for row in range(size,0,-1):
    for column in range(0,row):
        print(alphabets[column],end='')
    print('')    
    
    
