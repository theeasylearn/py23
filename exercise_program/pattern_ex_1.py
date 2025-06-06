'''
a b c d
a b c
a b
a
'''
alphabets = ['A ','B ','C ','D ']
for row in range(5,1,-1):
    for column in range(0,row-1):
        print(alphabets[column],end='')
    print('')    
    
