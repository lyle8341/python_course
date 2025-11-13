"""
序列：内容连续，有序，可使用下标索引的一类数据容器
切片： 从一个序列中，取出一个子序列，切片不会影响序列本身，而是会得到一个新的序列

语法:
    序列[起始下标:结束下标:步长]
    起始下标：留空视作从头开始
    结束下标（不含）：留空视作截取到结尾
    步长：
        步长1：一个个取元素
        步长2：每次跳过 1 个元素取
        步长N：每次跳过N-1个元素取
        步长负数：反向取（注意：起始下标和结束下标也要反向标记）
"""

# list切片
my_list = [0, 1, 2, 3, 4, 5, 6]
new_list = my_list[1:4]  # 默认步长是1
print(my_list)
print(new_list)  # [1, 2, 3]

# tuple切片
my_tuple = (0, 1, 2, 3, 4, 5, 6)
# 从头到尾 步长1
new_tuple = my_tuple[:]
print(new_tuple)

# str切片 从头到尾 步长2
my_str = "abcdefgh"
new_str = my_str[::2]
print(new_str)

# str 从头到尾， 步长-1
r_new_str = my_str[::-1]
print(r_new_str)

# str 从3开始，到1结束 步长-1
r_new_str = my_str[3:1:-1]
print(r_new_str)

# str从头到尾 步长-2
new_my_tuple = my_tuple[::-2]
print(new_my_tuple)
