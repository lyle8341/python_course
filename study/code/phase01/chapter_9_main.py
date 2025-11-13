def add(a, b):
    print(a + b)


# chapter-9-main.py 这么写的话，只要模块被引用后就会被执行,所以需要写在 __name__下
if __name__ == '__main__':
    add(5, 6)
