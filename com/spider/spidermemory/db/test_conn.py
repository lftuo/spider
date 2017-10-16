import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306,charset='utf8')
cur = conn.cursor()
cur.execute(' create table person (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY , name VARCHAR(20),age INT)')
data = "'qiye',20"
cur.execute(' insert into person (name,age) VALUES (%s)'%data)
conn.commit()
