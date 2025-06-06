import mysql.connector as con

db = con.connect(host='localhost',db='php24',user='root',password='')

print("connection established....")