"""
读取文件
"""
import _io

f = open("chapter-8-读文件.py", "r", encoding="UTF-8")
print(type(f))


# read()
def read_fun(f: _io.TextIOWrapper):
    print(f"读取10字节: {f.read(10)}")
    print(f"读取全部字节: {f.read()}")


# readLines()
def readLine_fun(f: _io.TextIOWrapper):
    lines = f.readline()
    print(f"line对象的类型: {type(lines)}")
    print(f"lines对象的内容: {lines}")


# for循环读取文件
def for_fun(f: _io.TextIOWrapper):
    for line in f:
        print(line)


# read_fun(f)
# readLine_fun(f)
for_fun(f)

# 关闭文件，解除文件占用
f.close()

# with open 会自动关闭文件
with  open("chapter-8-读文件.py", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)
