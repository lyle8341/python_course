"""
json数据和字典转换
"""

import json

data = [
    {"name": "lyle", "age": 10},
    {"name": "TOM", "age": 2},
    {"name": "john", "age": 34},
    {"name": "孙悟空", "age": 600}
]

# ensure_ascii处理中文编码问题
json_str = json.dumps(data, ensure_ascii=False)

print(type(json_str))
print(json_str)

# 字典转json
d = {"name": "月杰伦", "addr": "西藏"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

list_str = '[{"name": "lyle", "age": 10}, {"name": "TOM", "age": 2}, {"name": "john", "age": 34}, {"name": "孙悟空", "age": 600}]'
lj = json.loads(list_str)
print(type(lj))
print(lj)

dict_str = '{"name": "月杰伦", "addr": "西藏"}'
dj = json.loads(dict_str)
print(type(dj))
print(dj)