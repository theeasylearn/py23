# write a program swap a number
# 23 -> 32

num = int(input("enter 2 digit number : "))

# 1st way to swap
num = str(num)    # type casting

# ans = num[1]+num[0]
ans = num[::-1]
print(ans)

# --------------------------------------------------------------
# 2nd way to swap
# 23
# 2.3
# ->2
# first = int(num/10)
# last = num%10

# first = str(first)
# last = str(last)

# print(last+first)
