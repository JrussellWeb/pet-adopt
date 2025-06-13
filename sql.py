from flask import g
import sqlite3

# get a connection from the app context so that we don't open the database more than once during a session
def get_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = connect_database("data.db")
        g._connection = connection
        setup_user_table(connection)

    return connection

def connect_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def close_database():
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()
        delattr(g, '_connection')

def setup_user_table(connection):
    cursor = connection.cursor()
    # Check if the table exists
    cursor.execute("""SELECT name FROM sqlite_master 
                   WHERE type = 'table' 
                   AND name = 'user'""")
    row = cursor.fetchone()
    if row:
        # Already set up
        return
    
    # Table does not exist; create it
    cursor.execute("""CREATE TABLE user (
        username TEXT,
        password TEXT,
        email TEXT,
        PRIMARY KEY(username)
    )""")

    return

def insert_user(username, password, email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO user 
                   (username, password, email) 
                   VALUES (?, ?, ?)""", (username, password, email))
    connection.commit()

def get_user(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM user
                   WHERE username = ?""", (username,))
    row = cursor.fetchone()
    return row

