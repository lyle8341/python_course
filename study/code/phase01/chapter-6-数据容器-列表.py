"""
字面量
[e1, e2, e3, e4, ...]

变量
变量名 = [e1, e2, e3, ....]

定义空列表
变量名 = []
变量名 = list()
"""
candidate = ["lucy", "jack"]
name_list = ["joe", "john", "trump"]
print(name_list)
print(type(name_list))
print("============ 正向索引 start from 0 ============")
for i in range(3):
    print(name_list[i], end=" ")
print()
print("============ 反向索引 start from -1 ============")
for i in range(-1, -4, -1):
    print(name_list[i], end=" ")
print()

print("============ 混合类型 ============")
mix_list = [344, True, "lyle", 3.14]
print(mix_list)
print(type(mix_list))

print("============ 嵌套 ============")
embed_list = [[1, 2, 3], [4, 5, 6]]
print(embed_list)
print(type(embed_list))
print(embed_list[1][2])

# 查找列表元素-不存在会报错
index = mix_list.index("lyle")
print(f"lyle在mix_list列表中的下标索引是：{index}")

# 修改特定索引的值
name_list[0] = "smith"
print(name_list)
# 指定位置插入新元素
name_list.insert(1, "Taj")
print(name_list)
# 追加
name_list.append("coco")
print(name_list)
name_list.extend(candidate)
print(name_list)
# 删除元素-两种方式
del mix_list[2]
print(mix_list)
# 删除并返回
ele = mix_list.pop(0)
print(mix_list)

# 删除某个元素在列表中的第一个匹配项
name_list = ["joe", "john", "trump", "john"]
name_list.remove("john")
print(name_list)
# 清空
name_list.clear()

# 统计列表内某个元素的数量
name_list = ["joe", "john", "trump", "john"]
total = name_list.count("john")
print(f"john数量: {total}")

# 统计列表中全部元素个数
total = len(name_list)
print(f"列表元素数量: {total}")

# 列表遍历
index = 0
while index < len(name_list):
    tmp = name_list[index]
    print(tmp, end=" ")
    index += 1
print()

for e in name_list:
    print(e, end=" ")
