Library Management System with MySQL Integration
Overview
The Library Management System is a Python-based application that manages the operations of a library, including books, users, and authors. It integrates Object-Oriented Programming (OOP) concepts with MySQL to provide persistent storage and enhanced functionality.

This project is a continuation of the OOP-based Library Management System developed in Module 4. It leverages MySQL for data storage and retrieval, extending the system's capabilities for better data management and scalability.

Features
Books Management:

Add new books to the library
Search for books by title or ISBN
Borrow and return books
Display all books
Users Management:

Add new users
View user details
Display all users
Authors Management:

Add new authors
View author details
Display all authors
Borrowing System:

Borrow books for users
Track borrowed books and return dates
Handle availability of books
Project Structure
Python Classes: Object-oriented programming is used to create classes like Book, User, Author, and Genre which interact with the MySQL database.
MySQL Database Integration: CRUD operations (Create, Read, Update, Delete) are performed on a MySQL database to manage persistent data storage.
Command-Line Interface (CLI): The system offers an interactive CLI that allows users to perform operations like adding books, borrowing books, and managing users.
Database Schema
The database contains four main tables:

Books Table: Stores information about books, including title, author, ISBN, publication date, and availability.
Authors Table: Stores author details such as name and biography.
Users Table: Stores user information such as name and library ID.
Borrowed Books Table: Tracks borrowing history, including borrow and return dates.

Prerequisites
To run this project, ensure you have the following installed on your system:

Python 3.x
MySQL Server
MySQL Connector for Python

Setting Up the Database:
1. Create a MySQL Database
2. Run the SQL Scripts: Use the provided SQL scripts to create the necessary tables for the library management system.
3. Configure Database Connection: In the Python code, update the create_connection() function with your MySQL credentials:

Running the Application:
1. Clone the repository or download the project files.
2. Ensure the database setup is complete and MySQL is running.
3. Run the Python script from your command line:

Example Usage
Add a New Book:

From the main menu, choose "Book Operations" and then "Add a new book."
Enter the book details like title, author ID, ISBN, and publication date.
Borrow a Book:

Choose "Book Operations" and then "Borrow a book."
Enter the user ID and book ID to borrow the book.
Return a Book:

Choose "Book Operations" and then "Return a book."
Enter the book ID to return it and update the availability.
Error Handling
Duplicate Entries: The system handles duplicate entries for books, users, and borrowed books. For example, a unique constraint is enforced on ISBN numbers and user library IDs.
Invalid IDs: If an invalid book or user ID is entered, the system will alert the user and ask for valid input.
Future Enhancements
Genre and Category Management: Extend the system to allow the addition of genres and categories for books.
Advanced Search: Add more search filters, such as searching for books by genre, author, or publication year.
Overdue Book Tracking: Implement functionality to track overdue books and notify users of overdue return dates.
