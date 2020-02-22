import pymysql

count = "1446070"
bizdate = "123456"

db = pymysql.connect('localhost', 'root', '123456', 'test')
cursor = db.cursor()
cursor.execute("select * from kfc")
print(cursor.fetchall())
sql = 'insert into kfc(bizdate, count) values(%s, %s)'%(bizdate, count)
try:
    cursor.execute(sql)
    db.commit()
    cursor.execute("select * from kfc")
    print(cursor.fetchall())
except:
    db.rollback()
finally:
    cursor.close()
    db.close()
