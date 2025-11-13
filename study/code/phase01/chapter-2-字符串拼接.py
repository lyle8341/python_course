# 字面量拼接
print("lyle" + " is " + "a programmer")

name = "lyle"
job = "a programmer"
print(name + " is " + job)

# "+" 只能用于字符串拼接

"""
%s 将内容转成字符串，占位
%d 将内容转成整数，占位
%f 将内容转成浮点型，占位
"""
tip = "温馨提醒"
warning = "注意脚下"
message = "%s 雨天路滑 %s" % (tip, warning)
print(message)

# 字符串格式化，数字精度控制
"""
m.n
    m: 控制宽度，要求是数字，设置的宽度小于数字自身，不生效
    n: 控制小数点精度，要求是数字，会进行四舍五入
"""
num1 = 11
num2 = 3.14159
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字3.14159宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字3.14159宽度不限制，小数精度2，结果是：%.2f" % num2)

# 字符串格式化-快速写法
"""
格式:
    f"内容{变量名}"
"""
goods = "Mac Pro"
price = 20000
print(f"商品-{goods}，价格-{price}")

# 字符串格式化-表达式格式化
print("1 * 1的结果是：%d" % (1 * 1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在python中的类型是: %s" % type('字符串'))

my_str = "today is thursday"
v1 = my_str[2]  # d
print(v1)
v2 = my_str[-1]
print(v2)

is_idx = my_str.index("is")
print(is_idx)

# replace
"""
语法:
    字符串.replace(s1, s2)
    将字符串内的全部s1，替换为s2
    注意：不是修改字符串，而是得到了一个新字符串
"""

# split
sentence = "I am a programmer"
split_list = sentence.split(" ")
print(f"分割结果类型:{type(split_list)}, {split_list}")


# strip 去除前后空格
tip = "  only "
print(f"strip后：{tip.strip()}")
# strip("需要去除的符号")
"""
strip 删除集中的都会删除
"""
java_home = "123JAVA_HOME21321322311"
print(f"strip特定删除集: {java_home.strip('123')}")

#统计子串出现次数
content = "no no no oh"
print(f"字符串no出现次数: {content.count('no')}")

#统计字符串长度
print(f"字符串长度: {len('Hello')}")