"""
字典字面量
{key:value, key:value, key:value ...}

变量名 = {key:value, key:value ...}

空字典
变量名 = {}
变量名 = dict()
"""
my_dict = {"name": "lyle", "age": 30}

# 空字典
m_d1 = {}
m_d2 = dict()

# 获取
name = my_dict["name"]
print(name)

# 新增
my_dict["sex"] = "Male"
# 修改
my_dict["age"] = 35
print(my_dict)

# 删除元素
result = my_dict.pop("sex")
print(result)

# 元素个数
print(len(my_dict))

# 全部keys
key_list = my_dict.keys()
print(key_list)

# 遍历方式一
for key in my_dict.keys():
    print(f"{key}:{my_dict[key]}")

# 遍历方式二
for key in my_dict:
    print(f"{key}:{my_dict[key]}")

# 清空
my_dict.clear()
