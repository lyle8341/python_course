"""

[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

常用组合形式：
import 模块名
import 模块名 as 别名
from 模块名 import *
from 模块名 import 类、变量、方法等
from 模块名 import 功能名 as 别名
"""

# import 模块名 可以使用模块中的所有
# import time
# time.sleep(5)
# time.time()

# 只导入了模块的指定方法
# from time import sleep
# sleep(3)

# 作用同 import 模块名，只是写法不同
# from time import *
# sleep(4)

# 别名
import time as t
t.sleep(3)