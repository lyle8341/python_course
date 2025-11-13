# 导入全部，*导入all列表中的
from chapter_9_my_module import *

test(4, 5)
sub(2, 3)

# 导入全部
import chapter_9_my_module as my_module

my_module.test(1, 2)
my_module.mul(4, 5)

# 导入指定
from chapter_9_my_module import test

test(3, 4)



# 导入自己创建的包
# import study.code.my_package.my_module1 as my_module1
# import study.code.my_package.my_module2 as my_module2
# my_module1.info_print1()
# my_module2.info_print2()


# from study.code.my_package import my_module1
# from study.code.my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

from study.code.my_package import *
my_module1.info_print1()
# my_module2.info_print2()