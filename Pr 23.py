#23.	Integrate SQL with Python by importing suitable module.
import pymysql as pym
mycon=sqltor.connect(host="localhost",user="root",passwd="tiger",database="gvkcv")
cursor=mycon.cursor()
cursor.execute("select *from student10")
data=cursor.fetchall()
for i in data:
    print(i)
mycon.close() 