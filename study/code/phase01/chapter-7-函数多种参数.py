def user_info(name, age, gender):
    print(f"名字:{name}，年龄:{age}，性别:{gender}")


# 1.位置参数：调用函数时根据函数定义的参数位置来传递参数
user_info("Tom", 2, "雄")

# 2.关键字参数： 键值对
user_info(age=1, gender="雌性", name="小红")
# 和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("小李", age=4, gender="中性")


# 3.缺省参数,！！！必须要在最后
def account_info(name, age, gender="男"):
    print(f"名字:{name}，年龄:{age}，性别:{gender}")


account_info('始皇帝', 70)


# 4.1位置传递不定长 --- args 是元组类型
def stu_info(*args):
    print(args)


stu_info("Tom")
stu_info("Tom", 3)
stu_info("Tom", 3, "女")


# 4.2关键字不定长 ---- kwargs 是字典类型
def user(**kwargs):
    print(kwargs)


user(name="Tom", age=13, id=30)
