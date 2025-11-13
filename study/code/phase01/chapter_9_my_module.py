#如果一个模块文件有 `__all__` 变量，当使用`from xxx import *`导入时，只能导入这个列表中的元素

__all__ = ['test', 'sub']


def test(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)

def mul(a, b):
    print(a * b)