
import mysql.connector
import bcrypt
from datetime import datetime
from mysql.connector import Error

# Database connection
def connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='', 
            database='krispy_king'  
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
            query = "SELECT id, password FROM useraccount WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            # Format datetime to 'Month Day, Year at HH:MM AM/PM'
            current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")

            if result:
                user_id, stored_password = result[0], result[1]
                stored_password = stored_password.encode('utf-8') if isinstance(stored_password, str) else stored_password
                # stored_password = result[0].encode('utf-8') if isinstance(result[0], str) else result[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    log_status = "Login successful"
                    cursor.execute(
                        "INSERT INTO logs (status, datetime, userid) VALUES (%s, %s, %s)",
                        (log_status, current_time, user_id)
                    )
                    conn.commit()
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
            query = "INSERT INTO useraccount (fullname, email, username, password) VALUES (%s, %s, %s, %s)"
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


