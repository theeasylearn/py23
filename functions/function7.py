#Arbitrary Argument function
def calculate(*numbers):
    sum = 0 
    average = 0 
    for num in numbers:
        sum=sum + num 
    average = sum / len(numbers)
    return sum,average
    

result = calculate(10,20,30,40,50)
print(result)

result2 = calculate(10,20,30,40,50,90,70,80,100)
print(result2)