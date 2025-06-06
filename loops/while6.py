latters = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

char = input("enter a latter : ")

# find key of latter
count=0
# print(list(latters.items()))
l1 = list(latters.items())

while count<=25:
    if char == l1[count][1]:
        key = l1[count][0]
    count+=1
    
count = 1
while count<=key:
    print(latters[count],end=" ")
    count+=1

# print(latters[2])
# print(latters[3])
# print(latters[4])
