import mysql.connector

def conenct_mysql(user_id, password_id, port, database):
    connection = mysql.connector.connect(
        user=user_id, password=password_id, host='mysql', port=port, database=database)
    return connection