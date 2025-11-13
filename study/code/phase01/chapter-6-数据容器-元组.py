"""
元组 不可修改
元组中如果有列表元素，这个列表元素里面的值可以修改。

字面量
(e1, e2, e3, e4, ...)

变量
变量名 = (e1, e2, e3, ....)

定义空列表
变量名 = ()
变量名 = tuple()
"""

t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(type(t1))

# 定义单个元素的元组， 一定要加个逗号！！！，否则就不是元组类型了
t4 = ("nice",)

# 元组嵌套
t5 = ((1, 2, 3), (4, 5, 6))

t6 = ("java", "python", "c++", "c", "rust", "java")
pi = t6.index("python")
print(f"python的索引是: {pi}")

java_total = t6.count("java")
print(f"统计java个数: {java_total}")
print(f"t6元素数量: {len(t6)}")

# 遍历同列表
