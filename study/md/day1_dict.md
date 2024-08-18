+ 字典
```python
# 创建字典的字面量语法
scores = {'chinese': 34, 'math': 23, 'english': 12}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['chinese'])
print(scores['english'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['biology'] = 65
scores['physic'] = 71
scores.update(chemical=67, geography=85)
print(scores)
if 'biology' in scores:
    print(scores['biology'])
print(scores.get('biology'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('body', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('biology', 100))
# 清空字典
scores.clear()
print(scores)
```