"""
变量设置类型注解:
语法  变量:类型

"""

var_1: int = 40
var_2: float = 3.14
var_3: bool = True
var_4: str = "hello"


class Student:
    pass


# 类对象类型注解
stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"lyle": 23}
my_str: str = "name"

my_list: list[int] = [1, 2, 3]
# 元组类型需要将每一个元素都标记出来
my_tuple: tuple[str, int, bool] = ("lyle", 22, True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"age": 44}
