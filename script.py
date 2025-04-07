
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


def login_user(username, password):
    conn = connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0].encode('utf-8') if isinstance(result[0], str) else result[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    return True, "Login successful!"
                else:
                    return False, "Incorrect password."
            else:
                return False, "Username not found."

        except Error as e:
            print(f"Error: {e}")
            return False, "Login failed."
        finally:
            cursor.close()
            conn.close()
    else:
        return False, "Database connection failed."
    

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


