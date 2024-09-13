# Enhanced User Interface (UI) and Menu:

# Book Class

import mysql.connector

class Book:
    def __init__(self, book_id, title, author, genre, is_borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = is_borrowed

    @staticmethod
    def add_book(book_id, title, author, genre):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                database='LibraryDB',
                user='root',
                password='Password'
            )
            cursor = connection.cursor()
            query = """INSERT INTO Books (book_id, title, author, genre, is_borrowed)
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (book_id, title, author, genre, False))
            connection.commit()
            print("Book added successfully.")
        except mysql.connector.Error as e:
            print(f"Error adding book: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def display_all_books():
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                database='LibraryDB',
                user='root',
                password='Password'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Books")
            for (book_id, title, author, genre, is_borrowed) in cursor.fetchall():
                print(f"ID: {book_id}, Title: {title}, Author: {author}, Genre: {genre}, Borrowed: {is_borrowed}")
        except mysql.connector.Error as e:
            print(f"Error retrieving books: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


# User Class

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @staticmethod
    def add_user(user_id, name, email):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                database='LibraryDB',
                user='root',
                password='Password'
            )
            cursor = connection.cursor()
            query = """INSERT INTO Users (user_id, name, email) VALUES (%s, %s, %s)"""
            cursor.execute(query, (user_id, name, email))
            connection.commit()
            print("User added successfully.")
        except mysql.connector.Error as e:
            print(f"Error adding user: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


# Author Class

class Author:
    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name

    @staticmethod
    def add_author(author_id, name):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                database='LibraryDB',
                user='root',
                password='Password'
            )
            cursor = connection.cursor()
            query = """INSERT INTO Authors (author_id, name) VALUES (%s, %s)"""
            cursor.execute(query, (author_id, name))
            connection.commit()
            print("Author added successfully.")
        except mysql.connector.Error as e:
            print(f"Error adding author: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


# CLI Menu

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Display all books")
    # Other options borrow,return,search books will be added
    choice = input("Enter your choice: ")
    
    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        Book.add_book(book_id, title, author, genre)
    elif choice == "2":
        Book.display_all_books()
    else:
        print("Invalid choice. Please try again.")

def user_operations():
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. Display all users")
    # Uer-related operations can be added here
    choice = input("Enter your choice: ")
    
    if choice == "1":
        user_id = input("Enter User ID: ")
        name = input("Enter User Name: ")
        email = input("Enter User Email: ")
        User.add_user(user_id, name, email)
    else:
        print("Invalid choice. Please try again.")

def author_operations():
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. Display all authors")
    # Other author-related operations can be added here
    choice = input("Enter your choice: ")
    
    if choice == "1":
        author_id = input("Enter Author ID: ")
        name = input("Enter Author Name: ")
        Author.add_author(author_id, name)
    else:
        print("Invalid choice. Please try again.")

# Start the system
main_menu()

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='MYSQL',
            user='root',
            password='Password'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")


# Adding A New Book

def add_book(title, author_id, isbn, publication_date):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Query to insert a new book
        query = """INSERT INTO books (title, author_id, isbn, publication_date) 
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (title, author_id, isbn, publication_date))
        
        connection.commit()
        print("Book added successfully.")
    
    except Error as e:
        print(f"Error while adding book: {e}")
    
    finally:
        close_connection(connection)

# Borrowing A Book

def borrow_book(user_id, book_id, borrow_date):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Check if book is available
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        availability = cursor.fetchone()[0]
        
        if availability == 1:
            # Book is available, allow borrowing
            query = """INSERT INTO borrowed_books (user_id, book_id, borrow_date) 
                       VALUES (%s, %s, %s)"""
            cursor.execute(query, (user_id, book_id, borrow_date))
            
            # Update the book's availability to 0 
            cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
            
            connection.commit()
            print("Book borrowed successfully.")
        else:
            print("The book is currently not available.")
    
    except Error as e:
        print(f"Error while borrowing book: {e}")
    
    finally:
        close_connection(connection)


# Return A Book

def return_book(book_id, return_date):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Check if book is borrowed
        cursor.execute("SELECT * FROM borrowed_books WHERE book_id = %s AND return_date IS NULL", (book_id,))
        borrow_record = cursor.fetchone()
        
        if borrow_record:
            # Update the borrowed_books record with the return date
            query = """UPDATE borrowed_books 
                       SET return_date = %s WHERE book_id = %s AND return_date IS NULL"""
            cursor.execute(query, (return_date, book_id))
            
            # Update the book's availability to 1 
            cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
            
            connection.commit()
            print("Book returned successfully.")
        else:
            print("This book is not currently borrowed.")
    
    except Error as e:
        print(f"Error while returning book: {e}")
    
    finally:
        close_connection(connection)
