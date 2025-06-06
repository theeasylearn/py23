import mysql.connector as con

db = con.connect(host='localhost',db='py23',user='root',password='')
print("connection established...")

mycursor = db.cursor()

# sql ="select * from employee"
# mycursor.execute(sql)

# print(mycursor.fetchall())
# data = mycursor.fetchall()

# for i in data:
#     print(f"| {i[0]:2} | {i[1]:20} | {i[2]:10}  |  {i[3]:20} |")
#     print("-"*70)
    

sql = "select max(salary) from employee "
# values = [20000]

mycursor.execute(sql)
print(mycursor.fetchall())