import mysql.connector

def get_connection():

    connection = mysql.connector.connect(
        host='',
        port=,
        database='',
        user='',
        password='kensendme',
        autocommit=
        )
    return connection