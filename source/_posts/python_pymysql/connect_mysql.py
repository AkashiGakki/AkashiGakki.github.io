import pymysql

# 创建一个连接，新建数据库并且输出版本

db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version: ', data)
cursor.execute('create database spiders default character set utf8mb4')
db.close()
