import mysql.connector

config = {
    "host": "localhost",
    "port": 13306,
    "user": "root",
    "password": "root",
    }
conn = mysql.connector.connect(**config)

print("数据库连接成功")
