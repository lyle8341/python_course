+ 元组
```python
# 定义元组
t = ('abc', 12, True, '木乃伊')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '哦耶'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('伊莫顿', 30, True, '埃及')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = 'xxoo'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
```

+ 为什么还需要元组这样的类型呢
  + 1 .元组中的元素是无法修改的
  + 2 .元组在创建时间和占用的空间上面都优于列表