import mysql.connector as con

db = con.connect(host='localhost',db='py23',user='root',password='')
print("connection established...")

mycursor = db.cursor()

sql = "delete from student where id=%s"

id = int(input("enter id: "))

values=[id]

mycursor.execute(sql,values)

db.commit()