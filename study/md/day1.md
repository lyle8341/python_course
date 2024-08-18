+ python常用的6种值
  + 数字
    + 整数 int
    + 浮点数 float
    + 复数 complex
    + 布尔 bool True本质上是一个数字记作1， False记作0
  + 字符串
  + 列表
    + 有序可变序列
  + 元组
    + 有序不可变序列
  + 集合
    + 无序不重复集合
  + 字典
    + 无序key-value集合


+ 类型转换
  + int(x) 将x转换为一个整数
  + float(x)
  + str(x)


### 运算符

| 运算符                                              | 描述                           |
|--------------------------------------------------| ------------------------------ |
| `[]` `[:]`                                       | 下标，切片                     |
| `**`                                             | 指数                           |
| `~` `+` `-`                                      | 按位取反, 正负号               |
| `*` `/` `%` `//`                                 | 乘，除，模，整除               |
| `+` `-`                                          | 加，减                         |
| `>>` `<<`                                        | 右移，左移                     |
| `&`                                              | 按位与                         |
| `^` `\|`                                         | 按位异或，按位或               |
| `<=` `<` `>` `>=`                                | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                        | 等于，不等于                   |
| `is`  `is not`                                   | 身份运算符                     |
| `in` `not in`                                    | 成员运算符                     |
| `not` `or` `and`                                 | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `\|=` `^=` `>>=` `<<=` | （复合）赋值运算符             |

> **说明：** 在实际开发中，如果搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序。

+ for
```python
for i in "lyle":
    print(i)
```
+ range
  + range(101) 0~100
  + range(1,101) 1~100
  + range(1, 101, 2) 1~100,步长2
  + range(100, 0, -2)


+ for _ in range
  + When you are not interested in some values returned by a function we use underscore in place of variable name . Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.


+ 可变参数
  + ```python
    # 在参数名前面的*表示args是一个可变参数
    def add(*args):
        total = 0
        for val in args:
            total += val
        return total
    ```