#with argument with return value 
def getInterest(amount,rate=10,year = 1):
    print(f"amount = {amount} rate = {rate} year = {year}")
    interest = (amount * rate * year) / 100 
    return interest

amount = int(input("Enter amount"))
rate = int(input("Enter rate"))
year = int(input("Enter year"))

interest = getInterest(amount,rate,year)
print(f"Interest = {interest}")

#2nd call 
interest = getInterest(amount,rate)
print(f"(2nd call) Interest = {interest}")

#3rd call 
interest = getInterest(amount)
print(f"(3rd call) Interest = {interest}")