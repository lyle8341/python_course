class Student:

    # 成员变量定义可以省略哦
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


stu = Student("lyle", 30, "110")
