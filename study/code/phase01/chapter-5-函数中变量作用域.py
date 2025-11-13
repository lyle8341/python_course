# 全局变量
num = 400


def func():
    num = 300
    print(f"函数内部的num: {num}")


func()
print(f"全局num: {num}")


def func2():
    global num
    num = 9527
    print("函数内部声明全局变量")


func2()
print(f"全局num: {num}")