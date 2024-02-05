import mysql.connector
from pandas import DataFrame
from sqlalchemy import create_engine

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

sql = """
    SELECT  name,
        `Non-Elderly Population` AS Non_Elderly,
        `Non-Elderly Uninsured Population` AS Non_Elderly_Uninsured,
        `Age 19-34`+`Age 35-49`+`Age 50-64` AS Age_19_64,
        a.Male,
        b.Male Male_Non_Elderly,
        a.Female,
        b.Female Female_Non_Elderly,
        c.confirmed_cases AS cases_covid19,
        deaths
    FROM censo_2020 a
    LEFT JOIN uninsurance_2021 b
        ON b.`State Name` = a.name 
    LEFT JOIN covid19 c 
        ON a.name = c.state_name;
    """   

cursor = connection.cursor()
cursor.execute(sql)
columns = [desc[0] for desc in cursor.description]
df = DataFrame(cursor.fetchall(),columns=columns)
connection.close()
engine = create_engine("mysql+mysqlconnector://root:root@mysql:3306/db")
df.to_sql('open_enrollment', con=engine, if_exists='replace', index=False)

print(df)