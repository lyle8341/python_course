"""
pip install pymysql
"""

from pymysql import Connection

# 获取到mysql数据库连接对象
conn = Connection(
    host="localhost",
    port=3307,
    user='root',
    password='root'
)
print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("lyle")

# 执行非查询性质的SQL
cursor.execute("create table if not exists test_pymysql(id INT, info varchar(255))")

# 查询语句
cursor.execute("select * from student limit 100")
result: tuple = cursor.fetchall()
for r in result:
    print(r)


# 关闭数据库连接
conn.close()
