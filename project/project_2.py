'''
Book Library (Single Table)
Description:
A mini system to manage books in your personal library.

Table: books
Fields:
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- title (TEXT)
- author (TEXT)
- genre (TEXT)
- year_published (INTEGER)
- status (TEXT: owned/Borrowed)

Features:
- Add, edit, delete books
- Mark books as borrowed or available
- Search by title or author
'''
def displayBook():
    sql = "select * from books order by id desc"
    table = cn.fetchRow(sql)
    print(f"{'':7} id {'title':32} {'author':32} {'generation':32} {'':6}year published {'status':20}")
    print("_"*140)
    for row in table:
        print(f"{row[0]:10} {row[1]:32} {row[2]:32} {row[3]:32} {row[4]:20} {row[5]:20}")
        print("_"*140)
    pause = input('press any key to continue')
import connection as cn
choice = None 
while choice!=0:
    print("Press 1 to insert new book")
    print("Press 2 to display all book")
    print("Press 3 to edit book")
    print("Press 4 to delete book")
    print("Press 5 to search book")
    print("Press 0 to exit from application")
    choice = int(input("Enter your choice"))
    if choice<0 or choice>=6:
        print("invalid choice")
    elif choice==1:
        print("Enter new book detail")
        title = input("Enter title")
        author = input("Enter author")
        generation = input("Enter generation")
        year_published = input("Enter year published")
        status = input("Enter status(owned,borrowed)")
        sql = "INSERT INTO `books` (`title`, `author`, `generation`, `year_published`, `status`) VALUES (%s,%s,%s,%s,%s)"
        data = [title,author,generation,year_published,status]
        success = cn.runQuery(sql,data)
        if success == False:
            print('new book could not be inserted.')
        else:
            print('new book has been added')
    elif choice==2:
        displayBook()
    elif choice==3:
        displayBook()
        id = int(input("Enter book id to edit book"))
        sql = "select * from books where id=%s"
        data = [id]
        table = cn.fetchRow(sql,data)
        count = len(table)
        if count==0:
            print("Book not found")
        else:
            print("Enter book detail")
            title = input("Enter title")
            author = input("Enter author")
            generation = input("Enter generation")
            year_published = input("Enter year published")
            status = input("Enter status(owned,borrowed)")
            sql = "update books set title=%s, author=%s, generation=%s, year_published=%s, status=%s where id=%s"
            data = [title,author,generation,year_published,status,id]
            success = cn.runQuery(sql,data)
            if success == False:
                print('book can not be updated')
            else:
                print('book has been updated successfully')
                
    elif choice==4:
        displayBook()
        id = int(input("Enter book id to edit book"))
        sql = "select * from books where id=%s"
        data = [id]
        table = cn.fetchRow(sql,data)
        count = len(table)
        if count==0:
            print("Book not found")
        else:
            sql = "delete from books where id=%s"
            success = cn.runQuery(sql,data)
            if success == False:
                print('book can not be updated')
            else:
                print('book has been deleted successfully')
    elif choice==5:
        title = input("Enter book name to search")
        sql = "select * from books where title=%s"
        data = [title]
        table = cn.fetchRow(sql,data)
        print(f"{'':7} id {'title':32} {'author':32} {'generation':32} {'':6}year published {'status':20}")
        print("_"*140)
        if len(table)==0:
            print('data not found')
        else:
            for row in table:
                print(f"{row[0]:10} {row[1]:32} {row[2]:32} {row[3]:32} {row[4]:20} {row[5]:20}")
                print("_"*140)
        pause = input('press any key to continue')
    elif choice==0:
      print("good bye")