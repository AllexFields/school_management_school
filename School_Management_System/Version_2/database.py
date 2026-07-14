import mysql.connector
from mysql.connector import Error


def get_connection():
    """
    Creates and returns a connection to MySQL Database.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="EmmaWatson@MySQL21011986",   
            database="school_db"
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print("Database Connection Error :", e)

    return None