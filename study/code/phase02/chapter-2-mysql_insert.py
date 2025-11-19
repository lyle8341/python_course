from pymysql import Connection

# 获取到mysql数据库连接对象
conn = Connection(
    host="localhost",
    port=3307,
    user='root',
    password='root',
    # autocommit=True
)

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("lyle")

# 执行非查询性质的SQL
cursor.execute("insert into test_pymysql values (1,'today is wednesday')")

# 手动确认
conn.commit()
# 关闭数据库连接
conn.close()
