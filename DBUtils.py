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


# sql="select * from 用户表"
# param=[]
# data = find(sql,param,mode="many",size=1)
# print(data)

f = open("yonghushuju.txt", "r+", encoding="utf-8")
lis = f.readlines()
for i in lis:
    #把数据的换行换成空字符串，并且以逗号隔开，并且把数据赋值给use_lis
    use_list = i.replace("\n","").split(",")
    sql = "insert into user values(%s,%s,%s)"
    #将值传给param
    param = use_list
    #调用update方法
    update(sql,param)
f.close()
#净资产总和
sql = "select sum(money) from user"
param = []
data = find(sql,param,mode="all",size=1)
print(data)























