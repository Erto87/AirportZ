import mysql.connector


def search_db(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='testi',
    user='root',
    password='kensendme',
    autocommit=True
    )