import sqlite3

#a function to create a database and connect to it
def connect():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer )")
    connection.commit()
    connection.close()

#an insert function to add new values to the database
def insert(title, author, year, isbn):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title,author,year,isbn))
    connection.commit()
    connection.close()


#a function to fetch and view all data
def view():
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    connection.close()
    return results


#a search function to search by book/author/year or isbn
def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("bookstore.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    results = cursor.fetchall()
    connection.close()
    return results




connect()

