import mysql.connector
conn = mysql.connector.connect(user='root',password='leoliu1033',database='course_db')
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id,name) values(%s,%s)',['1','leoliu'])
# print('rowcount = ', cursor.rowcount)
cursor.execute('select * from user where id = %s',('1',))
value = cursor.fetchall()
print(value)
# conn.commit()
cursor.close()
conn.close()

