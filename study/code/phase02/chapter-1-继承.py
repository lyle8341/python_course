"""
class 类名(父类名):
    类内容体
"""


class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g is running")


class RemoteControl:
    type = "红外遥控"

    def control(self):
        print("红外开启了")


class FarFarFirst:
    pass


# 多继承中，如果父类有同名方法或属性，先继承的优先级高于后继承的
class PhonePro(Phone, RemoteControl, FarFarFirst):
    face_id = "011"

    def call_by_5g(self):
        print("5g is running")


pro = PhonePro()
print(pro.producer)
pro.call_by_4g()
pro.call_by_5g()
