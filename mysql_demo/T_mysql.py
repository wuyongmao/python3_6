#!/usr/bin/python3
'''
mysql CRUD (pymysql)



'''
import pymysql
import urllib.request
j=10
i=0
try:  
# 打开数据库连接
    db = pymysql.connect("localhost","root","root","db1",charset='utf8')
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")
    
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
     
    print ("Database version : %s " % data)
    
    
    
#Crete table
#     cursor.execute("create table   pytable(a int,b varchar(10))")   
    while i<j :    
        sql="insert into pytable values(%d,'w%s')" % (i,i)
        cursor.execute(sql)
        print(i)
        i=i+1
    
    db.commit()
    


#查询数据
    sql="select * from pytable"
    
    print(type(cursor.execute(sql)))
    results= cursor.fetchall()
    for row in results :
        t1=row[0]
        t2=row[1]
        print("t1=%s,t2=%s"%(t1,t2))
      
 
finally:
# 关闭数据库连接
    if db:
        db.close()