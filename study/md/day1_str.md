# 字符串

+ 字符串三种定义方式
  + ```python
    name1 = '第一种'
    name2 = "第二种"
    name3 = """第三种""" # 使用变量接收它，它就是字符串，不实用变量接收就可以作为多行注释
    ```
  + 以三个双引号或单引号开头的字符串可以折行
    
+ 字符串拼接
  + ```
    name = 'lyle'
    age = 30
    message = "My name is %s, age is %d" % (name, age)
    print(message)
    ```
+ 字符串格式化
  + %m.nd
  + m控制宽度 
  + .n控制小数点精度
  + %5d 表示宽度控制在5位，如数字11，就会变成: [空格][空格][空格]11
  + 快速写法
    + 语法: f"内容{变量}"
    + print(f"我是{name}，年龄{age}")


+ 演示1
  ```
  s1 = 'hello ' * 3
  print(s1) # hello hello hello
  s2 = 'world'
  s1 += s2
  print(s1) # hello hello hello world
  print('ll' in s1) # True
  print('good' in s1) # False
  str2 = 'abc123456'
  # 从字符串中取出指定位置的字符(下标运算)
  print(str2[2]) # c
  # 字符串切片(从指定的开始索引到指定的结束索引)
  print(str2[2:5]) # c12
  print(str2[2:]) # c123456
  print(str2[2::2]) # c246
  print(str2[::2]) # ac246
  print(str2[::-1]) # 654321cba
  print(str2[-3:-1]) # 45
  ```    
  
+ 演示二
  ```
  str1 = 'hello, world!'
  # 通过内置函数len计算字符串的长度
  print(len(str1)) # 13
  # 获得字符串首字母大写的拷贝
  print(str1.capitalize()) # Hello, world!
  # 获得字符串每个单词首字母大写的拷贝
  print(str1.title()) # Hello, World!
  # 获得字符串变大写后的拷贝
  print(str1.upper()) # HELLO, WORLD!
  # 从字符串中查找子串所在位置
  print(str1.find('or')) # 8
  print(str1.find('shit')) # -1
  # 与find类似但找不到子串时会引发异常
  # print(str1.index('or'))
  # print(str1.index('shit'))
  # 检查字符串是否以指定的字符串开头
  print(str1.startswith('He')) # False
  print(str1.startswith('hel')) # True
  # 检查字符串是否以指定的字符串结尾
  print(str1.endswith('!')) # True
  # 将字符串以指定的宽度居中并在两侧填充指定的字符
  print(str1.center(50, '*'))
  # 将字符串以指定的宽度靠右放置左侧填充指定的字符
  print(str1.rjust(50, ' '))
  str2 = 'abc123456'
  # 检查字符串是否由数字构成
  print(str2.isdigit())  # False
  # 检查字符串是否以字母构成
  print(str2.isalpha())  # False
  # 检查字符串是否以数字和字母构成
  print(str2.isalnum())  # True
  str3 = '  jackfrued@126.com '
  print(str3)
  # 获得字符串修剪左右两侧空格之后的拷贝
  print(str3.strip())
  ```
