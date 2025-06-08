import mysql.connector as con
db = None
try:
    db = con.connect(host='localhost',db='py23',user='root',password='')
    print("connection established....")
except con.Error as e:
    # print("Type:", type(e))
    # print("Message:", str(e))
    # print("Args:", e.args)
    print("Errno:",str(e.errno))
    # print("SQLSTATE:", getattr(e, 'sqlstate', None))
    if e.errno == 1049:
        print('database does not exists')
    if e.errno == 1045:
        print('username does not exists') 
    if e.errno == -1:
        print('invalid password') 
    if e.errno == 2003:
        print('Have you started wamp server? also check servername') 
    
#insert, update, delete, create table, drop table (never return data)   
def runQuery(sql,data):
    print(sql)
    print(data)
    try:
        command = db.cursor()
        command.execute(sql,data)
        db.commit()
        return True
    except con.Error as e:
        print(e.errno)
        if e.errno == 1146:
            print ("table does not exist")
        if e.errno == 1054:
            print ("field name is not valid")
        if e.errno == -1:
            print ("no of fields and no of arguments does not match")
        return False
#fetchrow method is used to execute select statement
def fetchRow(sql,data=None):
    print(sql)
    try:
        command = db.cursor()
        if data==None:
            command.execute(sql)
        else:
            print(data)
            command.execute(sql,data)
        return command.fetchall()
    except con.Error as e:
        print(e.errno)
        if e.errno == 1146:
            print ("table does not exist")
        if e.errno == 1054:
            print ("field name is not valid")
        if e.errno == -1:
            print ("no of fields and no of arguments does not match")
        return None
# sql = "select * from books";
# print(fetchRow(sql))

# sql = "select * from books where id=%s"
# data = [1]
# print(fetchRow(sql,data))

# sql = "INSERT INTO `books` (`title`, `author`, `generation`, `year_published`, `status`) VALUES (%s,%s,%s,%s,%s)"

# title = 'abc'
# author = 'xyz'
# generation = 'drama'
# year_published = 2000
# status = 'owned'

# success = runQuery(sql,[title,author,generation,year_published,status])
# if success == False:
#     print('sql command failed')
# else:
#     print('sql command executed successfully')