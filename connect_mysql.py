import mysql.connector 
from mysql.connector import Error

#function for connecting to SQL database
def connect_database():
    db_name = "fitness_center_db"   #make sure db_name matches the name of the data base
    user = "root"
    password = "password"    #enter in your own MySQL Workbench password
    host = "localhost"

    #connection is tested in a try block
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        #provides feedback when a connection is established and returns the connection data
        if conn.is_connected():
            print("Connected to MySQL database successfully")
            return conn

    #if the connection fails, provide the correct error message
    except Error as e:
        print(f"Error: {e}")
        return None