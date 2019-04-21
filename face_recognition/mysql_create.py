import pymysql

def connect_sql():
    #连接数据库
    conn = pymysql.connect(
        host='127.0.0.1', #本地地址   主机IP地址  也可以替换为   localhost
        user='root',      #账户
        passwd='123456',  #密码
        db='test',     #数据库名字
        charset='utf8mb4',
    )
    cur = conn.cursor()

    return conn, cur


#这个只能创建列表时用
def creat_table(table_name, cur):
    sql = "creat " + table_name + " if not exists " + table_name
    print(sql)
    try:
        cur.execute(sql)
        print("create table " + table_name + " successful")
    except Exception:
        print("create faild")
    finally:
        print("create over")









