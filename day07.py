#新增
# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor = con.cursor()
# sql = "insert into t_dept values(%s,%s,%s)"
# param= ["159","财务部","北京"]
#
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
#
# print("影响了",num,"行数据")
# # print(data)
# for i in data:
#     print(i)
# con.commit()
#
# cursor.close()
# con.close()

#删除
# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor = con.cursor()
# sql = "delete from t_dept where deptno=%s"
# param= ["159"]
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
#
# print("影响了",num,"行数据")
# # print(data)
# for i in data:
#     print(i)
# con.commit()
#
# cursor.close()
# con.close()

#修改
# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor = con.cursor()
# sql = "update t_dept set dname=%s,loc=%s where deptno=10"
# param= ['develop','新疆']
# num = cursor.execute(sql,param)
# # 查询的数据依然在游标里,获取游标里的数据
# data = cursor.fetchall()
#
# print("影响了",num,"行数据")
# # print(data)
# for i in data:
#     print(i)
# con.commit()
#
# cursor.close()
# con.close()

#查询
# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor = con.cursor()
# sql = "select * from t_dept where loc = %s"
# param = ["新疆"]
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
#
# print("影响了",num,"行数据")
# # print(data)
# for i in data:
#     print(i)
# con.commit()
#
# cursor.close()
# con.close()
