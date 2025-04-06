
import mysql.connector
import bcrypt
from mysql.connector import Error

# Database connection
def connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Change to your MySQL username
            password='',  # Change to your MySQL password
            database='krispy_king'  # Your database name
        )
        if conn.is_connected():
            print("Connected to MySQL")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None


# Hash password function
def hash_password(password):
    # Salt the password and hash it
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password



# Insert user function
def insert_user(fullname, email, username, password):

    # Hash the password before storing it
    hashed_password = hash_password(password)
            
    conn = connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (fullname, email, username, password) VALUES (%s, %s, %s, %s)"
            values = (fullname, email, username, hashed_password)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True, "User successfully signed up!"
        except Error as e:
            print(f"Error: {e}")
            return False, "Failed to sign up user."
    else:
        return False, "Database connection failed."


