import pymysql

table = 'students'
condition = 'age > 20'

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)

try:
    cursor.execute(sql)
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
