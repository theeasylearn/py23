import mysql.connector as con

db = con.connect(host='localhost',db='py23',user='root',password='')
print("connection established...")

mycursor = db.cursor()

sql = "insert into student value(%s,%s,%s,%s,%s)"

name = input("enter your name : ")
age = int(input("enter your age : "))
mobile = int(input("enter your phone : "))
gender = int(input("1=male, 0=female : "))

values = ['',name,age,mobile,gender]

mycursor.execute(sql,values)

db.commit()
