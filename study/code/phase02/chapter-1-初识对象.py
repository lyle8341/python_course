class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    """
    class 类名成:
        成员变量
        
    def 成员方法(self, 参数列表):
        方法体
    * self关键字是成员方法定义的时候，必须填写的。
    
    对象 = 类名称()
    """

    def say_hi(self):
        """
        在方法内部，想要访问类的成员变量，必须使用self
        """
        print(f"Hello {self.name}")



stu = Student()
stu.name = "lyle"
stu.gender = "男"
stu.nationality = "CHINA"
stu.native_place = "陕西"
stu.age = 100

print()
