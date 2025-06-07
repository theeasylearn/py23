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
import connection 
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
        print("insert new book")
    elif choice==2:
        print("display all book")
    elif choice==3:
        print("edit book")
    elif choice==4:
        print("delete book")
    elif choice==5:
        print("search book")
    elif choice==0:
        print("good bye")

    