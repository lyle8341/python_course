# python_course

### 1.安装python
+ ☑️add python xx to PATH

+ 命令简写
  + echo 'alias python="python3"' >> .bash_profile

+ linux有个默认的老版本python
  + rm -f /usr/bin/python
  + ln -s /usr/local/python3.10.4/bin/python3.10 /usr/bin/python
  + vim /usr/libexec/urlgrabber-ext-down
    + 首行改成 /usr/bin/python2
  + vim /usr/bin/yum
    + 首行改成 /usr/bin/python2

### 2.解释器
+ python.exe


+ 函数的说明文档
  ```python
  def func(x, y):
      """
      函数功能描述
      :param x: 形参x
      :param y: 形参y
      :return: 和
      """
      print("this is doc")
      return x + y
  ```
+ 多个返回值
  ```python
  def more_return():
      return 12, 13
  
  
  if __name__ == '__main__':
      a, b = more_return()
      print(a)
      print(b)
  ```

+ 三元表达式
  > res = 条件成立时返回的值 if 条件 else 条件不成立时返回的值

+ 列表生成式（列表推导式）
  > [表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]

  > egg_list=['鸡蛋%s' %i for i in range(10)]
+ 集合推导式
  > formula = {str2 for str2 in str1 if len(str2) >= 4}
+ 字典推导式
  > formula = {key: value for key, value in dict1.items() if key == 'name'}
 
+ 生成器表达式
  > (expression for item in iterable if condition)
  
  + 与列表生成式的语法格式相同，只需要将[ ]换成( )


+ mysql
  + pip install pymysql cryptography


参考引用：
+ 1 .[Python-100-Days](https://github.com/jackfrued/Python-100-Days/tree/master)
+ 2 .[PythonScraping](https://github.com/Santostang/PythonScraping)
+ 3 .[examples-of-web-crawlers](https://github.com/shengqiangzhang/examples-of-web-crawlers)