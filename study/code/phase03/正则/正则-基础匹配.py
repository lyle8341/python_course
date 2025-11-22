import re

s = "1python study self python"

# match 从头匹配
result = re.match("python", s)
print(result)
if result is not None:
    print(result.span())
    print(result.group())

# search 搜索整个字符串，找出匹配的，从前向后，找到第一个后就停止
s = "1python44444python213355python"
result = re.search("python", s)
print(result)
if result is not None:
    print(result.span())
    print(result.group())

# findall 找出全部匹配项，找不到返回空 list
result = re.findall('python', s)
print(result)
result = re.findall('lyle', s)
print(result)


