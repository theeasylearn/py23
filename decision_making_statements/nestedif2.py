# Title: Ticket Price Calculation Based on Age and Time
# Ask the user for their age and the time of entry (morning/evening).
# If the age is below 12 or above 60, give a 50% discount.
# If it's evening time, apply an extra 10% charge.
# Print the final ticket price based on these conditions.

age = int(input("enter your age : "))
time = int(input("1->morning & 2->evening time : "))
price = 500

if (time==1 or time==2) and (age>5 and age<100) :
    if age<=12 or age>=60:
        print("congrats! you got 50% off")
        price = price - ((50/100) * price)

    if time==2:
        print("10% extra charges....")
        price = price + ((10/100)*price)
    
    print(f"your final price : {price}")
    
else:
    print("Invalid Input!!!")
    
