import mysql.connector

config = {
    "host": "139.159.154.40",
    "port": 30006,
    "user": "pyshark_demo",
    "password": "xhwZWNdD32rZnmPs",
    "database": "pyshark_demo"
}
conn = mysql.connector.connect(**config)

print("数据库连接成功")
