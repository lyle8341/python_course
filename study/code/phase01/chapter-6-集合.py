"""
字面量集合
{e1, e2, e3 ...}

变量名 = {e1, e2, e3 ...}

空集合
变量名 = set()

无序，所以不支持索引访问
"""

my_set = {"python", "java", "java", "spring", "mysql", "rust"}
my_empty_set = set()

# 添加元素
my_set.add("cloud")
my_set.add("spring")

# 移除元素
my_set.remove("java")
print(my_set)

# 从集合中随机取一个元素，并被移除
my_set.pop();
print(my_set)

my_set.clear()

# difference 集合差集：得到一个新集合，原集合不变
s1 = {23, 6, 7, 5, 2}
s2 = {5, 2, 100, 35}

s3 = s1.difference(s2)
print(f"s1 - s2 = {s3}")

s4 = s2.difference(s1)
print(f"s2 - s1 = {s4}")

# difference_update s1被修改，s2不变
s1 = {23, 6, 7, 5, 2}
s2 = {5, 2, 100, 35}
s1.difference_update(s2)
print(s1)
print(s2)

# 合并
s1 = {23, 6, 7, 5, 2}
s2 = {5, 2, 100, 35}
s3 = s1.union(s2)
print(s3)

# 统计元素个数
print(len(my_set))

for e in s3:
    print(f"集合s3元素:{e}")
