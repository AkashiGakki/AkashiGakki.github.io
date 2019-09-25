import pymysql

data = {
    'id': '20190001',
    'name': 'Akashi',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'insert into {table}({keys}) values({values}) on duplicate key update'.format(table=table, keys=keys, values=values)

update = ','.join([" {key} = %s".format(key=key) for key in data])

sql += update

try:
    cursor.execute(sql, tuple(data.values())*2)
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
