class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__
    def __str__(self):
        return f"Student类对象: name:{self.name}, age:{self.age}"

    # __lt__

    # __le__

    # __eq__


stu = Student("lyle", 30)

print(stu)
print(str(stu))
