num = 0
while num < 100:
    print("起床!")
    num += 1

# for遍历字符串

name = "xylophone"
for x in name:
    print(x, end=" ")
print()

"""
range(num1, num2)
[num1, num2)

range(num1, num2, step)
step默认为1
"""
for x in range(10):  # 0~9
    print(x, end=" ")
print()

for x in range(5, 10):  # 5~9
    print(x, end=" ")
print()

for x in range(5, 10, 2):  # 5，7，9
    print(x, end=" ")
