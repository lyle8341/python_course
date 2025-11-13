"""
def 定义带有名称的函数 ===>可以重复使用
lambda关键字 定义匿名函数 ===>临时使用一次

语法定义:
    lambda 入参: 函数体(只能有一行代码)
"""


def func(_calculate):
    result = _calculate(1, 2)
    print(f"参数类型: {type(_calculate)}")
    print(result)


func(lambda x, y: x + y)
