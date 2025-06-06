import mysql.connector as con

db = con.connect(host='localhost',db='py23',user='root',password='')
print("connection established...")

mycursor = db.cursor()

sql = "update student set mobile = %s where id=%s"

id= int(input("enter id : "))
mobile= int(input("enter mobile : "))

values = [mobile,id]

mycursor.execute(sql,values)

db.commit()