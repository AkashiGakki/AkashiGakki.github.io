import pymysql

data = {
    'id': '20190002',
    'name': 'Asuka',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
try:
    cursor.execute(sql, tuple(data.values()))
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
