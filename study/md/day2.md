# 面向对象编程基础

https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/08.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80.md




+ 类的私有成员变量
  + 变量名以 __开头(2个下划线)
+ 私有成员方法
  + 方法名以__开头(2个下划线)
+ 破解方法
  + 对象._类名__私有成员方法()
  + 对象._类名__私有成员属性




+ 继承
  ```
  class 类名(父类1, 父类2, 父类3...)
  ```
+ 调用父类同名成员
  + 方式一
    + 父类名.成员变量
    + 父类名.成员方法(self)
  + 方式二
    + super().成员变量
    + super().成员方法()



+ 变量类型注解
  + 基础语法 
    > 变量: 类型
  + ```python
    var_1: int = 10
    var_2: float = 3.14
    var_3: str = "lyle"
    ```
  + ```
    class Student:
      pass
    stu: Student = Student()
    
    my_list: list = [1,2,3]
    my_tuple: tuple = (1,2,3)
    my_set: set = {1,2,3}
    my_dic: dict = {"name":"lyle"}
    my_str: str = "good"
    
    my_list: list[int] = [1, 2, 3]
    my_tuple: tuple[str, int, bool] = ("nice", 2, True)
    my_set: set[int] = {1, 2, 3}
    my_dic: dict[str, str] = {"name": "lyle"}
    ```
  + 注释种进行类型注解
    ```python
    import json
    import random
    
    result = random.randint(1, 10) # type:int
    var_1 = json.loads('{"name":"lyle"}') #type:dict[str, str]
    def func():
        return 10
    var_3 = func() # type:int
    ```

+ 函数和方法形参类型注解
  > def 函数方法名(形参名: 类型, 形参名: 类型,形参名: 类型...) -> 返回值类型:


+ union
  ```python
  from typing import Union

  my_list: list[Union[str, int]] = [1, 2, "night"]
  my_dict: dict[str, Union[str, int]] = {"name": "lyle", "age": 30}
  
  def func(data: Union[int, str]) -> Union[str, int]:
    pass
  ```
  

+ 多态
  ```python
  class Animal:
      def speak(self):
          pass
  
  
  class Dog(Animal):
      def speak(self):
          print("wang wang wang")
  
  
  class Cat(Animal):
      def speak(self):
          print("miao miao miao")
  
  def make_noise(animal: Animal):
      animal.speak()
  
  if __name__ == '__main__':
      dog = Dog()
      cat = Cat()
      make_noise(dog)
      make_noise(cat)
  ```
  
+ 抽象类
  + 含有抽象方法的类称之为抽象类
+ 抽象方法
  + 方法体是空实现（pass）称之为抽象方法