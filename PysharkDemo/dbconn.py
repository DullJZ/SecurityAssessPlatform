import mysql.connector

config = {
    "host": "localhost",
    "port": 13306,
    "user": "root",
    "password": "root",
    "database": "pysharkDB"
}
conn = mysql.connector.connect(**config)

db_name = config["database"]

print("数据库连接成功")

# 检测数据库是否存在
cursor = conn.cursor()
cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
if cursor.fetchone() is None:
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"数据库 {db_name} 创建成功")

# 检测数据表是否存在
table_name = "xhcms"
cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
if cursor.fetchone() is None:
    cursor.execute(f"""
    CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP NOT NULL COMMENT '请求时间',
        top_layer VARCHAR(255) NOT NULL COMMENT '顶层协议',
        src_ip VARCHAR(255) NOT NULL COMMENT '源ip',
        dst_ip VARCHAR(255) NOT NULL COMMENT '目的地址',
        http_header JSON NULL COMMENT '头部',
        http_data MEDIUMBLOB NULL COMMENT '数据',
        is_sql_hack TINYINT(1) NOT NULL DEFAULT 0 COMMENT '是否为SQL注入'
    ) COMMENT '熊海cms流量监控' COLLATE = utf8mb4_general_ci
    """)
    print(f"数据表 {table_name} 创建成功")