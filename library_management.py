#connect mysql
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sai2323",
    database="library_db")
cursor=conn.cursor()

#python code

#Add Books 
def add_book():
    title=input("Enter Book title :")
    author=input("Enter Author Name :")
    query="INSERT INTO books(title,author,book_status) VALUES (%s,%s,%s)"
    values=(title,author,"Avilable")

    cursor.execute(query,values)
    conn.commit()

#view the Books

def view_book():
    cursor.execute("SELECT * FROM books")
    books=cursor.fetchall()
    if books:
        for book in books:
            print("ID:",book[0])
            print("Title:",book[1])
            print("Author:",book[2])
            print("Status:",book[3])
            print("-------------------")
    else:
        print("Book is Not Found \n")

#return book

def return_book():
    book_id=input("Enter Book ID to Return :")
    cursor.execute("UPDATE books SET book_status='Avilable' WHERE book_id=%s",(book_id,))
    conn.commit()


def delete_book():
    book_id=input("Enter Book ID To Delete :")
    cursor.execute("DELETE FROM books WHERE book_id=%s",(book_id,))
    conn.commit()
    print("Book Deleted Sucessfully! \n")

while True:
    print("------LIBRAEY MANAGEMENT SYSTEM--------")
    print("1.Add Book")
    print("2.View Book")
    print("3.Return Book")
    print("4.Delete Book")
    print("5.Exit")

    choice=input("Enter your Choice :")
    if choice=="1":
          add_book()
    elif choice=="2":
          view_book()
    elif choice=="3":
          return_book()
    elif choice=="4":
          delete_book()
    elif choice=="5":
          print("Exit")
    break
else:
    print("---Invalid Choice---")

cursor.close()
conn.close()

    
 