import pymysql
host = "localhost"
password = ""
user = "root"
database = "bank"

def update(sql, param):  # 针对增删改的方法
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()

def find(sql, param, mode="all", size=1):  # 针对查询的方法
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    if mode == "all":  # 判断获取方式
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()
# 将数据库文件转为文本文件
sql="select * from user"
param=[]
# 找到数据库中的数据赋值给n
n=find(sql,param,mode="all",size=1)
# 打开g.txt文件
e = open("g.txt","w+",encoding="utf-8")
# 遍历数据库中的数据
for i in n:
    # 把数据库中数据的每一个每次都赋值给a
    a=i[0]+','+str(i[1])+','+str(i[2])+"\n"
    # 把数据库文件传到g.txt文件中保存
    e.write(a)
# 关闭b.txt文件
e.close()










