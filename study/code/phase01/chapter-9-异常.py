"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
[else:]
    没有异常的时候执行
[finally:]
    无论如果，都执行
"""
#基础语法（捕获全部异常）
try:
    f = open("not_exist.txt", "r", encoding="UTF-8")
except:
    print("出现异常了。没有找到文件")

# 捕获指定异常
try:
    print(fuck)
except NameError as e:
    print("变量未定义异常")
    print(e)

# 捕获多个异常
try:
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print("除0异常")
    print(e)

#捕获全部异常
try:
    1 / 0
except Exception as e:
    print(e)