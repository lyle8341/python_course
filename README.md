# python_course
learn python


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







参考引用：
+ 1 .[Python-100-Days](https://github.com/jackfrued/Python-100-Days/tree/master)
+ 2 .[PythonScraping](https://github.com/Santostang/PythonScraping)
+ 3 .[examples-of-web-crawlers](https://github.com/shengqiangzhang/examples-of-web-crawlers)