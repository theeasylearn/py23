n1 = float(input("enter number1 : "))
n2 = float(input("enter number2 : "))

print(n1==n2)
print(n1!=n2)
print(n1>n2)
print(n1<n2)
print(n1>=n2)
print(n1<=n2)

# -----------------------------------------------------
a = 10
b = 10
c = 10
# check all variable value are same or not
print(a==b and b==c)

print(a==b or a==c)

print(not(a==b and b>c or c<=a))

print(not(a>b and a==c or c<a or not(c!=a)))
