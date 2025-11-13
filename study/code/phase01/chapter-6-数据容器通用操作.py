my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# len 元素个数
print(f"列表元素个数: {len(my_list)}")
print(f"元组元素个数: {len(my_tuple)}")
print(f"字符串元素个数: {len(my_str)}")
print(f"集合元素个数: {len(my_set)}")
print(f"字典元素个数: {len(my_dict)}")

# max 最大元素
print(f"列表  最大元素: {max(my_list)}")
print(f"元组  最大元素: {max(my_tuple)}")
print(f"字符串最大元素: {max(my_str)}")
print(f"集合  最大元素: {max(my_set)}")
print(f"字典  最大元素: {max(my_dict)}")

# min

# 容器转换 list(x) tuple(x) str(x) set(x)
print(f"列表转列表: {list(my_list)}")
print(f"元组转列表: {list(my_tuple)}")
print(f"字符串转列表: {list(my_str)}")
print(f"集合转列表: {list(my_set)}")
print(f"字典转列表: {list(my_dict)}")

print(f"列表转元组: {tuple(my_list)}")
print(f"元组转元组: {tuple(my_tuple)}")
print(f"字符串转元组: {tuple(my_str)}")
print(f"集合转元组: {tuple(my_set)}")
print(f"字典转元组: {tuple(my_dict)}")

print(f"列表转字符串: {str(my_list)}")
print(f"元组转字符串: {str(my_tuple)}")
print(f"字符串转字符串: {str(my_str)}")
print(f"集合转字符串: {str(my_set)}")
print(f"字典转字符串: {str(my_dict)}")

print(f"列表转集合: {set(my_list)}")
print(f"元组转集合: {set(my_tuple)}")
print(f"字符串转集合: {set(my_str)}")
print(f"集合转集合: {set(my_set)}")
print(f"字典转集合: {set(my_dict)}")

print("===================")
# 排序
my_list = [4, 2, 3, 1, 5]
my_tuple = (4, 1, 5, 3, 2)
my_str = "adehcgfb"
my_set = {4, 5, 3, 1, 2}
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(f"列表排序: {sorted(my_list)}")
print(f"元组排序: {sorted(my_tuple)}")
print(f"字符串排序: {sorted(my_str)}")
print(f"集合排序: {sorted(my_set)}")
print(f"字典排序: {sorted(my_dict)}")

print(f"列表排序: {sorted(my_list, reverse=True)}")