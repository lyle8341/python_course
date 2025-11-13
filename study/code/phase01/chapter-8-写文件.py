import time

# w模式： 文件不存在会创建文件，存在的话会清空原内容
# a模式： 文件不存在会创建文件，存在的话会追加写入
f = open("../../../output.txt", "w", encoding="UTF-8")
content = """物是人非事事休，欲语泪先流"""
# 写入到内存缓冲区
f.write(content)

# time.sleep(500000)
# 刷到磁盘
# f.flush()

# close方法，内置了flush功能
f.close()