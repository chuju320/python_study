#-*-coding:utf-8-*-

import pymysql,mysqldb

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='mysql')
cur = conn.cursor()
cur.execute('select host,user from USER ')

print cur.description
r = cur.fetchall()
print r


for i in cur:
    print i

cur.close()
conn.close()